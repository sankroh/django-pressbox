from setuptools import setup, find_packages

setup(
    name = 'django-pressbox',
    version = '0.1.0',
    description = 'This is a simple press item management application for your Django powered site.',
    keywords = 'django apps',
    license = 'New BSD License',
    author = 'Kevin Fricovsky',
    author_email = 'kevin@howiworkdaily.com',
    maintainer = 'Rohit Sankaran',
    maintainer_email = 'rohit@lincolnloop.com',
    url = 'http://github.com/roadhead/django-pressbox/',
    dependency_links = [],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
)

