from LogicGate import LogicGate
from BinaryGate import BinaryGate

class OrGate(BinaryGate):
    def __init__(self, label):
        super(OrGate, self).__init__(label)

    def perform(self):
        A = self.get_pinA()
        B = self.get_pinB()
        if A == 0 and B == 0:
            return 0
        else:
            return 1
