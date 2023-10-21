from music21 import stream, chord
import random


MAJOR_INTERVALS = [0, 2, 4, 5, 7, 9, 11]


# when you provide all integers < 12, it is assumed to be an octaveless pitch class,
# so all notes will be relative to middle C. This is more restrictive than we want,
# so we will boost the octave _and_ randomly bump to increase the randomness
def random_chord():
    num_notes = 3
    octave = 4
    note_vals = random.sample(range(0, 12), k=num_notes)
    transposition_amount = octave * 12 + random.randint(-7, 7)
    note_vals = [n + transposition_amount for n in note_vals]
    random_chord = chord.Chord(note_vals)
    return random_chord


def random_major_chord():
    num_notes = 3
    note_vals = random.sample(MAJOR_INTERVALS, k=num_notes)
    result_chord = chord.Chord(note_vals)
    return result_chord


class ChordCollection:
    def __init__(self, num_chords, flavor="major") -> None:
        if flavor == "major":
            self.chords = [random_major_chord() for _ in range(num_chords)]
        else:
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
    chords = ChordCollection(num_chords=8, flavor="major")
    my_stream = chords.to_stream()
    my_stream.show("midi")
