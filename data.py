

# notes = ['C', ['C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'E#',
#          'F', ['F#', 'Gb'], 'G', ['G#', 'Ab'], 'A', ['A#', 'Bb'], 'B', 'C', [
#              'C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'E#',
#          'F', ['F#', 'Gb'], 'G', ['G#', 'Ab'], 'A', ['A#', 'Bb'], 'B']


notes = ['Cb', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#',
         'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 
         'Cb', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#',
         'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'Cb']


# Major scale formula U (tonika),  W, W, H, W, W, W, H (tonika)


major_formula = [1, 1, 0, 1, 1, 1]


def creating_scale(note, formula):
    scale = []
    scale_note_index = notes.index(note)
    scale.append(note)
    marker = 0

    for step in formula:
        if step == 1:
            marker += 3
            scale.append(notes[scale_note_index + marker])
        else:
            marker += 2
            scale.append(notes[scale_note_index + marker])

    return scale


print(creating_scale('D', major_formula))
print(creating_scale('C', major_formula))
print(creating_scale('G', major_formula))
print(creating_scale('E', major_formula))
print(creating_scale('F#', major_formula))
print(creating_scale('B', major_formula))
print(creating_scale('A', major_formula))
print(creating_scale('Eb', major_formula))




scales = {'C': ['Cmaj', 'Dmin', 'Emin', 'Fmaj', ' Gmaj', 'Amin', 'Bdim']}
