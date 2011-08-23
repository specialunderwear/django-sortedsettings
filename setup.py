#!/usr/bin/env python
"""
Django-sortedsettings
-------------------

A script that outputs all the values in your settings.py, but ordered
alphabetically.

usage::

    sortsettings.py

This will dump the settings.py module sorted

or::

    sortsettings.py settings.someothermodule

This will dump the settings/someothermodule.py module sorted
"""
from distutils.core import setup

setup(
    name='django-sortedsettings',
    version='1.0',
    description="Sort the django settings module's entries alphabetically",
    long_description=__doc__,
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