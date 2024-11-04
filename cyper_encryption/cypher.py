from pprint import pprint
from random import random, randint

from Tools.scripts.dutree import display


def y_cord_cal(user_input):
    y_count = 0
    y_state = True
    y_cord_array = []
    for i in range(len(user_input)):
        if y_state:
           y_cord_array.append(y_count)
           y_count += 1
           if y_count == 3:
               y_state = False
        else:
            y_cord_array.append(y_count)
            y_count -= 1
            if y_count == 0:
                y_state = True
    return y_cord_array

def cypher_text(user_input):
    text_len = len(user_input)
    cyper_array = [[] for _ in range(text_len)]
    display_cyper_array = [[]for _ in range(4)]
    rise_fall_state = True
    rise_fall_counter = 0
    y_alg = 0
    y_cords = y_cord_cal(user_input)
    output_string = ""


    for i in range(text_len):
        for z in range(4):
            if z == y_cords[i]:
                cyper_array[i].append(user_input[i])
            else:
                ran_num = randint(33, 126)
                cyper_array[i].append(chr(ran_num))

    for i in range(4):
        display_array = []
        for z in range(text_len):
            display_array.append(cyper_array[z][i])
        display_cyper_array[i] = display_array
        output_string += "".join(display_array)
    pprint(display_cyper_array)
    return output_string

user_input = input('Enter text: ')
print(cypher_text(user_input))