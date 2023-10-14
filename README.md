# alea

[![PyPI](https://img.shields.io/pypi/v/alea.svg)](https://pypi.org/project/alea/)
[![Changelog](https://img.shields.io/github/v/release/spstolar/alea?include_prereleases&label=changelog)](https://github.com/spstolar/alea/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/spstolar/alea/blob/main/LICENSE)

assistant for aleatoric music ideas

## Installation

Install this library using `pip`:

    pip install alea

## Usage

Usage instructions go here.

## Development

When you add `music21` it will create `~/.music21rc`. It is convenient to add the path to MuseScore4.exe to the `midiPath` XML element. This way you can immediately launch a result without having to manually move files around and select it from the MS4 browser. See [this chapter](https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html) for more.

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd alea
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
