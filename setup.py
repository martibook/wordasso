import setuptools
import codecs
import os


def local_file(file):
    return codecs.open(os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8')


setuptools.setup(
    name="wordasso",
    version="0.1.0",
    author="Author",
    author_email="martibook@outlook.com",
    description="Several word association function based on datamuse API",
    long_description=local_file('README.rst').read(),
    url="https://github.com/martibook/wordasso.git",
    packages=["wordasso"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
