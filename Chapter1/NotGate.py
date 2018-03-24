from LogicGate import LogicGate
from UnaryGate import UnaryGate

class NotGate(UnaryGate):
    def __init__(self, label):
        super(NotGate, self).__init__(label)
    def perform(self):
        A = self.get_pin()
        if A == 1:
            return 0
        else:
            return 1
