import re
import xml.etree.ElementTree as ET
import sys
import os
sys.dont_write_bytecode = True

if __name__ == "__main__":
    #Notes files
    dict_patients = {}
    num_files = len(os.listdir(os.path.dirname(
        sys.path[0]) + '/Codes/MimicIII/Noteevents_output/'))
    i = 0
    for txt_test_file in os.listdir(os.path.dirname(sys.path[0]) + '/Codes/MimicIII/Noteevents_output/'):
        i += 1
        print("Process - Patient number: " + str(i))
        print("Process - Progress: " + str(i*100/num_files) + "%")
        if txt_test_file[-3:]=="txt":
            subject_id = txt_test_file[:-19]
            filepath = os.path.dirname(
                sys.path[0]) + '/Codes/MimicIII/Noteevents_output/' + txt_test_file
            textfile = open(filepath, 'r')
            filetext = textfile.read()
            textfile.close()
            matches = set(re.findall("(C\d{7})", filetext))
            matches_str = ' '.join(matches)
            #print(matches_str)
            filepath_write = os.path.dirname(
                sys.path[0]) + '/Codes/MimicIII/Patients/Cuis/' + txt_test_file[:len(txt_test_file) - 15]
            with open(filepath_write, 'w') as f:
                f.write(matches_str)