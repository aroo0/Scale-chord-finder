
from Circular_Linked_List import Circular_Linked_List


#               ~~<<< SCALES >>>~~


scales = ['C', 'C#', 'Db', 'D', 'Eb', 'E', 'F',
          'F#', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


tones = ['C', ['C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'F', [
    'F#', 'Gb'], 'G', ['G#', 'Ab'], 'A', ['A#', 'Bb'], 'B']


tones_clist = Circular_Linked_List()

for tone in tones:
    tones_clist.append_node(tone)

# print(tones_clist)


print(tones_clist.make_list_from_list('A'))

# major_form = [2, 4, 5, 7, 9, 11]
# minor_harm_form = [2, 3, 5, 7, 8, 11]

# def find_index(note, tones):
#     if note in tones:
#         scale_note_index = tones.index(note)
#     else:
#         for tone in tones:
#             if note in tone:
#                 scale_note_index = tones.index(tone)

#     return scale_note_index


# def creating_scale(note, formula):
#     scale = Circular_Linked_List()
#     scale_note_index = find_index(note, tones)
#     scale.append(note)

#     for step in formula:
#         to_check_note = tones[scale_note_index + step]
#         if type(to_check_note) == list:
#             if scale[-1][0] in to_check_note[0]:
#                 scale.append(to_check_note[1])
#             else:
#                 scale.append(to_check_note[0])
#         else:
#             scale.append(to_check_note)

#     return scale


# def creating_scale(note, formula):
#     scale = []
#     scale_note_index = find_index(note, tones)
#     scale.append(note)

#     for step in formula:
#         to_check_note = tones[scale_note_index + step]
#         if type(to_check_note) == list:
#             if scale[-1][0] in to_check_note[0]:
#                 scale.append(to_check_note[1])
#             else:
#                 scale.append(to_check_note[0])
#         else:
#             scale.append(to_check_note)

#     return scale


# ~~<<< CHORDS >>>~~

# MINOR SCALES CHORDS: i, ii dim, III, iv, V, VI, vii dim
# MAJOR SCALES CHORDS: I, ii, iii, IV, V, vi, vii dim
