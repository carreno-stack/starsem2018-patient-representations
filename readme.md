# Learning Patient Representations from Text

This repository is the official implementation of [Learning Patient Representations from Text](https://arxiv.org/abs/1805.02096).

[Original paper's repository](https://github.com/dmitriydligach/starsem2018-patient-representations).

## Requirements/Data Download

* Include libraries:

** Deep learning: keras, gensim, sklearn
** Others: codecs, numpy, configparser, os, nltk, pandas, sys, glob, string, collections, operator, pickle, xml

* Obtain access to [MIMIC III](https://physionet.org/content/mimiciii/1.4/) and [i2b2 Obesity Challenge](https://www.i2b2.org/NLP/Obesity/Main.php) datasets.
* Install Apache cTAKES following the instructions on [this page](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+4.0+User+Install+Guide#cTAKES4.0UserInstallGuide-InstallcTAKES).
* Create [UMLS](https://uts.nlm.nih.gov/uts/signup-login?_gl=1*1tk5kri*_ga*ODQ0MDU0MjY1LjE2NDYzNjEyNDE.*_ga_7147EPK006*MTY1MTExNzYwNC4yLjEuMTY1MTExNzYwOC4w*_ga_P1FPTH9PL4*MTY1MTExNzYwNC4yLjEuMTY1MTExNzYwOC4w) account and obtain your userdid and key for running cTAKES.

## Preprocessing

1. Extract CUIs from MIMIC III patient data:

* Create MIMIC_INPUT_DIRECTORY and MIMIC_OUTPUT_DIRECTORY.
* Exctract notes for each patient in the MIMIC III NOTEVENTS.csv file and save each patient notes in the individual txt files: run `notes_prep.py`. 
Save txt files in MIMIC_INPUT_DIRECTORY.
* Run cTAKES pipeline:
```shell script
bin/runClinicalPipeline.sh  -i MIMIC_INPUT_DIRECTORY  --xmiOut MIMIC_OUTPUT_DIRECTORY --user dacarrenog --key ******
```
* Extract CUIs only (accouning for negation) from xmi files created by the cTAKES pipeline: run `notesfilegen.py`

Note: we need to account for negations in the CUIs extraction process, as some CUIs may appear in the notes with the negation, for example "Patient does not experience shortness of breath".

2. Extract CUIs from i2b2 patient data:

* Set up MIMIC_INPUT_DIRECTORY and MIMIC_OUTPUT_DIRECTORY.
* Exctract notes for each patient in the i2b2 dataset and save each patient notes in the individual txt file: run `cormodiblity_prep.py`.
Save txt files in MIMIC_INPUT_DIRECTORY.
* Run cTAKES pipeline:
```shell script
bin/runClinicalPipeline.sh  -i MIMIC_INPUT_DIRECTORY  --xmiOut MIMIC_OUTPUT_DIRECTORY --user dacarrenog --key ******
```
* Extract CUIs only (accouning for negation) from xmi files created by the cTAKES pipeline:: run `cormodibilityfilegen.py`

3. Prepare corpus for word2vec model:

* Run corpus_gen.py
It will create pickled corpus file that will be used for training word2vec model.

## Dependencies

1. Set up correct directories for MIMIC III input files per `cuis.cfg` file.
* Add MIMIC III CPTEVENTS.csv, DIAGNOSES_ICD.csv, PROCEDURES_ICD.csv files to the directory specified in `cuis.cfg`.
2. Set up correct directories for i2b2 input files per `dense.cfg`  and `sparse.cfg` files.

## Training

To train a billing code prediction model:

1. cd Codes.
2. To run the model with randomly initalized CUIs:
```shell script
ft.py cuis.cfg
```
3. To run the model with word2vec pre-trained CUIs embeddings:
```shell script
ft.py cuis_w2v.cfg
```

## Evaluation

To evaluate the model on the i2b2 data:

1. cd Comorbidity
2. To run sparse model:
```shell script
svm.py sparse.cfg
```
3. To run dense (learned) model:
```shell script
svm.py dense.cfg
```
## Pre-trained Models

Pre-trained models are uploaded to the Codes/Model directory:

* w2v.h5 - Word2Vec pretrained CUIs embeddings model.
* model.h5 - billing code prediction model.

## Results

Our model achieves the following performance on Precision, Recall and F1 scores when compared with the original paper results:

|                     Disease                 | Sparse |       |       | SVD (300   dimensions) |       |       | SVD (1000   dimensions) |       |       | Learned, random   CUIs |       |       | Learned,   word2vec initialized |       |          |
|:-------------------------------------------:|:------:|:-----:|:-----:|:----------------------:|:-----:|:-----:|:-----------------------:|:-----:|:-----:|:----------------------:|:-----:|:-----:|:-------------------------------:|:-----:|:--------:|
|                                             | P      | R     | F1    | P                      | R     | F1    | P                       | R     | F1    | P                      | R     | F1    | P                               | R     | F1       |
| Avg (reproduced)                            | 0.767  | 0.642 | 0.665 | 0.727                  | 0.631 | 0.651 | 0.767                   | 0.642 | 0.665 | 0.666                  | 0.692 | 0.67  | 0.692                           | 0.708 | 0.696    |
| Avg (paper)                                 | 0.733  | 0.65  | 0.675 | 0.685                  | 0.672 | 0.674 | 0.685                   | 0.672 | 0.674 | 0.709                  | 0.725 | 0.715 | 0.709                           | 0.725 | 0.715    |
| Abs   % Difference (paper vs reproduction)* | 4.64%  | 1.23% | 1.48% | 6.13%                  | 6.10% | 3.41% | 11.97%                  | 4.46% | 1.34% | 6.06%                  | 4.55% | 6.29% | 2.40%                           | 2.34% | 2.66%    |

## Contributing

Please contribute to the [original repository](https://github.com/dmitriydligach/starsem2018-patient-representations).
