from music21 import note, stream
import random

def random_note():
    note_val = random.randint(30, 70)
    print(note_val)
    return note.Note(note_val) 

def create_random_notes(num_notes=4):
    return [random_note() for _ in range(num_notes)]

def random_note_stream(num_notes=4):
    notes = create_random_notes(num_notes)
    note_stream = stream.Stream()
    for note in notes:
        note_stream.append(note)

    return note_stream

def save_note_stream(filename=None):
    if filename is None:
        filename = f"example_midi/{num_notes}_notes.midi"
    fp = note_stream.write("midi", fp=filename)

if __name__ == "__main__":
    note_stream = random_note_stream(8)
    note_stream.show("midi")
