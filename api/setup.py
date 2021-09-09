from setuptools import setup
from tndc_api.api import (
    name, version, author, email, description)

OPTS = dict(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=email,
    packages=[f'{name}.api'],
    zip_safe=False,
    install_requires=[
        'blinker',
        'gunicorn',
        'gevent',
        'flask',
        'flask-restful',
        'flask-sqlalchemy',
        'flask-migrate',
        'marshmallow',
        'pyyaml',
        'healthcheck'
    ]
)

if __name__ == '__main__':
    setup(**OPTS)
