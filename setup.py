#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-sortedsettings',
    version='1.0',
    description="Sort the django settings module's entries alphabetically",
    author='Lars van de Kerkhof',
    author_email='sortedsettings@permanentmarkers.nl',
    url='https://github.com/specialunderwear/django-sortedsettings',
    scripts=['sortsettings.py'],
    license='GPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: System :: Installation/Setup'
    ],
    
)