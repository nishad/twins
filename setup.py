from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="univ",
    version="0.01",
    description="A command line utility for coins",
    load_description=long_description,
    url="http://github.com/coins14/twins",
    py_modules=["coins"],
    scripts=["univ"],
    install_requires=open("requirements.txt").read().split('\n'),
    packages=find_packages(),
    classfiers = [
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: Utilities"
    ]
)
