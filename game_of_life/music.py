# import synthesizer
from synthesizer import Player, Synthesizer, Waveform

from mygamefile import Game

many_notes = [["C4", "D4", "E4", "F4", "G4", "A4", "B4",
         "C5", "D5", "E5", "F5", "G5", "A5", "B5",
         "C6", "D6", "E6", "F6", "G6", "A6"],
        ["C4", "D4", "E4", "D4", "C4", "D4", "E4",
         "D5", "C4", "D4", "E4", "D4", "C4", "D4",
         "E4", "D4", "C4", "D4", "E4", "D4"],
        ["C4", "F4", "G4", "F4", "C4", "F4", "G4",
         "F5", "C4", "F4", "G4", "F4", "C4", "F4",
         "G4", "F4", "C4", "F4", "G4", "F4"],
         ]


def play_notes(notes_to_play, duration=1.0):
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.3, use_osc2=False)
    player = Player()
    player.open_stream()
    player.play_wave(synthesizer.generate_chord(notes_to_play, duration))


def play_a_note(cursor_x):
    note_to_play = many_notes[0][cursor_x]
    play_notes([note_to_play], 0.3)


def make_music(game: Game, prev_board):
    n_i = 0
    any_changed = False
    notes_to_play = []
    total_newly_alive_cells = 0
    for row_i, row in enumerate(game.board):
        prev_row = prev_board[row_i]
        for i, cell in enumerate(row):
            prev_cell = prev_row[i]
            if cell == 1 and cell!=prev_cell:
                total_newly_alive_cells += 1
                any_changed = True
                notes_to_play.append(many_notes[total_newly_alive_cells % 3][i])
    if any_changed:
        # print(game.board)
        print(notes_to_play)
        play_notes(notes_to_play)