from app import create_app
from bs4 import BeautifulSoup
import pytest
import re

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SITE_URL': 'https://test.com',
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def fetch_soup(client, path):
    rv = client.get(path)
    assert rv.status_code == 200
    return BeautifulSoup(rv.data, 'lxml')

def test_unique_titles(client):
    titles = {}
    pages = ['/', '/about/', '/experience/', '/education/', '/skills/', '/projects/', '/contact/', '/privacy/']
    for page in pages:
        soup = fetch_soup(client, page)
        title = soup.title.string.strip() if soup.title else ''
        assert title, f'{page} has no title'
        assert title not in titles, f'{page} has duplicate title: {title}'
        titles[title] = page

def test_unique_meta_descriptions(client):
    descs = {}
    pages = ['/', '/about/', '/experience/', '/education/', '/skills/', '/projects/', '/contact/', '/privacy/']
    for page in pages:
        soup = fetch_soup(client, page)
        meta = soup.find('meta', attrs={'name': 'description'})
        assert meta, f'{page} has no meta description'
        desc = meta.get('content', '')
        assert desc, f'{page} has empty meta description'
        assert desc not in descs, f'{page} has duplicate meta description'

def test_images_have_alt(client):
    pages = ['/', '/about/', '/experience/', '/education/', '/skills/', '/projects/', '/contact/']
    for page in pages:
        soup = fetch_soup(client, page)
        for img in soup.find_all('img'):
            assert img.get('alt') is not None, f'{page} has image without alt: {img}'

def test_json_ld_valid(client):
    soup = fetch_soup(client, '/')
    script = soup.find('script', type='application/ld+json')
    assert script, 'No JSON-LD found'
    import json
    data = json.loads(script.string)
    assert data['@context'] == 'https://schema.org'
    assert data['@type'] == 'Person'
    assert data['name'] == 'Harmanan Gurvinder Kohli'

def test_sitemap_contains_all_routes(client):
    rv = client.get('/sitemap.xml')
    soup = BeautifulSoup(rv.data, 'xml')
    urls = [loc.text for loc in soup.find_all('loc')]
    expected = ['/', '/about/', '/experience/', '/education/', '/skills/', '/projects/', '/contact/', '/privacy/']
    site_url = 'https://test.com'
    for path in expected:
        assert f'{site_url}{path}' in urls, f'{path} missing from sitemap'

def test_robots_txt_valid(client):
    rv = client.get('/robots.txt')
    text = rv.data.decode()
    assert 'User-agent:' in text
    assert 'Sitemap:' in text
    assert 'Allow: /' in text
