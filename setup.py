import setuptools
from setuptools import find_packages

setuptools.setup(
    name='US_VISA',
    version='0.0.0',
    author='amit sahoo',
    author_email='amitsahoo1989@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language:: Python::3",
        "License:: OSI Approved::MIT License",
        "Operating System:: OS independent"
    ],
    python_requires = '>=3.6'
)