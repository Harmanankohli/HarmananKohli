from flask_frozen import Freezer
from app import create_app

app = create_app()
freezer = Freezer(app)

@freezer.register_generator
def download_file():
    yield {'filename': 'Harmanan_Kohli_Professional.pdf'}
    yield {'filename': 'Harmanan_Kohli_Academic.pdf'}

if __name__ == '__main__':
    freezer.freeze()
