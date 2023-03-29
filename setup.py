# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import os
from setuptools import setup, find_packages
from pathlib import Path

here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

version = None
version_file = Path('.') / 'pd' / 'version.py'
if version_file.exists():
    with open(version_file, encoding='utf-8') as f:
        version_dict = {}
        exec(f.read(), version_dict)
        version = version_dict.get("VERSION", version)

setup(
    name="step-sdk",
    version=version,
    description="Parallel Domain Python Step and Stream SDK",
    author="Parallel Domain",
    author_email="support@paralleldomain.com",
    url="https://github.com/parallel-domain/pd-api-py",
    setup_requires=[
        'wheel'
    ],
    install_requires=[
        'flatbuffers==1.*',
        'numpy',
        'pyquaternion',
        'pyzmq',
        'protobuf==3.*',
        'opencv-python-headless',
        'click',
        'shapely',
        'dacite',
        'requests',
        'peewee',
        'matplotlib',
    ],
    extras_require={
        'visualization': [
            'opencv-python',
        ],
        'dev': [
            'pytest',
            'pytest-repeat',
            'requests-mock',
            'imgui[glfw]',
            'tqdm',
        ],
        'docs': [
            'Sphinx',
            'sphinx-rtd-theme',
            'myst-parser',
            'scanpydoc',
            'sphinx-autodoc-typehints',
            'sphinx-paramlinks',
            'breathe',
            'exhale',
            'sphinxcontrib-redoc'
        ]
    },
    packages=find_packages(include=['pd', 'pd.*']),
    include_package_data=True,
    python_requires=">=3.8",
    project_urls={
        "Documentation": "https://docs.paralleldomain.com",
        "Source Code": "https://github.com/parallel-domain/pd-api-py",
    },
)
