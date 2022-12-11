from Circular_Linked_List import Circular_Linked_List
from Tree import *
import re

# All musical tones, as the basic building blocks of the program, also scales for which we will search for chords.
tones = ['C', ['C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'F', [
    'F#', 'Gb'], 'G', ['G#', 'Ab'], 'A', ['A#', 'Bb'], 'B']

scales = ['C', 'C#', 'Db', 'D', 'Eb', 'E', 'F',
          'F#', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


def flatting_list(list):
    #Classic flatting list function
    flatlist = []
    for element in list:
        if type(element) == list:
            flatlist += flatting_list(element)
        else:
            flatlist += element
    return flatlist


tones_flat = flatting_list(tones)

# Formulas for major and minor scales. 
# The numbers indicate the interval distances between the tones that make up a given scale. 
major_scale_formula = [2, 4, 5, 7, 9, 11]
minor_natural_scale_formula = [2, 3, 5, 7, 8, 10]
minor_harmonic_scale_formula = [2, 3, 5, 7, 8, 11]

# Chord formulas in the same manner.
chord = [2, 4]
dim_chord = [15, 18]
aug_chord = [4, 8]

# Numbers and chord mode, will be useful later, during iteration, to append substance to the generated strings.
major_scale_chord_prog = ['Major (I) 1', 'minor (ii) 2', 'minor (iii) 3',
                          'Major (IV) 4', 'Major (V) 5', 'minor (VI) 6', 'diminished (vi) 7']
minor_natural_scale_chord_prog = [
    'minor (i) 1', 'diminished (ii) 2', 'Major (III) 3', 'minor (iv) 4', 'minor (v) 5', 'Major (VI) 6', 'Major (VII) 7']
minor_harmionic_scale_chord_prog = [
    'minor (i) 1', 'diminished (ii) 2', 'augumented (iii) 3', 'minor (iv) 4', 'Major (V) 5', 'Major (VI) 6', 'diminished (vii) 7']



# ~~<<< DATA >>>~~

# All tones as Circular Linked List:

# Creating from the initial variable with a list of tones a looped Circular_Linked_List, in order to generate from it the scales and chords.
tones_list = Circular_Linked_List()
for tone in tones:
    tones_list.append_node(tone)

# Empty dictionaries will be populated by methods of Circular_Linked_List class
major_chord_progression = {}
minor_natural_progression = {}
minor_harmonic_scales_progression = {}
major_chords = {}
minor_chords = {}
aug_chords = {}
dim_chords = {}

# Lopping through each tone in the scale to make a major and two minor scales for each tone, 
# also a major and minor chord, a diminished and aougumented. Formulas for scales and chords
# in numerical form and their intervals are expressed in line 27. 
# Lists will be added to the above dictionaries in the formula:
# {scale tone: a list with the tones that fall within its scope}. Analogously with chords.

for note in tones_flat:
    # Major scale and chord 
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
    minor_chords[note + ' minor'] = minor_natural_scale.make_list_from_list(
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


# TREE 
# Inserting finished lists within the tree structure. 

def adding_to_tree(chord_progression, scale):
    for key, value in chord_progression.items():
        scale_child = TreeNode(key)
        scale.add_child(scale_child)
        for chord in value:
            chord_leaf = TreeNode(chord)
            scale_child.add_child(chord_leaf)
            
# TREE SCHEME:

#                SCALES
#           /      |      \
#          /       |       \
#       Major   Minor     Minor II
#      / | \    / | \     / | \
#     C  D  E  C  D  E   C  D   E  //e.g

# Initializing the tree class with root and leafs
scale_root = TreeNode('Scales')
major_child = TreeNode('Major')
minor_natural_child = TreeNode('Minor Natural')
minor_harmonic_child = TreeNode('Minor Harmonic')
scale_root.children = [major_child, minor_natural_child, minor_harmonic_child]

# Adding particular scales as leafs
adding_to_tree(major_chord_progression, major_child)
adding_to_tree(minor_natural_progression, minor_natural_child)
adding_to_tree(minor_harmonic_scales_progression, minor_harmonic_child)

