
#               ~~<<< SCALES >>>~~

notes = ['Cb', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#',
         'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'Cb',
         'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#',
         'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'Cb']



major_formula = [1, 1, 0, 1, 1, 1]
minor_harmonic_formula = [1, 0, 1, 1, 0, 2]

scales = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F',
    'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']

def creating_scale(note, formula):
    scale = []
    scale_note_index = notes.index(note)
    scale.append(note)
    marker = 0

    for step in formula:
        if step == 1:
            marker += 3
        elif step == 2:
            marker += 4
        else:
            marker += 2

        scale.append(notes[scale_note_index + marker])

    return scale

minor_scales = {}
major_scales = {}

for scale in scales:
    minor_scales[scale] = creating_scale(scale, minor_harmonic_formula)
    major_scales[scale] = creating_scale(scale, major_formula)


# print(minor_scales)
# print(major_scales)


###                 ~~<<< CHORDS >>>~~

### MINOR SCALES CHORDS: i, ii dim, III, iv, V, VI, vii dim
### MAJOR SCALES CHORDS: I, ii, iii, IV, V, vi, vii dim