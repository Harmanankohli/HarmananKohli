from app import create_app
import pytest

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

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Harmanan' in rv.data

def test_about_page(client):
    rv = client.get('/about/')
    assert rv.status_code == 200

def test_experience_page(client):
    rv = client.get('/experience/')
    assert rv.status_code == 200

def test_education_page(client):
    rv = client.get('/education/')
    assert rv.status_code == 200

def test_skills_page(client):
    rv = client.get('/skills/')
    assert rv.status_code == 200

def test_projects_page(client):
    rv = client.get('/projects/')
    assert rv.status_code == 200

def test_contact_page(client):
    rv = client.get('/contact/')
    assert rv.status_code == 200

def test_privacy_page(client):
    rv = client.get('/privacy/')
    assert rv.status_code == 200

def test_robots_txt(client):
    rv = client.get('/robots.txt')
    assert rv.status_code == 200
    assert b'Sitemap' in rv.data

def test_sitemap_xml(client):
    rv = client.get('/sitemap.xml')
    assert rv.status_code == 200
    assert b'<urlset' in rv.data

def test_all_pages_have_meta(client):
    pages = ['/', '/about/', '/experience/', '/education/', '/skills/', '/projects/', '/contact/']
    for page in pages:
        rv = client.get(page)
        assert rv.status_code == 200
        assert b'<meta name="description"' in rv.data, f'{page} missing meta description'
