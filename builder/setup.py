from pathlib import Path

from setuptools import setup, find_packages

from version import __version__ as version


ROOT_PATH = Path(__file__).parent
README_PATH = ROOT_PATH.parent / "README.md"

long_description = README_PATH.read_text()

setup(
    name="mypy-boto3-builder",
    version=version,
    packages=find_packages(),
    url="https://github.com/vemel/boto3_type_annotations",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Builder for mypy-boto3.",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Typing :: Typed",
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["mypy_boto3_builder = main:main"]},
)