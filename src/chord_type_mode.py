import random
from assets.constants import N4

def generate_chord():
    chord_flavors = [
        major_triad,
        minor_triad,
        diminished_triad,
        augmented_triad,
    ]
    chord_flavor = random.choice(chord_flavors)
    random_note = random.choice(list(N4))
    return chord_flavor(random_note.value)


def major_triad(note) -> list[int]:
    tonic = note
    maj3  = note * (2 ** (1/3))
    maj5  = note * (2 ** (7/12))
    return [tonic, maj3, maj5], "M"

def minor_triad(note) -> list[int]:
    tonic = note
    min3  = note * (2 ** (3 / 12))
    maj5  = note * (2 ** (7/12))
    return [tonic, min3, maj5], "m"

def diminished_triad(note) -> list[int]:
    tonic = note
    min3  = note * (2 ** (3 / 12))
    trit  = note * (2 ** (1 / 2))
    return [tonic, min3, trit], "d"

def augmented_triad(note) -> list[int]:
    tonic = note
    maj3  = note * (2 ** (1/3))
    min6  = note * (2 ** (8/12))
    return [tonic, maj3, min6], "a"