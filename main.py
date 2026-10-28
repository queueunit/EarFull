import sounddevice as sd
import numpy as np
import sys
from pathlib import Path
from enum import Enum
import argparse

from assets.constants import SAMPLE_RATE, N4
from src.chord_type_mode import generate_chord
from src.generate_piano_note import generate_piano_note
from src.Player import Player

def main():
    name = input("Enter your name: ") 
    player_path = Path(f"profiles/{name}.json")
    if player_path.exists():
        player = Player(name, player_path)
    else:
        player = Player(name)
    chord_frequencies, type = generate_chord()
#    chord_frequencies = [N4.C.value, N4.E.value, N4.G.value]
    duration = 3.0
    total_samples = int(SAMPLE_RATE * duration)

    # Combine the notes into a chord
    chord_audio = np.zeros(total_samples)
    for freq in chord_frequencies:
        chord_audio += generate_piano_note(freq, duration=duration)

    # Scale down volume to prevent clipping
    chord_audio = (chord_audio / len(chord_frequencies)) * 5.0

    # Play the synthesized piano chord live
    print(f"Playing synthesized piano chord of type {type}")
    sd.play(chord_audio, SAMPLE_RATE)
    sd.wait()
    

#def generate_piano_note(frequency, duration=2.5):
#    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
#    
#    # 1. Piano Harmonic Structure (relative amplitudes of overtones)
#    # Pianos have prominent harmonics that decay differently than the fundamental note.
#    harmonics = [
#        (1.0, 1.0, 0.5),   # (harmonic multiplier, initial amplitude, decay rate)
#        (2.0, 0.6, 0.7),
#        (3.0, 0.3, 0.9),
#        (4.0, 0.15, 1.2),
#        (5.0, 0.08, 1.5)
#    ]
#    
#    wave = np.zeros_like(t)
#    for mult, amp, decay in harmonics:
#        # Higher harmonics decay faster in a real piano string
#        harmonic_envelope = np.exp(-decay * t)
#        wave += amp * harmonic_envelope * np.sin(2 * np.pi * frequency * mult * t)
#        
#    # 2. Global ADSR Volume Envelope (simulates hammer strike and note decay)
#    # Fast attack, smooth exponential decay
#    global_envelope = np.exp(-1.5 * t)
#    
#    # Apply envelope and normalize
#    note = wave * global_envelope
#    return note / np.max(np.abs(note))


if __name__ == "__main__":
    main()
