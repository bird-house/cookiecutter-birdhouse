# !/usr/bin/env python

from setuptools import setup

with open("requirements_dev.txt") as f:
    dev_requirements = f.read().splitlines()

setup(
    name='cookiecutter-birdhouse',
    packages=[],
    version='0.5.0',
    description='Cookiecutter template for a PyWPS service',
    license='BSD',
    author='Carsten Ehbrecht',
    author_email='ehbrecht@dkrz.de',
    url='https://github.com/bird-house/cookiecutter-birdhouse',
    keywords=['cookiecutter', 'template', 'package', 'wps' 'pywps', 'birdhouse'],
    extras_require={
        "dev": dev_requirements,
    },
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
