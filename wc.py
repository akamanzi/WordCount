import sys
import argparse
script_name = sys.argv[0]
allowed_options = ['l', 'w', 'c']
line_flag = 'l'
word_flag = 'w'
byte_flag = 'c'
max_length = "L"
CHAR_FLAG = "m"
version_flag = "version"

results = []
total_words = 0
total_lines = 0
total_bytes = 0
total_line_length = 0

no_flag = False
multiple_flags = False
is_file_from_flag_present = False

class Counter:

	def __init__(self, file_content):
		self.file_content = file_content

	def line_count(self):
		return len(self.file_content.splitlines())

	def word_count(self):
		return len(self.file_content.split())

	def byte_count(self):
		return len(self.file_content)

	def count_max_line_length(self, file_name):
		try:
			with open(file_name, 'r', encoding='utf-8') as f:
				file_content = f.read()
				line = file_content.split('\n')
				large_line_len = 0
				for l in line:
					if len(l) > large_line_len:
						large_line_len = len(l)
		except UnicodeDecodeError:
			file_handler = FileHandler([], [])
			large_line_len = file_handler.open_binary_file(file_name)
		return large_line_len


class ArgumentHandler:
	def handle_arguments(self):
		# Initialise arguments
		help_message = """
		Print newline, word, and byte counts for each FILE, and a total line if
		more than one FILE is specified.  With no FILE, or when FILE is -,
		read standard input.  A word is a non-zero-length sequence of characters
		delimited by white space.\n
		The options below may be used to select which counts are printed, always in
		the following order: newline, word, character, byte, maximum line length."""

		version_message = "wc (GNU coreutils) 8.21" \
						  "Copyright (C) 2013 Free Software Foundation, Inc." \
						  "License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>." \
						  "This is free software: you are free to change and redistribute it." \
						  "There is NO WARRANTY, to the extent permitted by law"

		help_flag_message = "read input from the files specified by" \
							"NUL-terminated names in file F;" \
							"If F is - then read names from standard input"

		parser = argparse.ArgumentParser(description=help_message,
										 add_help=False)
		parser.add_argument("-l", help="output number of lines", action='store_true')
		parser.add_argument("-w", help="output number of words", action='store_true')
		parser.add_argument("-c", help="output number of bytes", action='store_true')
		parser.add_argument("--help", help="outputs help message", action='help',
							default=argparse.SUPPRESS)
		parser.add_argument("--version", help="outputs version of wc", action='version',
							version=version_message)
		parser.add_argument("-L", help="output length of the longest line", action='store_true')
		parser.add_argument("-m", help="output number of characters in file", action='store_true')
		parser.add_argument("--files0-from", action='store_true', help=help_flag_message)
		parser.add_argument("filename", nargs='+')

		if len(sys.argv) == 1:
			stdin_content = sys.stdin.read()
			handle_stdin(stdin_content)
			sys.exit()

		args = parser.parse_args()
		flag_list = []
		list_of_arguments = []
		if args.l:
			flag_list.append(line_flag)
		if args.w:
			flag_list.append(word_flag)
		if args.m:
			flag_list.append(CHAR_FLAG)
		if args.c:
			flag_list.append(byte_flag)
		if args.L:
			flag_list.append(max_length)
		if args.files0_from:
			global is_file_from_flag_present
			is_file_from_flag_present = True

		list_of_arguments.extend([args.filename, flag_list])
		return list_of_arguments


class FileHandler:
	def __init__(self, file_names, flags):
		self.file_names = file_names
		self.flags = flags

	def openfiles(self):
		global num_of_lines
		global num_of_words
		for file in self.file_names:
			num_of_lines = 0
			num_of_words = 0
			global total_words, total_lines, total_bytes, total_line_length

			try:
				with open(file, 'rb') as f:
					file_content = f.read()
					if is_file_from_flag_present:
						self.handle_null_terminated_files(file_content, self.flags)
						break
					counter = Counter(file_content)
					num_of_lines = counter.line_count()
					num_of_words = counter.word_count()
					byte_count = counter.byte_count()
					max_line_length = counter.count_max_line_length(file)

					total_words += num_of_words
					total_lines += num_of_lines

					total_bytes += byte_count
					if len(self.flags) >= 1:
						global multiple_flags
						multiple_flags = True
						if line_flag in self.flags:
							results.extend([num_of_lines])
						if word_flag in self.flags:
							results.extend([num_of_words])
						if CHAR_FLAG in self.flags:
							results.extend([byte_count])
						if byte_flag in self.flags:
							results.extend([byte_count])
						if max_length in self.flags:
							total_line_length += max_line_length
							results.extend([max_line_length])
						results.extend([file])

					else:
						global no_flag
						no_flag = True
						results.extend([num_of_lines, num_of_words, f.tell(), file])
					print_results(results)
					results.clear()
			except OSError:
				pass
				#print("we don't handle that situation yet!")
		if len(self.file_names) > 1:
			if no_flag:
				results.extend([total_lines, total_words, total_bytes, 'total'])
			if multiple_flags:
				if line_flag in self.flags:
					results.extend([total_lines])
				if word_flag in self.flags:
					results.extend([total_words])
				if CHAR_FLAG in self.flags:
					results.extend([total_bytes])
				if byte_flag in self.flags:
					results.extend([total_bytes])
				if max_length in self.flags:
					results.extend([max_line_length])
				results.extend(['total'])
			print_results(results)

	def open_binary_file(self, file_name):
		with open(file_name, 'rb') as f:
			file_content = f.read()
			line = file_content.splitlines()
			large_line_len = 0
			for l in line:
				if len(l) > large_line_len:
					large_line_len = len(l)
		return large_line_len

	def handle_null_terminated_files(self, file_content, flags):
		global is_file_from_flag_present
		if self.is_line_null_terminated(file_content):
			# check if the file has only 1 word
			if len(file_content.split(b'\n')) == 1 and len(file_content.split()) == 1 and len(file_content) > 1:
				file_path = []
				for line in file_content.split(b'\x00'):
					file_path.append(line.decode('utf-8'))
				is_file_from_flag_present = False
				self.file_names = file_path
				self.flags = flags
				self.openfiles()
				#openfile(file_path, flags)
			else:
				for line in file_content.split(b'\n'):
					print(line.decode('utf-8'))

		else:
			for line in file_content.split(b'\n'):
				print(line.decode('utf-8'))

	def is_line_null_terminated(self, file):
		if b'\x00' in file:
			return True
		else:
			return False



def print_results(results):
	for result in results:
		if result == results[-1]:
			print('\t', result)
		else:
			print('\t', result, end='')

# TODO: pass arguments
def missing_file_missing():
	print("Wc: File missing")

def handle_stdin(input):
	line_count = len(input.split('\n')) - 1
	word_count = len(input.split())
	byte_count = len(input)
	print('\t', line_count, '\t', word_count, '\t', byte_count)

# TODO: pass arguments and return list of results

if __name__ == "__main__":
	list_of_arguments = ArgumentHandler()
	parsed_arguments_list = list_of_arguments.handle_arguments()
	file_handler = FileHandler(parsed_arguments_list[0], parsed_arguments_list[1])
	file_handler.openfiles()

