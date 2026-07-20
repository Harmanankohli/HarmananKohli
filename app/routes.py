import json
import os
from flask import render_template, Response

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path) as f:
        return json.load(f)

def register_routes(app):

    @app.context_processor
    def inject_globals():
        profile = load_json('profile.json')
        return dict(profile=profile, site_url=app.config.get('SITE_URL', ''))

    @app.route('/')
    def index():
        profile = load_json('profile.json')
        projects = load_json('projects.json')
        return render_template('index.html', profile=profile, projects=projects)

    @app.route('/about/')
    def about():
        profile = load_json('profile.json')
        return render_template('about.html', profile=profile)

    @app.route('/experience/')
    def experience():
        timeline = load_json('timeline.json')
        return render_template('experience.html', timeline=timeline)

    @app.route('/academics/')
    def academics():
        academics_data = load_json('academics.json')
        return render_template('academics.html', academics=academics_data)

    @app.route('/skills/')
    def skills():
        return render_template('skills.html')

    @app.route('/projects/')
    def projects():
        projects = load_json('projects.json')
        return render_template('projects.html', projects=projects)

    @app.route('/contact/')
    def contact():
        return render_template('contact.html')

    @app.route('/privacy/')
    def privacy():
        return render_template('privacy.html')

    @app.route('/robots.txt')
    def robots():
        content = "User-agent: *\nAllow: /\nSitemap: " + app.config.get('SITE_URL', '') + "/sitemap.xml\n"
        return Response(content, mimetype='text/plain')

    @app.route('/sitemap.xml')
    def sitemap():
        pages = ['/', '/about/', '/experience/', '/academics/', '/skills/', '/projects/', '/contact/', '/privacy/']
        site_url = app.config.get('SITE_URL', '')
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for page in pages:
            xml += '  <url>\n'
            xml += f'    <loc>{site_url}{page}</loc>\n'
            xml += '  </url>\n'
        xml += '</urlset>'
        return Response(xml, mimetype='application/xml')
