import random
from assets.constants import N4, Int

def generate_chord():
    chord_flavors = [
        major_triad,
        minor_triad,
        diminished_triad,
        augmented_triad,
        suspended_second,
        suspended_fourth,
        add_ninth,
        major_seventh,
        dominant_seventh,
        minor_seventh,
        half_diminished,
        full_diminished,

    ]
    chord_flavor = random.choice(chord_flavors)
    random_note = random.choice(list(N4))
    chord = chord_flavor(random_note.value)
    return chord
#    return chord_flavor(random_note.value)


def major_triad(note) -> tuple[list[int], str]:
    tonic = note
    maj3  = note * Int['M3']
    maj5  = note * Int['P5']
    return [tonic, maj3, maj5], "M"

def minor_triad(note) -> tuple[list[int], str]:
    tonic = note
    min3  = note * Int['m3']
    maj5  = note * Int['P5']
    return [tonic, min3, maj5], "m"

def diminished_triad(note) -> tuple[list[int], str]:
    tonic = note
    min3  = note * Int['m3']
    trit  = note * Int['tri']
    return [tonic, min3, trit], "d"

def augmented_triad(note) -> tuple[list[int], str]:
    tonic = note
    maj3  = note * Int['M3']
    min6  = note * Int['m6']
    return [tonic, maj3, min6], "a"

def suspended_second(note) -> tuple[list[int], str]:
    tonic = note
    maj2  = note * Int['M2']
    maj5  = note * Int['P5']
    return [tonic, maj2, maj5], "s2"

def suspended_fourth(note) -> tuple[list[int], str]:
    tonic = note
    maj4  = note * Int['P4']
    maj5  = note * Int['P5']
    return [tonic, maj4, maj5], "s4"

def add_ninth(note) -> tuple[list[int], str]:
    tonic = note
    maj3  = note * Int['M3']
    maj5  = note * Int['P5']
    maj9  = note * Int['M9']
    return [tonic, maj3, maj5, maj9], "a9"

def major_seventh(note) -> tuple[list[int], str]:
    tonic = note
    maj3  = note * Int['M3']
    maj5  = note * Int['P5']
    maj7  = note * Int['M7']
    return [tonic, maj3, maj5, maj7], "M7"

def dominant_seventh(note) -> tuple[list[int], str]:
    tonic = note
    maj3  = note * Int['M3']
    maj5  = note * Int['P5']
    dom7  = note * Int['m7']
    return [tonic, maj3, maj5, dom7], "d7"

def minor_seventh(note) -> tuple[list[int], str]:
    tonic = note
    min3  = note * Int['m3']
    maj5  = note * Int['P5']
    min7  = note * Int['m7']
    return [tonic, min3, maj5, min7], "m7"

def half_diminished(note) -> tuple[list[int], str]:
    tonic = note
    min3  = note * Int['m3']
    trit  = note * Int['tri']
    min7  = note * Int['m7']
    return [tonic, min3, trit, min7], "d7"

def full_diminished(note) -> tuple[list[int], str]:
    tonic = note
    min3  = note * Int['m3']
    trit  = note * Int['tri']
    ff7   = note * Int['M6']
    return [tonic, min3, trit, ff7], "dd7"

def first_inversion(chord: list[str], label: str):
    if len(chord) == 3:
        return [chord[1], chord[2], chord[0]], label + " 1st"
    elif len(chord) == 4:
        return [chord[1], chord[2], chord[3], chord[0]], label + " 1st"

def second_inversion(chord: list[str], label: str):
    if len(chord) == 3:
        return [chord[2], chord[0], chord[1]], label + " 2nd"
    elif len(chord) == 4:
        return [chord[2], chord[3], chord[0], chord[1]], label + " 2nd"

def third_inversion(chord: list[str], label: str):
    return [chord[3], chord[0], chord[1], chord[2]], label + " 3rd"