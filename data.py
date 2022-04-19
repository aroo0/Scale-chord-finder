

notes = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'B']


# Major scale formula U (tonika),  W, W, H, W, W, W, H (tonika)

cmaj = []
major_formula = [1, 1, 0, 1, 1, 1, 0]



def creating_scale(note, formula):
    scale = []
    scale_note_index = notes.index(note)
    scale.append(note)
        
    for index in range(len(formula)):
        for note in notes[scale_note_index:]:
            marker = 0
            if scale[index] == 1:




    return scale














scales = {'C': ['Cmaj', 'Dmin', 'Emin', 'Fmaj',' Gmaj', 'Amin', 'Bdim']}