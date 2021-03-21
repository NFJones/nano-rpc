#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = []
with open("requirements.txt", "r") as infile:
    install_requires = [r for r in infile.read().split("\n") if r]

setup(
    name="nano-rpc",
    version="2021.0",
    description="Interact with the Nano RPC API from the command line.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NFJones/nano-rpc",
    author="Neil F Jones",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="nano crypto rpc",
    packages=["nano_rpc"],
    python_requires=">=3.5, <4",
    install_requires=install_requires,
    entry_points={"console_scripts": ["nano_rpc = nano_rpc.main:main"]},
)
