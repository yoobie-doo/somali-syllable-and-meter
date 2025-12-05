# SomSyll

[![DOI](https://zenodo.org/badge/655122226.svg)](https://doi.org/10.5281/zenodo.17393480)


## About
This project intends to aid in the computational analysis of Somali poetry and includes two main features:
- rule based syllabification 
- metrical scansion 
 
The scope of this project is also restricted to standard, Af Maxaa dialect, Somali.

## How to Use
Upto three command line arguments can be supplied for syll.py.


If one or two files are supplied, then the first will always be taken as the input file,

And the second will be taken as a combined syllable and meter output file.
```
python3 syll.py input.txt
```
```
python3 syll.py input.txt output.txt
```
If, and only if, three files are supplied,

The first isupdated readme to reflect new io output options taken as the input,

The second is taken as the syllabification output file,

And the third is taken as the metrical scansion output file.
```
python3 syll.py input.txt syllable.txt meter.txt
```
If no command line arguments are given the following prompt is shown.

```
python3 syll.py 
Enter one line:
```
The program will then return the syllabified line along with it's meter.

## Outputs
For one line (no supplied files):
```
Enter one line: Waqtiyada socdaalka ah

['waq', 'ti', 'ya', 'da', 'soc', 'daal', 'ka', 'ah']
[1, 1, 1, 1, 1, 2, 1, 1]
```

For one output file (1 input, and 1 optional output file):
```
wakh ti ya da sod caal ka ah   1 1 1 1 1 2 1 1
a yaa ma ha sil si lad da ah   1 2 1 1 1 1 1 1 1
xil li ya da bal suu ree   1 1 1 1 1 2 2
soo ji re had daad ta hay   2 1 1 1 2 1 ?
```
For syllable and meter output files (1 input and 2 mandatory output files):
```
wakh ti ya da sod caal ka ah   
a yaa ma ha sil si lad da ah   
xil li ya da bal suu ree   
soo ji re had daad ta hay   
```
```
1 1 1 1 1 2 1 1
1 2 1 1 1 1 1 1 1
1 1 1 1 1 2 2
2 1 1 1 2 1 ?
```

## Probablistic Diphthong Scanning

```
Enter one line: soomaali baan ahay

['soo', 'maa', 'li', 'baan', 'a', 'hay']
[2, 2, 1, 2, 1, '1']
```
Previously diphthongs were scanned as '?', now through an assessment of diphthong frequencies for jiifto poetry diphthongs are corrected by assessing the maximum likelihood that the given line of poetry fits known jiifto templates. Other genres of poetry will be assessed at a later date.

## Accuracy:
On a corpus of **11609** lines of Jiifto poetry:

This program was able to **accurately syllabify 99.991%** of lines, with just 1 line failing due to consonant clusters in loan a word.

This program was also able to **accurately scan 93.325%** of lines, with 5126 diphthongs marked as ?.
_no longer accurate, new results to be computed_

## Notes
the project is still under development, but we wanted to make the algorithm accessible as early as possible.

## Authors
Idiris Cali — Lead Linguist

Ayub Nur    — Lead Programmer


## Cite This Project
```
@software{nur_somali_poetry_parser_2025,
  author       = {Ayub Nur and Idiris Cali},
  title        = {SomSyll: A Rule-Based Approach to Somali Metre and Alliteration},
  year         = {2025},
  version      = {v0.0.1-alpha},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17393480},
  url          = {https://doi.org/10.5281/zenodo.17393480}
}
```
