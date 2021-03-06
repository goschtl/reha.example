#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

test_requires = [
    'WebTest',
    'importscan',
    'pytest',
    'pytest-cov',
    'reha.testing'
]

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("docs/HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ['borb', 'uvcreha', "setuptools"]


setup_requirements = ""

setup(
    name="reha.example",
    author="UV WEB Community",
    author_email="ck@novareto.de",
    version="0.1.0",
    description="Example Python namespace package.",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    url="https://git.bg-kooperation.de",
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=[
        "reha",
    ],
    setup_requires=setup_requirements,
    entry_points={
        "fanstatic.libraries": [
            "reha.example  = reha.example.app:library",
        ],
        "reiter.application.modules": ["reha.example = reha.example"],
    },
    extras_require={
        'test': test_requires,
    },
    test_suite='tests',
    zip_safe=False,
)
