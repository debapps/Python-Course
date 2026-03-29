class StudentsDataException(Exception):
	def __init__(self, message):
		super().__init__(message)

class BadLine(StudentsDataException):
	def __init__(self, line):
		message = f'Bad line: {line}'
		super().__init__(message)

class FileEmpty(StudentsDataException):
	def __init__(self, filename):
		message = f'File is empty: {filename}'
		super().__init__(message)

student_dir = {}

class StudentData:
	def __init__(self, line):
		self.data = line
		try:
			self.fname, self.lname, self.grade = self.data.strip().split('\t')
			self.name = f'{self.fname} {self.lname}'
			self.grade = float(self.grade)
		except ValueError:
			raise BadLine(self.data)

	def get_name(self):
		return self.name

	def get_grade(self):
		return self.grade

class FileReadHandle:
	def __init__(self, filename):
		self.file_name = filename
		try:
			self.file = open(self.file_name, 'rt', encoding='utf-8')
		except IOError:
			raise StudentsDataException(f'Cannot open file: {self.file_name}')

	def read_file(self):
		lines = self.file.readlines()

		if not lines:
			raise FileEmpty(self.file_name)

		for line in lines:
			try:
				student = StudentData(line)

				name = student.get_name()
				grade = student.get_grade()
				if name in student_dir.keys():
					student_dir[name] += grade
				else:
					student_dir[name] = grade

			except BadLine as e:
				print(e)

if __name__ == '__main__':
	filename = 'data/input/student_data.txt'
	try:
		file_handle = FileReadHandle(filename)
		file_handle.read_file()
		
		print('\nStudent data report:\n')
		for name, grade in student_dir.items():
			print(f'{name} : {grade}')

	except StudentsDataException as e:
		print(e)
    

		