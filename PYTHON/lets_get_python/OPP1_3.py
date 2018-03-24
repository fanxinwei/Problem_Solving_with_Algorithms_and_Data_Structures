######20171225#######
class Charactor(object):
	def __init__(self, name):
		self.health = 100
		self.name = name
	def show(self):
		print(self.name)
		
class Student(Charactor):
	def __init__(self, name, forgename):
		super(Student,self).__init__(name)
		self.forge = Forge(forgename)
		
class Forge(object):
	def __init__(self, forgename):
		self.name = forgename

Me = Student('fan','ivy')
print(Me.name)
print(Me.forge.name)