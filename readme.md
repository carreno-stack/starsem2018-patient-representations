### Implementation of the Code for Dligach and Miller, 2018 *SEM paper *Learning Patient Representations from Text*

Pre-requisites for running the experiment:

* Obtain access to MIMIC III and i2b2 Obesity Challenge datasets.
* Install Apache cTAKES following [this link](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+4.0+User+Install+Guide#cTAKES4.0UserInstallGuide-InstallcTAKES).
* Create UMLS account and obtain your usedid and key.

To train a billing code prediction model:

1. Extract CUIs from MIMIC III patient data:

* Exctract notes for each patient of the MIMIC III NOTEVENTS.csv and save in individual txt file: run `notes_prep.py`
* Set up MIMIC_INPUT_DIRECTORY and MIMIC_OUTPUT_DIRECTORY.
* Run cTAKES pipeline:
```shell script
bin/runClinicalPipeline.sh  -i MIMIC_INPUT_DIRECTORY  --xmiOut MIMIC_OUTPUT_DIRECTORY --user dacarrenog --key ******
```
* Extract CUIs from xmi files created by the pipeline: run `notesfilegen.py`
2. Set up correct directories as per `cuis.cfg` file.
* Add MIMIC III CPTEVENTS.csv, DIAGNOSES_ICD.csv, PROCEDURES_ICD.csv files to the directory specified in `cuis.cfg`.
3. cd Codes.
4. 
```shell script
ft.py cuis.cfg
```

To run the experiments with i2b2 data:

1. Extract CUIs from i2b2 patient data:

* Exctract notes for each patient of the i2b2 dataset and save in individual txt file: run `cormodiblity_prep.py`
* Set up MIMIC_INPUT_DIRECTORY and MIMIC_OUTPUT_DIRECTORY.
* Run cTAKES pipeline:
```shell script
bin/runClinicalPipeline.sh  -i MIMIC_INPUT_DIRECTORY  --xmiOut MIMIC_OUTPUT_DIRECTORY --user dacarrenog --key ******
```
* Extract CUIs from xmi files created by the pipeline: run `cormodibilityfilegen.py`
2. Set up correct directories as per `dense.cfg`  and `sparse.cfg` files.
3. cd Comorbidity
4. 
```shell script
svm.py sparse.cfg
```
5. 
```shell script
svm.py dense.cfg
```

For the experiments described in the paper, we used NumPy 1.13.0, scikit-learn 0.19.1, and Keras 2.0.4 with Theano 0.9.0 backend. Titan X GPU we used for training neural network models was provided by NVIDIA.