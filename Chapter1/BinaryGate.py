from LogicGate import LogicGate
#from Connector import Connector

class BinaryGate(LogicGate):
	def __init__(self,label):  
		super(BinaryGate,self).__init__(label)
		
		self.pinA = None
		self.pinB = None
		
	def get_pinA(self):
		if self.pinA == None:
			return int(input("pinA for gate " + self.get_label() + "-->"))
		else:
			return self.pinA.get_from().get_output()

	def get_pinB(self):
		if self.pinB == None:
			return int(input("pinB for gate " + self.get_label() + "-->"))
		else:
			return self.pinB.get_from().get_output()

	def set_next_pin(self, source):
		print(source)
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				print('Sorry')

	
	
