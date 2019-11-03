import unittest
import subprocess
from unittest.mock import patch
import wc


def cmd_command(flags, test_inputs):
    return subprocess.check_output('python3 wc.py %s %s' % (flags, " ".join(test_inputs)), shell=True)


class SingleFileTestCases(unittest.TestCase):

    def test_single_file_textfile1(self):
        command = subprocess.check_output('python3 wc.py testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t 21\t 355\t testinputs/test_1.txt\n'
        self.assertEqual(command, expected_output)

    def test_single_textfile2(self):
        command = subprocess.check_output('python3 wc.py testinputs/test_2.txt', shell=True)
        expected_output = b'\t 0\t 0\t 0\t testinputs/test_2.txt\n'
        self.assertEqual(command, expected_output)

    def test_single_textfile3(self):
        command = subprocess.check_output('python3 wc.py testinputs/test_3.txt', shell=True)
        expected_output = b'\t 1\t 8\t 43\t testinputs/test_3.txt\n'
        return self.assertEqual(command, expected_output)

    def test_python_file(self):
        command = subprocess.check_output('python3 wc.py testinputs/test_1.py', shell=True)
        expected_output = b'\t 6\t 28\t 492\t testinputs/test_1.py\n'
        return self.assertEqual(command, expected_output)



class SingleFileMultipleFlagsTestCases(unittest.TestCase):

    def test_single_file_with_word_flag(self):
        command = subprocess.check_output('python3 wc.py -w testinputs/test_1.txt', shell=True)
        expected_output = b'\t 21\t testinputs/test_1.txt\n'
        return self.assertEqual(command, expected_output)

    def test_single_file_with_line_flag(self):
        command = subprocess.check_output('python3 wc.py -l testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t testinputs/test_1.txt\n'
        self.assertEqual(command, expected_output)

    def test_single_file_with_byte_flag(self):
        command = subprocess.check_output('python3 wc.py -c testinputs/test_1.txt', shell=True)
        expected_output = b'\t 355\t testinputs/test_1.txt\n'
        return self.assertEqual(command,expected_output)

    def test_single_file_with_max_line_length_flag(self):
        command = subprocess.check_output('python3 wc.py -L testinputs/test_1.txt', shell=True)
        expected_output = b'\t 74\t testinputs/test_1.txt\n'
        return self.assertEqual(command,expected_output)

    def test_single_file_with_line_bytes_flags(self):
        command = subprocess.check_output('python3 wc.py -l -c testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t 355\t testinputs/test_1.txt\n'
        return self.assertEqual(command, expected_output)

    def test_single_file_with_word_bytes_flags(self):
        command = subprocess.check_output('python3 wc.py -w -c testinputs/test_1.txt', shell=True)
        expected_output = b'\t 21\t 355\t testinputs/test_1.txt\n'
        return self.assertEqual(command, expected_output)

    def test_single_file_with_word_line_byte_flags(self):
        command = subprocess.check_output('python3 wc.py -w -c -l testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t 21\t 355\t testinputs/test_1.txt\n'
        return self.assertEqual(command, expected_output)

    def test_single_file_with_combined_line_word_flags(self):
        command = subprocess.check_output('python3 wc.py -wl testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t 21\t testinputs/test_1.txt\n'
        return self.assertEqual(command, expected_output)

    def test_single_file_with_combined_word_byte_flags(self):
        command = subprocess.check_output('python3 wc.py -wc testinputs/test_1.txt', shell=True)
        expected_output = b'\t 21\t 355\t testinputs/test_1.txt\n'
        return self.assertEqual(command, expected_output)

    def test_single_file_with_combined_line_byte_flags(self):
        command = subprocess.check_output('python3 wc.py -lc testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t 355\t testinputs/test_1.txt\n'
        return self.assertEqual(command, expected_output)

    def test_single_file_with_combined_line_byte_word_flags(self):
        command = subprocess.check_output('python3 wc.py -lcw testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t 21\t 355\t testinputs/test_1.txt\n'
        return self.assertEqual(command, expected_output)

    def test_single_file_with_combined_maxline_word_byte_line_flag(self):
        command = subprocess.check_output('python3 wc.py -lcwL testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t 21\t 355\t 74\t testinputs/test_1.txt\n'
        return self.assertEqual(command,expected_output)

    def test_single_file_with_combined_maxline_line_flag(self):
        command = subprocess.check_output('python3 wc.py -lL testinputs/test_1.txt', shell=True)
        expected_output = b'\t 4\t 74\t testinputs/test_1.txt\n'
        return self.assertEqual(command,expected_output)

    def test_single_file_with_combined_maxline_byte_flag(self):
        command = subprocess.check_output('python3 wc.py -Lc testinputs/test_1.txt', shell=True)
        expected_output = b'\t 355\t 74\t testinputs/test_1.txt\n'
        return self.assertEqual(command,expected_output)

    def test_single_file_with_combined_maxline_maxline_flag(self):
        command = subprocess.check_output('python3 wc.py -LL testinputs/test_1.txt', shell=True)
        expected_output = b'\t 74\t testinputs/test_1.txt\n'
        return self.assertEqual(command,expected_output)

    def test_single_file_with_combined_maxline_word_flag(self):
        command = subprocess.check_output('python3 wc.py -Lw testinputs/test_1.txt', shell=True)
        expected_output = b'\t 21\t 74\t testinputs/test_1.txt\n'
        return self.assertEqual(command,expected_output)






class MissingArgumentsTestCases(unittest.TestCase):

    def test_empty_flag(self):
        command = subprocess.check_output('python3 wc.py - testinputs/test_1.txt', shell=True)
        expected_output = b"we don't handle that situation yet!\n\t 4\t 21\t 355\t testinputs/test_1.txt\n\t 4\t 21\t 355\t total\n"
        return self.assertEqual(command, expected_output)

    def test_missing_flag(self):
        command = subprocess.check_output('python3 wc.py -', shell=True)
        expected_output = b"we don't handle that situation yet!\n"
        return self.assertEqual(command, expected_output)

class MultipleFilesNoFlagsTestCases(unittest.TestCase):

    def test_multiple_files_without_flag(self):
        command = subprocess.check_output('python3 wc.py testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t 21\t 355\t testinputs/test_1.txt\n\t 1\t 8\t 43\t testinputs/test_3.txt\n\t 5\t 29\t 398\t total\n'
        return self.assertEqual(command, expected_output)

class MultipleFilesWithFlagsTestCases(unittest.TestCase):

    def test_multiple_files_with_line_flag(self):
        command = subprocess.check_output('python3 wc.py -l testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t testinputs/test_1.txt\n\t 1\t testinputs/test_3.txt\n\t 5\t total\n'
        return self.assertEqual(command, expected_output)

    def test_multiple_files_with_line_word_flag(self):
        command = subprocess.check_output('python3 wc.py -l -w testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t 21\t testinputs/test_1.txt\n\t 1\t 8\t testinputs/test_3.txt\n\t 5\t 29\t total\n'
        return self.assertEqual(command, expected_output)

    def test_multiple_files_with_combined_line_word_flag(self):
        command = subprocess.check_output('python3 wc.py -lw testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t 21\t testinputs/test_1.txt\n\t 1\t 8\t testinputs/test_3.txt\n\t 5\t 29\t total\n'
        return self.assertEqual(command, expected_output)

    def test_multiple_files_with_combined_line_byte_flag(self):
        command = subprocess.check_output('python3 wc.py -lc testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t 355\t testinputs/test_1.txt\n\t 1\t 43\t testinputs/test_3.txt\n\t 5\t 398\t total\n'
        return self.assertEqual(command, expected_output)

    def test_multiple_files_with_line_word_byte_flag(self):
        command = subprocess.check_output('python3 wc.py -l -w -c testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t 21\t 355\t testinputs/test_1.txt\n\t 1\t 8\t 43\t testinputs/test_3.txt\n\t 5\t 29\t 398\t total\n'
        return self.assertEqual(command, expected_output)

    def test_multiple_files_with_combined_line_word_byte_flag(self):
        command = subprocess.check_output('python3 wc.py -lwc testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t 21\t 355\t testinputs/test_1.txt\n\t 1\t 8\t 43\t testinputs/test_3.txt\n\t 5\t 29\t 398\t total\n'
        return self.assertEqual(command, expected_output)

    @unittest.expectedFailure
    def test_help_flag(self):
        command = subprocess.check_output('python3 wc.py --help', shell=True)
        expected_output = b'\t 4\t 21\t 355\t testinputs/test_1.txt\n\t 1\t 8\t 43\t testinputs/test_3.txt\n\t 5\t 29\t 398\t total\n'
        return self.assertEqual(command,expected_output)

    def test_version_flag(self):
        command = subprocess.check_output('python3 wc.py --version', shell=True)
        expected_output = b'wc.py 1.0\n'
        return self.assertEqual(command,expected_output)

    def test_multiple_files_with_combined_maxline_word_byte_line_flag(self):
        command = subprocess.check_output('python3 wc.py -lcwL testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t 21\t 355\t 74\t testinputs/test_1.txt\n\t 1\t 8\t 43\t 42\t testinputs/test_3.txt\n\t 5\t 29\t 398\t 42\t total\n'
        return self.assertEqual(command,expected_output)

    def test_multiple_files_with_combined_maxline_line_flag(self):
        command = subprocess.check_output('python3 wc.py -lL testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 4\t 74\t testinputs/test_1.txt\n\t 1\t 42\t testinputs/test_3.txt\n\t 5\t 42\t total\n'
        return self.assertEqual(command,expected_output)

    def test_multiple_files_with_combined_maxline_word_flag(self):
        command = subprocess.check_output('python3 wc.py -Lw testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 21\t 74\t testinputs/test_1.txt\n\t 8\t 42\t testinputs/test_3.txt\n\t 29\t 42\t total\n'
        return self.assertEqual(command,expected_output)

    def test_multiple_files_with_combined_maxline_byte_flag(self):
        command = subprocess.check_output('python3 wc.py -Lc testinputs/test_1.txt testinputs/test_3.txt', shell=True)
        expected_output = b'\t 355\t 74\t testinputs/test_1.txt\n\t 43\t 42\t testinputs/test_3.txt\n\t 398\t 42\t total\n'
        return self.assertEqual(command,expected_output)





class BinaryFilesTestCases(unittest.TestCase):
    @unittest.expectedFailure
    def test_binary_file_with_text_file(self):
        command = subprocess.check_output('python3 wc.py testinputs/test_1.txt testinputs/Bob_dylan.jpeg', shell=True)
        expected_output = b'\t 4\t 21\t 355\t testinputs/test_1.txt\n\t 343\t 2728\t 60813 \t testinputs/Bob_dylan.jpeg\n\t 348\t 2749\t 61168\t total\n'
        return self.assertEqual(command,expected_output)

    @unittest.expectedFailure
    def test_binary_file(self):
        command = subprocess.check_output('python3 wc.py testinputs/Bob_dylan.jpeg', shell=True)
        expected_output = b'\t 343\t 2728\t 60813 \t testinputs/Bob_dylan.jpeg\n'
        return self.assertEqual(command, expected_output)

class UnicodeTestCases(unittest.TestCase):

    def test_georgian_text(self):
        command = subprocess.check_output('python3 wc.py testinputs/georgian.txt', shell=True)
        expected_output = b'\t 7\t 44\t 1115\t testinputs/georgian.txt\n'
        return self.assertEqual(command, expected_output)

    def test_ethiopian_text(self):
        command = subprocess.check_output('python3 wc.py testinputs/ethiopian.txt', shell=True)
        expected_output = b'\t 18\t 83\t 1077\t testinputs/ethiopian.txt\n'
        return self.assertEqual(command, expected_output)

    def test_drawing_text(self):
        command = subprocess.check_output('python3 wc.py testinputs/drawing_file.txt', shell=True)
        expected_output = b'\t 7\t 101\t 1249\t testinputs/drawing_file.txt\n'
        return self.assertEqual(command, expected_output)

    def test_file_without_extension(self):
        command = subprocess.check_output('python3 wc.py testinputs/no_extension', shell=True)
        expected_output = b'\t 8\t 54\t 718\t testinputs/no_extension\n'
        return self.assertEqual(command, expected_output)

    def test_unicode_dot_py(self):
        command = subprocess.check_output('python3 wc.py testinputs/test_unicode.py', shell=True)
        expected_output = b'\t 4\t 26\t 654\t testinputs/test_unicode.py\n'
        return self.assertEqual(command, expected_output)

class SdtInTestCases(unittest.TestCase):

    @patch('builtins.input', return_value="Hi Arnold")
    def test_one_line_stdin(self, input):
        command = subprocess.check_output('python3 wc.py', shell=True)
        expected_output = b'\t 0 \t 2 \t 9\n'
        return self.assertEqual(command, expected_output)

class CharacterFlagCombinationSingleFileTestCases(unittest.TestCase):

        test_inputs = ['testinputs/test_3.txt']
        def test_char_lines_combination(self):
            output = b'\t 1\t 43\t testinputs/test_3.txt\n'
            return self.assertEqual(cmd_command("-ml", self.test_inputs), output)

        def test_char_byte_combination(self):
            output = b'\t 43\t 43\t testinputs/test_3.txt\n'
            return self.assertEqual(cmd_command("-mc", self.test_inputs), output)

        def test_char_word_combination(self):
            output = b'\t 8\t 43\t testinputs/test_3.txt\n'
            return self.assertEqual(cmd_command("-mw", self.test_inputs), output)

        def test_char_char_combination(self):
            output = b'\t 43\t testinputs/test_3.txt\n'
            return self.assertEqual(cmd_command("-mm", self.test_inputs), output)

        def test_char_line_byte_combination(self):
            output = b'\t 1\t 43\t 43\t testinputs/test_3.txt\n'
            return self.assertEqual(cmd_command("-mlc", self.test_inputs), output)

        def test_char_line_word_combination(self):
            output = b'\t 1\t 8\t 43\t testinputs/test_3.txt\n'
            return self.assertEqual(cmd_command("-mlw", self.test_inputs), output)

        def test_char_line_word_combination(self):
            output = b'\t 1\t 43\t 42\t testinputs/test_3.txt\n'
            return self.assertEqual(cmd_command("-mlL", self.test_inputs), output)

        def test_char_line_word_byte_combination(self):
            output = b'\t 1\t 8\t 43\t 43\t 42\t testinputs/test_3.txt\n'
            return self.assertEqual(cmd_command("-mlLcw", self.test_inputs), output)


class CharacterFlagCombinationMultipleFilesTestCases(unittest.TestCase):

    test_inputs = ['testinputs/test_3.txt', 'testinputs/test_1.txt']
    def test_char_lines_combination(self):
        output = b'\t 1\t 43\t testinputs/test_3.txt\n\t 4\t 355\t ' \
                 b'testinputs/test_1.txt\n\t 5\t 398\t total\n'
        return self.assertEqual(cmd_command("-ml", self.test_inputs), output)

    def test_char_byte_combination(self):
        output = b'\t 43\t 43\t testinputs/test_3.txt\n\t 355\t 355\t ' \
                 b'testinputs/test_1.txt\n\t 398\t 398\t total\n'
        return self.assertEqual(cmd_command("-mc", self.test_inputs), output)

    def test_char_word_combination(self):
        output = b'\t 8\t 43\t testinputs/test_3.txt\n\t 21\t 355\t ' \
                 b'testinputs/test_1.txt\n\t 29\t 398\t total\n'
        return self.assertEqual(cmd_command("-mw", self.test_inputs), output)

    def test_char_char_combination(self):
        output = b'\t 43\t testinputs/test_3.txt\n\t 355\t ' \
                 b'testinputs/test_1.txt\n\t 398\t total\n'
        return self.assertEqual(cmd_command("-mm", self.test_inputs), output)

    def test_char_line_byte_combination(self):
        output = b'\t 1\t 43\t 43\t testinputs/test_3.txt\n\t 4\t 355\t 355\t ' \
                 b'testinputs/test_1.txt\n\t 5\t 398\t 398\t total\n'
        return self.assertEqual(cmd_command("-mlc", self.test_inputs), output)

    def test_char_line_word_combination(self):
        output = b'\t 1\t 8\t 43\t testinputs/test_3.txt\n\t 4\t 21\t 355\t ' \
                 b'testinputs/test_1.txt\n\t 5\t 29\t 398\t total\n'
        return self.assertEqual(cmd_command("-mlw", self.test_inputs), output)

    def test_char_line_word_combination(self):
        output = b'\t 1\t 43\t 42\t testinputs/test_3.txt\n\t 4\t 355\t 74\t ' \
                 b'testinputs/test_1.txt\n\t 5\t 398\t 74\t total\n'
        return self.assertEqual(cmd_command("-mlL", self.test_inputs), output)

    def test_char_line_word_byte_combination(self):
        output = b'\t 1\t 8\t 43\t 43\t 42\t ' \
                 b'testinputs/test_3.txt\n\t 4\t 21\t 355\t 355\t 74\t testinputs/test_1.txt\n\t 5\t 29\t 398\t 398\t 74\t total\n'
        return self.assertEqual(cmd_command("-mlLcw", self.test_inputs), output)

class Files0FromTestCases(unittest.TestCase):
    testinput = ['files0-from.txt']
    def test_files0from(self):
        output = b"\t 344\t 1490\t 60813\t testinputs/Bob_dylan.jpeg\n\t 7\t 101\t 1249\t " \
             b"testinputs/drawing_file.txt\n\t 19\t 83\t 1077\t testinputs/ethiopian.txt\n\t 199\t 993\t 13245\t " \
             b"testinputs/file_1.txt\n\t 7\t 44\t 1115\t testinputs/georgian.txt\n\t 1\t 1\t 2\t " \
             b"testinputs/new_line.txt\n\t 8\t 54\t 718\t testinputs/no_extension\n\t 7\t 28\t 492\t t" \
             b"estinputs/test_1.py\n\t 5\t 21\t 355\t testinputs/test_1.txt\n\t 1\t 0\t 0\t " \
             b"testinputs/test_2.txt\n\t 2\t 8\t 43\t testinputs/test_3.txt\n\t 5\t 26\t 654\t " \
             b"testinputs/test_unicode.py\nwe don't handle that situation yet!\n\t 605\t 2849\t 79763\t total\n"

        return self.assertEqual(cmd_command("--files0-from", self.testinput), output)

if __name__ == '__main__':
    unittest.main()




