# WordCount
Unix wc clone written in python - The program takes a file as an input and returns number of lines, words and bytes of the file passed. the program can also read multiple files passed together


## Download Program

To use the program, firt clone the project using below shown code:

`git clone https://github.com/akamanzi/WordCount.git`

## How to run the program

Navigate to the project root directory `cd WordCount`. In order to run the program, use the command below:

`Python3 wc.py path_to_file_name`

You could also run the program using any of the sample files located in the `testinputs` directory as indicated belwo:

`Python3 wc.py testinputs/test_1.txt`

## Using Flags
just like Unix's wc, this program accepts options:

`-L, -l`: for displaying number of lines in a passed file

##### Usage: `Python3 wc.py -L file_name`

`-w`: displays number of words in a given file

##### Usage: `Python3 wc.py -w file_name`

`-c`: displays number of bytes of a given file

##### Usage: `Python3 wc.py -c file_name`

`-L`: displays length of the longest line in a given file

##### Usage: `Python3 wc.py -L file_name`

`--help`: help for how the program is used

##### Usage: `Python3  wc.py --help`

`--version`: displays version wc program

##### Usage: `Python3  wc.py --version`

`--files0-from`: read input from NUL terminated files

##### Usage: `Python3  wc.py --files0-from file_name`

`-`: reads from standard input

##### Usage: `Python3  wc.py`



## Runnning Test

This program uses `unittest` testing framework. in order to run tests use the `-m` flag to specify `unittest` framework as below:

`Python3 -m unittest unittest_wc.py`

Additionally you could also run the doctests by running the following command:

`Python3 doctest_unit_wc.py`

#### NOTE: all the commands above should be run in the root directory. Test files used are located in the `testinputs` directory.

## Python Versions

- Compatible with python 3.3 and above 

## Known Issues:

- The program does not return accurate values of bytes and words when passed with binary files.

