class LogicGate(object):
	def __init__(self, label):  #basic has an input and an output
		self.label = label
		self.output = None
	
	def get_label(self):
		return self.label
	
	def get_output(self):
		self.output = self.perform()
		return self.output
	
