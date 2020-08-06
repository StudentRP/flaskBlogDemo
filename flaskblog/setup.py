import setuptools

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PoWeR", # Replace with your own username
    version="0.0.1",
    author="RP",
    author_email="Pylorusred@yahoo.com",
    description="First test at fullstack blog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=None,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
