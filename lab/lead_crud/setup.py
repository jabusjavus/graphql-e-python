import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid >= 1.9a',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'sqlalchemy_utils',
    'transaction',
    'zope.sqlalchemy',
    'alembic',
    'waitress',
    'graphene>=2.0',
    'webob-graphql>=1.0.dev',
]

tests_require = [
    'ipython',
    'ipdb',
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
    'pyre-check'
]

setup(
    name='lead_crud',
    version='0.0',
    description='lead crud',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = lead_crud:main',
        ],
        'console_scripts': [
            'initialize_lead_crud_db = lead_crud.scripts.initializedb:main',
        ],
    },
)
