import os
from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read()

setup(
    name='map_grapher',
    version='0.1',
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    author='Mohamed Leila',
    scripts=[],
    description='This package provides an easy interface to model US national and state maps as an undirected graph represented by an adjacency matrix. The graph model can be passed to an external solver to obtain a solution. The package will then reconstruct a colored map from the solution'
)
