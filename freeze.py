import os
from flask_frozen import Freezer
from app import create_app

app = create_app()
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    docs_dir = os.path.join(os.path.dirname(__file__), 'docs')
    open(os.path.join(docs_dir, '.nojekyll'), 'w').close()
    with open(os.path.join(docs_dir, 'CNAME'), 'w') as f:
        f.write('harmanan.is-a.dev')
