import os
from setuptools import setup

setup(
    name='pyKEGGscape',
    version='0.1.0',
    author='Kozo Nishida',
    author_email='knishida@riken.jp',
    license='MIT',
    url='https://github.com/kozo2/pyKEGGscape',
    py_modules=['pykeggscape'],
    description='A simple Python wrapper around the KEGG API, cyREST and Cytoscape.',
    keywords='kegg python rest cytoscape pathway bioinformatics',
    install_requires=['biopython', 'py2cytoscape'],
    test_suite='pykeggscape_test',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
