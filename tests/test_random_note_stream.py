import pytest
from music21 import note

from alea.random_note_stream import random_note, create_random_notes, random_note_stream


# Test random note generation
def test_random_note():
    n = random_note()
    assert isinstance(n, note.Note)
    # we want it to be within a certain range
    assert 30 <= n.pitch.ps <= 70


# Test creating multiple random notes
def test_create_random_notes():
    notes = create_random_notes(3)
    assert len(notes) == 3
    assert all(isinstance(n, note.Note) for n in notes)


# Test random note stream generation
def test_random_note_stream():
    s = random_note_stream(4)
    assert len(s) == 4
    assert all(isinstance(n, note.Note) for n in s)
