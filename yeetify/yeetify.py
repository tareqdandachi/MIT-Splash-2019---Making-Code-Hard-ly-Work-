#!/usr/bin/python3

import sys
import random

DEFAULT_YEETINGS = {"Yeet":"return", "YEET":"main", "Yeeeet":"(", "yeeeeT":")", "yeett":"int", "yeet":"printf", "Yeeet":"{", "yeeeT":"}", "yoted":";"}

def get_file_info(file_name):

    f = open(file_name, "r")

    contents = f.read()

    return contents

def yeet_dem_string(line, mappings):

    for char in "\'\"":

        while char in line:

            first_char = line.find(char)

            string_to_yeet = line[first_char+1:]

            second_char = string_to_yeet.find(char)

            string_to_yeet = string_to_yeet[:second_char]

            print('yo', string_to_yeet)

            if string_to_yeet != "":

                string_to_yeet = '"' + string_to_yeet + '"'

                yeeter = gimme_a_yeet(mappings)

                line = line.replace(string_to_yeet, yeeter)

                mappings[yeeter] = string_to_yeet

    return line, mappings

def gimme_a_yeet(mappings):

    mappings = set(mappings.keys())

    yeet = "yeet"

    while yeet in mappings:

        random_yeet = ""

        for i in "yeet":

            a, b = random.random(), random.random()

            if a < 0.4:

                random_yeet += i

            else:

                random_yeet += i*int(a*b*10)

        yeet = ''.join(map(yeet_regular_capitalisation_away_from_me_you_piece_of_yeet, random_yeet))

    return yeet

def yeet_regular_capitalisation_away_from_me_you_piece_of_yeet(string_to_yeet):

    if random.random() > 0.5:

        return string_to_yeet.upper()

    return string_to_yeet.lower()

def yeetify(code, mappings=DEFAULT_YEETINGS):

    code = code.split("\n")

    for i in range(len(code)):

        if not "#include" in code[i] and not "#define" in code[i]:

            code[i], mappings = yeetify_line(code[i], mappings)

    for yeet, mapping in mappings.items():

        code.insert(0, "#define " + yeet + " " + mapping)

    code = "\n".join(code)

    return code

def check_yeetification(possibly_a_yoted_string):

    return set(possibly_a_yoted_string.lower()) == {"y", "e", "t", " "}

def yeetify_line(line, mappings):

    line = " " + line + " "

    if line == "": return "", mappings

    line, mappings = yeet_dem_string(line, mappings)

    for yeet, mapping in mappings.items():

        if not mapping in "{(^:\"'!)};": mapping = " "+mapping+" "

        line = line.replace(mapping, " "+yeet+" ")

    for yeet, mapping in mappings.items():

        if not mapping in "{(^:\"'!)}": mapping = " "+mapping+" "

        line = line.replace(mapping, " "+yeet+" ")

    grand_yote = line.split(" ")

    for yote in grand_yote:

        if not check_yeetification(yote) and yote.replace(" ", "") != "":

            yeet_pass = gimme_a_yeet(mappings)

            line = line.replace(yote, yeet_pass)

            mappings[yeet_pass] = yote

    line = line[1:-1]

    line = line.replace("  ", " ")

    return line, mappings

if __name__ == "__main__":

    file_name = sys.argv[1]

    code = get_file_info(file_name)

    print(yeetify(code))

    # for line in code.split("\n"):
    #
    #     print(yeet_dem_string(line, DEFAULT_YEETINGS)[0])