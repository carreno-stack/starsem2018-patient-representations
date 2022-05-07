import re
import xml.etree.ElementTree as ET
import sys
import os
sys.dont_write_bytecode = True

if __name__ == "__main__":
    #Notes files
    dict_patients = {}
    num_files = len(os.listdir(os.path.dirname(
        sys.path[0]) + '/Codes/MimicIII/Noteevents_output_negation/'))
    i = 0
    for txt_test_file in os.listdir(os.path.dirname(sys.path[0]) + '/Codes/MimicIII/Noteevents_output_negation/'):
        i += 1
        print("Process - Patient number: " + str(i))
        print("Process - Progress: " + str(i*100/num_files) + "%")
        #if txt_test_file == "99383.txt.properties.txt":
        if txt_test_file[-3:]=="txt":
            subject_id = txt_test_file[:-19]
            filepath = os.path.dirname(
                sys.path[0]) + '/Codes/MimicIII/Noteevents_output_negation/' + txt_test_file
            textfile = open(filepath, 'r')
            filetext = textfile.read()
            textfile.close()
            #matches = set(re.findall("(C\d{7})", filetext))
            #matches_str = ' '.join(matches)
            #print(matches_str)
            #regex = re.compile('(( negated)?\n.*\n.*)', re.S)
            #matches_str = regex.sub(lambda m: m.group().replace('"',"%",1), filetext)
            
            
            
            matches = set(re.findall("(\"( negated)?\n.*\n.*)", filetext))
            match_str = [] 
            for item in matches:
                #print(item[0])
                #print(item[1])
                string = re.sub("(\n)","",item[0])
                string = re.sub("(\t)","",string)
                string = re.sub("  "," ",string)
                string = re.sub("\" ","",string)
                string = re.sub("negated \S+ ","n",string)
                #print("Original string: "+string)
                string = re.sub("\D+ ","",string)
                #print("New string: "+string)
                string=set(re.findall("(n?C\d{7})", string))
                matches_str = ' '.join(string)
                match_str.append(matches_str)
            match_str = ' '.join(match_str)
            
            filepath_write = os.path.dirname(
                sys.path[0]) + '/Codes/MimicIII/Patients/Cuis/' + txt_test_file[:len(txt_test_file) - 15]
            with open(filepath_write, 'w') as f:
                f.write(match_str)