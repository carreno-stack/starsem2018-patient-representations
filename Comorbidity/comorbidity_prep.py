import xml.etree.ElementTree as ET
import sys
import os
sys.dont_write_bytecode = True


if __name__ == "__main__":
    
    #test files
    xml_test_file = os.path.dirname(
        sys.path[0]) + '/Comorbidity/Xml/obesity_patient_records_test.xml'
    tree = ET.parse(xml_test_file)
    for doc in tree.iter('doc'):
        doc_id = doc.attrib.get('id')
        notes_text = ""
        for text in doc:
            notes_text += text.text
        filepath = os.path.dirname(sys.path[0]) + '/Comorbidity/Test_records_txt/' + doc_id + '.txt'
        with open(filepath, 'w') as f:
            f.write(notes_text)
            
    #train files - 1
    xml_train_file = os.path.dirname(
        sys.path[0]) + '/Comorbidity/Xml/obesity_patient_records_training.xml'
    tree = ET.parse(xml_train_file)
    for doc in tree.iter('doc'):
        doc_id = doc.attrib.get('id')
        notes_text = ""
        for text in doc:
            notes_text += text.text
        filepath = os.path.dirname(
            sys.path[0]) + '/Comorbidity/Train_records_txt/' + doc_id + '.txt'
        with open(filepath, 'w') as f:
            f.write(notes_text)
    
    #train files - 2
    xml_train_file = os.path.dirname(
        sys.path[0]) + '/Comorbidity/Xml/obesity_patient_records_training2.xml'
    tree = ET.parse(xml_train_file)
    for doc in tree.iter('doc'):
        doc_id = doc.attrib.get('id')
        notes_text = ""
        for text in doc:
            notes_text += text.text
        filepath = os.path.dirname(
            sys.path[0]) + '/Comorbidity/Train_records_txt/' + doc_id + '.txt'
        with open(filepath, 'w') as f:
            f.write(notes_text)
    
