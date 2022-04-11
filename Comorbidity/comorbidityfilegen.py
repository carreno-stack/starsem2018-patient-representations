import xml.etree.ElementTree as ET
import sys
import os
sys.dont_write_bytecode = True

if __name__ == "__main__":
    #Test files
    for xmi_test_file in os.listdir(os.path.dirname(sys.path[0]) + '/Comorbidity/Test_records_output/'):        
        if xmi_test_file[-3:]=="xmi":
            xmi_file = os.path.dirname(
                sys.path[0]) + '/Comorbidity/Test_records_output/' + xmi_test_file
            print(xmi_file)
            tree = ET.parse(xmi_file)
            root = tree.getroot()
            dictionary_polarity = {}
            dictionary_cui = {}
            
            for child in root:
                if 'ontologyConceptArr' in child.attrib:
                    dictionary_polarity.update(dict.fromkeys(child.attrib.get(
                        'ontologyConceptArr').split(), "n" if child.attrib.get('polarity') == "-1" else "y"))
            
            for child in root:
                if 'cui' in child.attrib:
                    dictionary_cui.update(dict.fromkeys(child.attrib.get("cui").split(), dictionary_polarity.get(child.attrib.get("{http://www.omg.org/XMI}id"))))
            
            output_string = ""
                    
            for key in dictionary_cui:
                output_string = output_string + ("n" if dictionary_cui[key]=="n" else "") + str(key) + " "
            
            filepath = os.path.dirname(
                sys.path[0]) + '/Comorbidity/Cuis/Test/' + xmi_test_file[:len(xmi_test_file) - 4]
            with open(filepath, 'w') as f:
                f.write(output_string)
    
    #Train files
    for xmi_train_file in os.listdir(os.path.dirname(sys.path[0]) + '/Comorbidity/Train_records_output/'):
        if xmi_train_file[-3:] == "xmi":
            xmi_file = os.path.dirname(
                sys.path[0]) + '/Comorbidity/Train_records_output/' + xmi_train_file
            print(xmi_file)
            tree = ET.parse(xmi_file)
            root = tree.getroot()
            dictionary_polarity = {}
            dictionary_cui = {}

            for child in root:
                if 'ontologyConceptArr' in child.attrib:
                    dictionary_polarity.update(dict.fromkeys(child.attrib.get(
                        'ontologyConceptArr').split(), "n" if child.attrib.get('polarity') == "-1" else "y"))

            for child in root:
                if 'cui' in child.attrib:
                    dictionary_cui.update(dict.fromkeys(child.attrib.get("cui").split(
                    ), dictionary_polarity.get(child.attrib.get("{http://www.omg.org/XMI}id"))))

            output_string = ""

            for key in dictionary_cui:
                output_string = output_string + \
                    ("n" if dictionary_cui[key] ==
                     "n" else "") + str(key) + " "

            filepath = os.path.dirname(
                sys.path[0]) + '/Comorbidity/Cuis/Train1+2/' + xmi_train_file[:len(xmi_train_file) - 4]
            with open(filepath, 'w') as f:
                f.write(output_string)
