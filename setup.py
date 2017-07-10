from setuptools import setup, find_packages

__version__ = '0.1.0'

setup(
    name='alembic_demo',
    description='Alembic demo',
    version=__version__,
    author='Rod Glover',
    author_email='rglover@uvic.ca',
    url='https://github.com/rod-glover/alembic-demo',
    install_requires='''
        alembic
    '''.split()
)