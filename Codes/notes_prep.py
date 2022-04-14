import numpy as np
import sys
import os
import csv
sys.dont_write_bytecode = True

note_events_file = os.path.dirname(
    sys.path[0]) + '/Codes/MimicIII/NOTEEVENTS.csv'

dict_notes = {}

with open(note_events_file, newline='') as file_name:
    note_events = csv.reader(file_name, delimiter=",", quotechar='"')
    row_count = 2083182
    print("Number of rows: " + str(row_count))
    i = 0
    for row in note_events:
        i += 1
        print("Process - Row number: " + str(i))
        print("Process - Progress: " + str(i*100/row_count) + "%")
        try:
            dict_notes[row[1]].append(row[10])
        except KeyError:
            dict_notes[row[1]] = [row[10]]

dict_length = len(dict_notes)
print("Dictionary length: " + str(dict_length))

i=0
for subject in dict_notes:
    i += 1
    path = sys.path[0] + '/MimicIII/Noteevents_txt/'#+str(i % 30+1)+'/'
    print(path)
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    print("Write - Row number: " + str(i))
    print("Write - Progress: " + str(i*100/dict_length) + "%")
    filepath = os.path.dirname(path) +'/'+ subject + '.txt'
    print(filepath)
    with open(filepath, 'w') as f:
        f.write(' '.join(dict_notes[subject]))
