if __name__ == "__main__":
	import sys
	script_name = sys.argv[0]
	allowed_options = ['-l', '-w', '-c']
	results = []
	total_words = 0
	total_lines = 0
	total_bytes = 0
	one_flag = False
	no_flag = False
	multiple_flags = False
	flag_count = 0

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
					if len(argument) > 1:
						global multiple_flags
						global flag_count
						multiple_flags = True
						for i in argument:
							if i == '-l':
								flag_count += 1
								results.extend([num_of_lines])
							if i == '-w':
								flag_count += 1
								results.extend([num_of_words])
							if i == '-c':
								flag_count += 1
								results.extend([f.tell()])
						results.extend([file])
					elif len(argument) == 1:
						global one_flag
						one_flag = True
						if argument[0] == '-l':
							results.extend([num_of_lines, file])
						elif argument[0] == '-w':
							results.extend([num_of_words, file])
						elif argument[0] == '-c':
							results.extend([f.tell(), file])
					else:
						global no_flag
						no_flag = True
						results.extend([num_of_lines, num_of_words, f.tell(), file])
					print_results(results)
					results.clear()
			except OSError:
				print("miniwc: we don't handle that situation yet!")
			except UnicodeDecodeError:
				with open(sys.argv[1], 'rb') as f:
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
			elif one_flag:
				for flag in argument:
					if flag == '-l':
						results.extend([total_lines])
					elif flag == '-c':
						results.extend([total_bytes])
					elif flag == '-w':
						results.extend([total_words])
					results.extend(['total'])
			elif multiple_flags:
				for flag in argument:
					if flag == '-l':
						results.extend([total_lines])
					if flag == '-w':
						results.extend([total_words])
					if flag == '-c':
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

	#check for flags in the list
	if len(sys.argv) == 1:
		missing_file_missing()

	elif sys.argv[1][0] == '-':
		if len(sys.argv[1]) == 1:
			missing_file_missing()
		else:
			flag_character = '-'
			flags = [flag for flag in sys.argv if flag[0].lower() == flag_character]
			last_flag = flags[-1]
			last_flag_index = sys.argv.index(last_flag)
			file_in_argument = sys.argv[last_flag_index+1:]
			if len(flags) >= 1:
				if any(i in allowed_options for i in flags):
					openfile(file_in_argument, flags)

			#if sys.argv[1:] in allowed_options:
			else:
				print("breaking out")
				pass

	else:
		argument = []
		openfile(sys.argv[1:],argument)