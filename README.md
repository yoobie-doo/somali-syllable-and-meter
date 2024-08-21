# About
This project intends to aid in the computational analysis of Somali poetry and includes two main features:
- rule based syllabification 
- metrical scansion 
 
The scope of this project is also restricted to standard, Af Maxaa dialect, Somali.

# How to Use
upto two command line arguments can be supplied for syll.py
```
python3 syll.py input.txt output.txt
```
If no command line arguments are given the following prompt is shown

```
Enter one line:
```
The program will then return the syllabified line along with it's meter 

# Outputs
For one line:
```
Enter one line: Waqtiyada socdaalka ah

['waq', 'ti', 'ya', 'da', 'soc', 'daal', 'ka', 'ah']
[1, 1, 1, 1, 1, 2, 1, 1]
```

For an output file:

```
wakh ti ya da sod caal ka ah   1 1 1 1 1 2 1 1
a yaa ma ha sil si lad da ah   1 2 1 1 1 1 1 1 1
xil li ya da bal suu ree   1 1 1 1 1 2 2
soo ji re had daad ta hay   2 1 1 1 2 1 ?
```

# Diphthong Scanning
the program currently cannot scan diphthongs, as they can vary in length. The currect bandaid patch solution is to mark syllables containing a diphthong as follows:

```
Enter one line: soomaali baan ahay

['soo', 'maa', 'li', 'baan', 'a', 'hay']
[2, 2, 1, 2, 1, '?']

known length:       8
unknown syllables:  1
```
~**known length:** is the summed length of the long and short syllables.~

~**unknown syllables:** notes the number of syllables that were unable to be determined as long or short~

_these features have temporarily been disabled_

# Notes
the project is still under development, but we wanted to make the algorithm accessible as early as possible.

# Authors
Idiris Cali — Lead Linguist

Ayub Nur    — Lead Programmer
