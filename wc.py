import sys
import argparse
script_name = sys.argv[0]
allowed_options = ['l', 'w', 'c']
line_flag = 'l'
word_flag = 'w'
byte_flag = 'c'
max_length = "L"
version_flag = "version"

results = []
total_words = 0
total_lines = 0
total_bytes = 0
total_line_length = 0

no_flag = False
multiple_flags = False

def count_longest_line(file_name):
	large_line = ''
	large_line_len = 0
	with open(file_name, 'rb') as f:
		for line in f:
			if len(line) > large_line_len:
				large_line_len = len(line)
				large_line = line
	return large_line_len

def openfile(file_names, argument):
	global num_of_lines
	global num_of_words

	for file in file_names:
		num_of_lines = 0
		num_of_words = 0
		global total_words, total_lines, total_bytes, total_line_length

		try:
			with open(file, 'rb') as f:
				file_content = f.read()
				# TODO: isolate counting
				num_of_lines = len(file_content.splitlines())
				num_of_words = len(file_content.split())
				total_words += num_of_words
				total_lines += num_of_lines

				total_bytes += f.tell()
				if len(argument) >= 1:
					global multiple_flags
					multiple_flags = True
					if line_flag in argument:
						results.extend([num_of_lines])
					if word_flag in argument:
						results.extend([num_of_words])
					if byte_flag in argument:
						results.extend([f.tell()])
					if max_length in argument:
						max_line_length = count_longest_line(file)
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
			print("we don't handle that situation yet!")
	if len(file_names) > 1:
		if no_flag:
			results.extend([total_lines, total_words, total_bytes, 'total'])
		if multiple_flags:
			if line_flag in argument:
				results.extend([total_lines])
			if word_flag in argument:
				results.extend([total_words])
			if byte_flag in argument:
				results.extend([total_bytes])
			if max_length in argument:
				pass
				#results.extend([total_line_length])
			results.extend(['total'])
		print_results(results)
	#return results

def print_results(results):
	sorted_integers = sorted([i for i in results if type(i) is int])
	sorted_file_names = sorted([i for i in results if type(i) is str])
	sorted_result = sorted_integers+sorted_file_names
	for result in sorted_result:
		if result == sorted_result[-1]:
			print('\t', result)
		else:
			print('\t', result, end='')

# TODO: pass arguments
def missing_file_missing():
	print("Wc: File missing")

# TODO: pass arguments and return list of results
def handle_arguments():
	# Initialise arguments
	help_message = """
	Print newline, word, and byte counts for each FILE, and a total line if
	more than one FILE is specified.  With no FILE, or when FILE is -,
	read standard input.  A word is a non-zero-length sequence of characters
	delimited by white space.\n
	The options below may be used to select which counts are printed, always in
	the following order: newline, word, character, byte, maximum line length."""

	parser = argparse.ArgumentParser(description=help_message,
									 add_help=False)
	parser.add_argument("-l", help="output number of lines", action='store_true')
	parser.add_argument("-w", help="output number of words", action='store_true')
	parser.add_argument("-c", help="output number of bytes", action='store_true')
	parser.add_argument("--help", help="outputs help message", action='help',
						default=argparse.SUPPRESS)
	parser.add_argument("--version",  help="outputs version of wc", action='version',
						version='%(prog)s 1.0')
	parser.add_argument("-L", help="output length of the longest line" ,action='store_true')
	parser.add_argument("filename", nargs='+')
	if len(sys.argv) == 1:
		sys.stdout.write("we don't handle that situation yet!\n")
		sys.exit()
	args = parser.parse_args()
	flag_list = []
	list_of_arguments = []
	if args.l:
		flag_list.append(line_flag)
	if args.w:
		flag_list.append(word_flag)
	if args.c:
		flag_list.append(byte_flag)
	if args.L:
		flag_list.append(max_length)


	# print(args.filename, flag_list)
	#openfile(args.filename, flag_list)
	list_of_arguments.extend([args.filename, flag_list])
	return list_of_arguments

if __name__ == "__main__":
	parsed_arguments_list = handle_arguments()
	#print(parsed_arguments_list[0], parsed_arguments_list[1])
	openfile(parsed_arguments_list[0], parsed_arguments_list[1])
	#print(output)
	#print_results(output)
