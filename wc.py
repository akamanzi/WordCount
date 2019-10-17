if __name__ == "__main__":
	import sys
	import argparse
	script_name = sys.argv[0]
	allowed_options = ['l', 'w', 'c']
	line_flag = 'l'
	word_flag = 'w'
	byte_flag = 'c'
	results = []
	total_words = 0
	total_lines = 0
	total_bytes = 0
	no_flag = False
	multiple_flags = False


	def openfile(file_names, argument):
		global num_of_lines
		global num_of_words

		for file in file_names:
			num_of_lines = 0
			num_of_words = 0
			global total_words, total_lines, total_bytes

			try:
				with open(file, 'r') as f:
					for line in f:
						num_of_lines += 1
						num_of_words += len(line.split())

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
						results.extend([file])

					else:
						global no_flag
						no_flag = True
						results.extend([num_of_lines, num_of_words, f.tell(), file])
					print_results(results)
					results.clear()
			except OSError:
				print("we don't handle that situation yet!")
			except UnicodeDecodeError:
				with open(file, 'rb') as f:
					for line in f:
						num_of_lines+=1
						line_in_uni = line.decode('latin-1')
						num_of_words += len(line_in_uni.split())
					total_words += num_of_words
					total_bytes += f.tell()
					total_lines += num_of_lines
					print('\t',num_of_lines-1, end='')
					print('\t',num_of_words, end='')
					print('\t', f.tell(), end=' ')
					print('\t',f.name)

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
				results.extend(['total'])
			print_results(results)
	def print_results(results):
		sorted_integers = sorted([i for i in results if type(i) is int])
		sorted_file_names = sorted([i for i in results if type(i) is str])
		sorted_result = sorted_integers+sorted_file_names
		for result in sorted_result:
			if result == sorted_result[-1]:
				print('\t', result)
			else:
				print('\t', result, end='')

	def missing_file_missing():
		print("Wc: File missing")


	def handle_arguments():
		# Initialise arguments
		parser = argparse.ArgumentParser(description="Program that counts words, lines and size of a given file")
		parser.add_argument("-l", help="output number of lines", action='store_true')
		parser.add_argument("-w", help="output number of words", action='store_true')
		parser.add_argument("-c", help="output number of bytes", action='store_true')
		parser.add_argument("filename", nargs='+')
		if len(sys.argv) == 1:
			sys.stderr.write("we don't handle that situation yet!\n")
			sys.exit()
		args = parser.parse_args()
		flag_list = []
		if args.l:
			flag_list.append(line_flag)
		if args.w:
			flag_list.append(word_flag)
		if args.c:
			flag_list.append(byte_flag)

		# print(args.filename, flag_list)
		openfile(args.filename, flag_list)

	handle_arguments()

	# #check for flags and files in the list
	# if len(sys.argv) == 1:
	# 	missing_file_missing()
	#
	# elif sys.argv[1][0] == '-':
	# 	if len(sys.argv[1]) == 1:
	# 		missing_file_missing()
	# 	else:
	# 		flag_character = '-'
	# 		flags = [flag for flag in sys.argv if flag[0].lower() == flag_character]
	# 		last_flag = flags[-1]
	# 		last_flag_index = sys.argv.index(last_flag)
	# 		files_in_list = [single_file for single_file in sys.argv[1:] if single_file[0].lower() != flag_character]
	# 		file_in_argument = sys.argv[last_flag_index+1:]
	# 		used_flags = []
	# 		if len(flags) >= 1:
	# 			for i in flags:
	# 				for j in i:
	# 					used_flags.append(j)
	# 			if any(i in allowed_options for i in used_flags):
	# 				openfile(file_in_argument, used_flags)
	# 			else:
	# 				print("wrong flag used")
	#
	# 		else:
	# 			print("breaking out")
	# 			pass
	#
	# else:
	# 	argument = []
	# 	openfile(sys.argv[1:], argument)