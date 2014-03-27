# -*- coding: utf-8 -*-
"""
    StarClusterReliableIPCluster
    ~~~~~~~~~~

    A Starcluster plugin adding support for running ipcluster with
    supervisord monitoring the processes.
"""

from setuptools import setup


setup(
    name='StarClusterReliableIPCluster',
    version='0.0.1',
    url='https://github.com/telmewheretoeat/StarClusterReliableIPCluster',
    license='LGPL3',
    author='Cory Dolphin',
    author_email='wcdolphin@gmail.com',
    description="A Starcluster plugin adding support for running ipcluster"
    "with supervisord monitoring",
    py_modules=['ipclustersupervisord'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Starcluster',
    ],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public '
        'License (LGPL)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Clustering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
