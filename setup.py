import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-oppia-implementations',
    version='0.3.0',
    packages=['oppia_implementations',
              'oppia_implementations.api'],
    include_package_data=True,
    license='GNU GPL v3 License',  # example license
    description='OppiaMobile learning platform implementations server',
    long_description=README,
    url='https://digital-campus.org/',
    author='Alex Little, Digital Campus',
    author_email='alex@digital-campus.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "django==4.2.15",
        "Pillow==10.3.0",
        "django-ses == 3.5.2",
        "sorl-thumbnail==12.10.0",
        "djangorestframework==3.15.2",
        "djangorestframework-api-key==3.0.0"
    ],
)
