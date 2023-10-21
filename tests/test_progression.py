import pytest
from music21 import chord, stream

from alea.progression import ProgressionMaker


# Test initialization of ProgressionMaker
def test_ProgressionMaker_init():
    pm = ProgressionMaker("C")
    assert pm.root_note == "C"
    # make sure there are at least 2 octaves of notes available to pull from
    assert len(pm.pitches) >= 14


# Test getting correct triad notes
def test_get_triad_notes():
    pm = ProgressionMaker("C")
    # the first triad of the C Major progression should be CEG in the third octave
    assert pm.get_triad_notes(0) == ["C3", "E3", "G3"]


# Test chord progression creation
def test_create():
    pm = ProgressionMaker("C")
    cs = pm.create()

    # there should be 4 chords
    assert len(cs) == 4
    assert all(isinstance(c, chord.Chord) for c in cs)

    # the chord bases (minus octaves) should be C F G C
    assert [str(c.root())[:-1] for c in cs] == ["C", "F", "G", "C"]


# Test end-to-end with different root note
def test_integration():
    pm = ProgressionMaker("D")
    cs = pm.create()

    assert len(cs) == 4

    assert [str(c.root())[:-1] for c in cs] == ["D", "G", "A", "D"]
