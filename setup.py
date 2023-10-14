from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="alea",
    description="assistant for aleatoric music ideas",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="psi",
    url="https://github.com/spstolar/alea",
    project_urls={
        "Issues": "https://github.com/spstolar/alea/issues",
        "CI": "https://github.com/spstolar/alea/actions",
        "Changelog": "https://github.com/spstolar/alea/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["alea"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
