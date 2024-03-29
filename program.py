import data
import Tree
import re


def split_and_sort(list):
    # A function that divides the results after a BFS search and sorts the chords in order from I to VII
    for element in list:
        degree = int(str(element[3])[-1])
        element.append(degree)
        element[3] = str(element[3])[:-2]

    sorted_list = sorted(list, key=lambda x: x[-1])

    return sorted_list


def print_result(list):
    #Printing the results as follows: -->> Scale: Chord (function/number)
    print('This chord is found in the following scales:')

    for element in list:
        print(f"-->> {element[2]} {element[1]} scale: {element[3]}")


def set_chord():
    # Talking to the player, asking what chord he is looking for, first what sound second what mode.
    checker = None
    chord = ''
    while checker == None:
        answer = input('What chord do you want to find?\n')
        checker = check_note(answer)
        if checker == None:
            answer = input('There is no such note, try again\n')
            checker = check_note(answer)

        chord += checker

    checker_2 = None
    while checker_2 == None:
        checker_2 = check_type(answer)
        if checker_2 == None:
            answer = input(
                'There is no such chord type in our database, you can search for Major, minor, augumented or diminished chord\n')
        else:
            chord += checker_2

    print(f'You are searching for {chord} chord.')
    request = input(
        'Right, or do you want to look for another one? Typ again / con\n')

    if request == 'con':
        return chord
    else:
        set_chord()



# Check_note/check_type function:
# A regex implementation so that the program understands the various abbreviations 
# the player used to specify the chord: C flat/B/b Major/major/major, etc.
# Further translate to the standard in which these names are specified in the data structure.

def check_note(string):
    good = r'^([A-G]|[a-g]{1})'
    if re.search(good, string):
        note = string[0].upper()
        if re.search(r'(sharp|#)', string):
            note += '#'
        if re.search(r'(flat|b)', string):
            note += 'b'

        return note

    else:
        return None


def check_type(string):

    if re.search(r'(M?m?inor|M?m?in)', string):
        return ' minor'
    elif re.search(r'(M?m?ajor|M?m?aj)', string):
        return ' Major'
    elif re.search(r'(D?d?iminished|D?d?im)', string):
        return ' diminished'
    elif re.search(r'(A?a?gumented|A?a?ug)', string):
        return ' augumented'
    else:
        return None


def searching_chord():
    # The main function that handles talking to the player, 
    # specifying what he or she is looking for and searching for a chord.
    chord = set_chord()
    list_of_scales = split_and_sort(Tree.bfs(data.scale_root, chord))
    print_result(list_of_scales)
    display_notes(chord)

    question = None
    while question not in ['again', 'exit']:
        question = input('Okay, do you want to look for another chord or are we done? Type again/exit\n')

        if question == 'again':
            searching_chord()

        if question == 'exit':
            return


def display_notes(chord):
    # Additional functionality if the player would like to know what tones go into a chord.
    question = None
    while question not in ['y', 'n']:
        question = input(
            'Great, do you want to see the notes that go into this chord? y/n\n')

        if question == 'y':
            if 'Major' in chord:
                print(data.major_chords[chord])
            elif 'minor' in chord:
                print(data.minor_chords[chord])
            elif 'augmented' in chord:
                print(data.aug_chords[chord])
            else:
                print(data.dim_chords[chord])

        if question == 'n':
            return


def descript():
    print('Hello, this app finds a chord and its degree in major and minor scales. ')


def exit():
    print('Thanks, bye')


def conversation():
    descript()
    searching_chord()
    exit()



conversation()
