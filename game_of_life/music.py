# import synthesizer
from synthesizer import Player, Synthesizer, Waveform

from mygamefile import Game

def play_notes(notes_to_play, duration=1.0):
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.3, use_osc2=False)
    player = Player()
    player.open_stream()
    player.play_wave(synthesizer.generate_chord(notes_to_play, duration))

def make_music(game: Game):
    notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4",
             "C5", "D5", "E5", "F5", "G5", "A5", "B5",
             "C6", "D6", "E6", "F6", "G6", "A6"]
    any_alive = False
    live_columns = []
    for row in game.board:
        for i, cell in enumerate(row):
            if cell==1:
                any_alive = True
                live_columns.append(notes[i])
    if any_alive:
        print(game.board)
        play_notes(live_columns)