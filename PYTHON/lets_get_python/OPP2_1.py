class Base(object):
	def __init__(self):
		self.x = 10
class Inclass(Base):
	def __init__(self):
		super(Inclass,self).__init__()
		self.x = 20
		
my = Inclass()
print (my.x)
print Base.__subclasses__()