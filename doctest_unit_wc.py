'''
>>> import subprocess

########### Test Suite for normal file execution without flags ################# 
# Test case for the first input file
>>> subprocess.check_output('python3 wc.py testinputs/test_1.txt', shell=True)
b'\\t 4\\t 21\\t 355\\t testinputs/test_1.txt\\n'

# Test case for the second input file that is empty
>>> subprocess.check_output('python3 wc.py testinputs/test_2.txt', shell=True)
b'\\t 0\\t 0\\t 0\\t testinputs/test_2.txt\\n'

# Test case for the third input file
>>> subprocess.check_output('python3 wc.py testinputs/test_3.txt', shell=True)
b'\\t 1\\t 8\\t 43\\t testinputs/test_3.txt\\n'

# Test Case for input file passed with options/flags
>>> subprocess.check_output('python3 wc.py -c testinputs/test_1.txt', shell=True)
b'\\t 355\\t testinputs/test_1.txt\\n'

############### Test Suite for option flags ###############
# Testcase for word flag
>>> subprocess.check_output('python3 wc.py -w testinputs/test_1.txt', shell=True)
b'\\t 21\\t testinputs/test_1.txt\\n'

# Test Cases for byte flag
>>> subprocess.check_output('python3 wc.py -c testinputs/test_1.txt', shell=True)
b'\\t 355\\t testinputs/test_1.txt\\n'

# Test Cases for line flag
>>> subprocess.check_output('python3 wc.py -l testinputs/test_1.txt', shell=True)
b'\\t 4\\t testinputs/test_1.txt\\n'

# Test Cases for line and word flag
>>> subprocess.check_output('python3 wc.py -l -w testinputs/test_1.txt', shell=True)
b'\\t 4\\t 21\\t testinputs/test_1.txt\\n'

# Test Cases for line and character flag
>>> subprocess.check_output('python3 wc.py -l -c testinputs/test_1.txt', shell=True)
b'\\t 4\\t 355\\t testinputs/test_1.txt\\n'

# Test Cases for word and character flag
>>> subprocess.check_output('python3 wc.py -w -c testinputs/test_1.txt', shell=True)
b'\\t 21\\t 355\\t testinputs/test_1.txt\\n'


# Test Cases for word, character and line flag
>>> subprocess.check_output('python3 wc.py -w -c -l testinputs/test_1.txt', shell=True)
b'\\t 4\\t 21\\t 355\\t testinputs/test_1.txt\\n'

>>> subprocess.check_output('python3 wc.py - testinputs/test_1.txt', shell=True)
b"we don't handle that situation yet!\\n\\t 4\\t 21\\t 355\\t testinputs/test_1.txt\\n\\t 4\\t 21\\t 355\\t total\\n"

>>> subprocess.check_output('python3 wc.py -', shell=True)
b"we don't handle that situation yet!\\n"

>>> subprocess.check_output('python3 wc.py', shell=True)
b"we don't handle that situation yet!\\n"

################ Test Suite for multiple files with no flags #################
>>> subprocess.check_output('python3 wc.py testinputs/test_1.txt testinputs/test_3.txt', shell=True)
b'\\t 4\\t 21\\t 355\\t testinputs/test_1.txt\\n\\t 1\\t 8\\t 43\\t testinputs/test_3.txt\\n\\t 5\\t 29\\t 398\\t total\\n'

################ Test Suite for multiple files with single flags #################
# Test with single flag and multiple files
>>> subprocess.check_output('python3 wc.py -l testinputs/test_1.txt testinputs/test_3.txt', shell=True)
b'\\t 4\\t testinputs/test_1.txt\\n\\t 1\\t testinputs/test_3.txt\\n\\t 5\\t total\\n'

############### Test with multiple flag and multiple files ################
>>> subprocess.check_output('python3 wc.py -l -w testinputs/test_1.txt testinputs/test_3.txt', shell=True)
b'\\t 4\\t 21\\t testinputs/test_1.txt\\n\\t 1\\t 8\\t testinputs/test_3.txt\\n\\t 5\\t 29\\t total\\n'

>>> subprocess.check_output('python3 wc.py -l -w -c testinputs/test_1.txt testinputs/test_3.txt', shell=True)
b'\\t 4\\t 21\\t 355\\t testinputs/test_1.txt\\n\\t 1\\t 8\\t 43\\t testinputs/test_3.txt\\n\\t 5\\t 29\\t 398\\t total\\n'

############### Test with multiple flag and single files ################
>>> subprocess.check_output('python3 wc.py -l -w -c testinputs/test_1.txt', shell=True)
b'\\t 4\\t 21\\t 355\\t testinputs/test_1.txt\\n'

>>> subprocess.check_output('python3 wc.py -l -w testinputs/test_1.txt', shell=True)
b'\\t 4\\t 21\\t testinputs/test_1.txt\\n'

>>> subprocess.check_output('python3 wc.py -l testinputs/test_1.txt', shell=True)
b'\\t 4\\t testinputs/test_1.txt\\n'

########### Testcase against multiple files including binary files ###########3
>>> subprocess.check_output('python3 wc.py testinputs/test_1.txt testinputs/Bob_dylan.jpeg', shell=True)
b'\\t 4\\t 21\\t 355\\t testinputs/test_1.txt\\n\\t 343\\t 2728\\t 60813 \\t testinputs/Bob_dylan.jpeg\\n\\t 348\\t 2749\\t 61168\\t total\\n'
'''


