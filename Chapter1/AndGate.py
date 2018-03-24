from LogicGate import LogicGate
from BinaryGate import BinaryGate

class AndGate(BinaryGate):
	def __init__(self,label):  
		super(AndGate, self).__init__(label)

	def perform(self):
		A = self.get_pinA()
		B = self.get_pinB()
		if A == 1 and B == 1:
			return 1
		else:
			return 0
		
	
	
	
