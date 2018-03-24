######20171225#######
class Charactor(object):
	def __init__(self):
		self.health = 100
class Student(Charactor):
	def __init__(self):
		super(Student,self).__init__()

fanfan = Student()
print(fanfan.health)