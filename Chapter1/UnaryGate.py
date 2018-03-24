from LogicGate import LogicGate
from Connector import Connector

class UnaryGate(LogicGate):
    def __init__(self, label):
        super(UnaryGate, self).__init__(label)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input('Enter pin fot gate '+ self.get_label() + '-->'))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print('sorry')

