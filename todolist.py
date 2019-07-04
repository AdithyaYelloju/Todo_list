class ToDoList:
	
	def __init__(self, file_name):
		self.file_name = file_name
		self.tasks = self.load_file_into_list()

	def load_file_into_list(self):
		tasks = []
		with open(self.file_name, 'r') as file:
			for task in file:
				tasks.append(task.strip())
		return tasks

	def list_task(self):
		for index, task in enumerate(self.tasks, start=1):
			print('{}) {}'.format(index, task))

	def write_into_file(self):
		with open(self.file_name, 'w') as file:
			for task in self.tasks:
				file.write('{}\n'.format(task))

	def add_task(self, task):
		self.tasks.append(task)
		self.write_into_file()

	def done_task(self, task_index):
		if(input("Do you done '"+self.tasks[task_index-1]+"' for sure(y/n)? ") == 'y'):
			try:
				del(self.tasks[task_index-1])
				self.write_into_file()
			except IndexError:
				print("There is no open task  with index {}".format(task_index))
		else:
			print("Okay")

def todo_help():
	print()
	print("To-do List")
	print("* Craete new task: [todo Task]")
	print("* Mark a task ad done: [done Task]")
	print("* List the tasks: [list]")
	print()

def run():
	todolist = ToDoList("todolist.txt")
	todo_help()
	
	while(True):	
		cmd_details = input("Enter cmd:")
		cmd = cmd_details.split(' ',1)[0]

		if(cmd == 'list'):
			todolist.list_task()
		elif(cmd == 'todo'):
			task_description = cmd_details.split(' ',1)[1]
			todolist.add_task(task_description)
		elif(cmd == 'done'):
			task_index = int(cmd_details.split(' ',1)[1])
			todolist.done_task(task_index)
		elif(cmd == 'help'):
			todo_help()
		else:
			break



run()