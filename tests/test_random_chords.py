import pytest
from music21 import stream, chord

from alea.random_chords import random_chord, ChordCollection, random_chord_stream


def test_random_chord():
    chord1 = random_chord()
    assert len(chord1.pitches) == 3


def test_chord_collection():
    num_chords = 5
    cc = ChordCollection(num_chords)
    assert len(cc.chords) == num_chords

    chord_stream = cc.to_stream()
    assert len(chord_stream) == num_chords
    for c in chord_stream:
        assert isinstance(c, chord.Chord)
        assert c.duration.type == "half"


def test_random_chord_stream():
    num_chords = 4
    stream = random_chord_stream(num_chords)
    assert len(stream) == num_chords
    for c in stream:
        assert isinstance(c, chord.Chord)
