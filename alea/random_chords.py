from music21 import stream, chord
import random


def random_chord():
    num_notes = 3
    note_vals = random.sample(range(0, 12), k=num_notes)
    random_chord = chord.Chord(note_vals)
    return random_chord


class ChordCollection:
    def __init__(self, num_chords) -> None:
        self.chords = [random_chord() for _ in range(num_chords)]

    def to_stream(self):
        chord_stream = stream.Stream()
        for c in self.chords:
            c.duration.type = "half"
            chord_stream.append(c)

        return chord_stream


def random_chord_stream(num_chords=4):
    chord_stream = stream.Stream()
    chords = [random_chord() for _ in range(num_chords)]
    for c in chords:
        chord_stream.append(c)
    return chord_stream


if __name__ == "__main__":
    chords = ChordCollection(num_chords=8)
    my_stream = chords.to_stream()
    my_stream.show("midi")
