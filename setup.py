#!/usr/bin/env python3
"""
Setup script for GTK Python Dashboard Starter
"""

from setuptools import setup, find_packages
import os

# Read requirements
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read README if it exists
long_description = ""
if os.path.exists('README.md'):
    with open('README.md', 'r') as f:
        long_description = f.read()

setup(
    name='gtk-python-dashboard-starter',
    version='1.0.0',
    description='A modular template for building GTK3 desktop applications in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/gtk-python-dashboard-starter',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'dashboard=main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
