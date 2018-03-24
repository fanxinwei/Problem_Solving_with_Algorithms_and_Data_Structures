######20171225#######
class BaseClass(object):
	def show(self):
		print('perfect')

class InheritingClass(BaseClass):
	pass
	
x = InheritingClass()
x.show()