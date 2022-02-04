# !/usr/bin/env python

from distutils.core import setup

setup(
    name='cookiecutter-pypackage',
    packages=[],
    version='0.5.0',
    description='Cookiecutter template for a PyWPS service',
    license='BSD',
    author='Carsten Ehbrecht',
    author_email='ehbrecht@dkrz.de',
    url='https://github.com/bird-house/cookiecutter-birdhouse',
    keywords=['cookiecutter', 'template', 'package', 'wps' 'pywps', 'birdhouse'],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)
