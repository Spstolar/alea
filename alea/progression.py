from music21 import chord, stream, scale


class ProgressionMaker:
    def __init__(self, root_note):
        self.root_note = root_note
        self.scale = scale.MajorScale(root_note)
        # restrict to two octaves of notes
        self.pitches = [
            str(p) for p in self.scale.getPitches(root_note + "3", root_note + "5")
        ]

    def get_triad_notes(self, base: int):
        return self.pitches[base : base + 5 : 2]

    def create(self):
        bases = [0, 3, 4, 0]
        chords = [chord.Chord(self.get_triad_notes(b)) for b in bases]
        chord_stream = stream.Stream()
        for c in chords:
            c.duration.type = "half"
            chord_stream.append(c)
        return chord_stream


if __name__ == "__main__":
    progger = ProgressionMaker("c")
    chord_stream = progger.create()
    chord_stream.show("midi")
