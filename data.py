from Circular_Linked_List import Circular_Linked_List


# ~~<<< SCALES >>>~~

tones = ['C', ['C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'F', [
    'F#', 'Gb'], 'G', ['G#', 'Ab'], 'A', ['A#', 'Bb'], 'B']

scales = ['C', 'C#', 'Db', 'D', 'Eb', 'E', 'F',
          'F#', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


def flatting_list(list):
    flatlist = []
    for element in list:
        if type(element) == list:
            flatlist += flatting_list(element)
        else:
            flatlist += element
    return flatlist


tones_flat = flatting_list(tones)

major_scale_formula = [2, 4, 5, 7, 9, 11]
minor_natural_scale_formula = [2, 3, 5, 7, 8, 10]
minor_harmonic_scale_formula = [2, 3, 5, 7, 8, 11]


# ~~<<< CHORDS >>>~~


# MAJOR SCALES CHORDS: I, ii, iii, IV, V, vi, viidim
# MINOR NATURAL SCALE CHORDS: i, iidim, III, iv, v, VI, VII
# MINOR HARMONIC SCALE CHORDS: i, iidim, IIIaug, iv, V, VI, viidim


major_scale_chord_prog = ['Major', 'minor', 'minor',
                          'Major', 'Major', 'minor', 'diminished']
minor_natural_scale_chord_prog = [
    'minor', 'diminished', 'Major', 'minor', 'minor', 'Major', 'Major']
minor_harmionic_scale_chord_prog = [
    'minor', 'diminished', 'augumented', 'minor', 'Major', 'Major', 'diminished']

chord = [2, 4]
dim_chord = [15, 18]
aug_chord = [4, 8]


# ~~<<< DATA >>>~~

# All tones as Circular Linked List:

tones_list = Circular_Linked_List()

for tone in tones:
    tones_list.append_node(tone)


# Major/ Minor natural / Minor harmonic scales as Circular Linked List, and then as scales progressions as Lists in Dict:

# Scales

major_chord_progression = {}

minor_natural_progression = {}

minor_harmonic_scales_progression = {}

# Chords

major_chords = {}

minor_chords = {}

aug_chords = {}

dim_chords = {}

# LOOP FOR SCALES AND CHORDS FROM TONES

for note in tones_flat:

    # Major scale and chord ------------>
    major_scale = tones_list.make_list_from_list(note, major_scale_formula)
    if note in scales:
        major_chord_progression[note] = major_scale.generating_list(
            major_scale_chord_prog)

    # Major chords
    major_chords[note +
                 ' Major'] = major_scale.make_list_from_list(note, chord).gen_pure_list()        
    # Augumented chords
    aug_chords[note + ' augumented'] = tones_list.make_list_from_list(
        note, aug_chord).gen_pure_list()

    # Minor natural ------------>
    minor_natural_scale = tones_list.make_list_from_list(
        note, minor_natural_scale_formula)
    if note in scales:
        minor_natural_progression[note] = major_scale.generating_list(
            minor_natural_scale_chord_prog)

    # Minor chords
    minor_chords[note + ' Minor'] = minor_natural_scale.make_list_from_list(
        note, chord).gen_pure_list()

    # Diminished chords
    dim_chords[note + ' diminished'] = tones_list.make_list_from_list(
        note, dim_chord, 'dim').gen_pure_list()

    # Minor harmonic ------------>
    minor_harmonic_scale = tones_list.make_list_from_list(
        note, minor_harmonic_scale_formula)
    if note in scales:
        minor_harmonic_scales_progression[note] = major_scale.generating_list(
            minor_harmionic_scale_chord_prog)


