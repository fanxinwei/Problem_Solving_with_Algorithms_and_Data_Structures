from AndGate import AndGate
from NotGate import NotGate
from OrGate import OrGate
from Connector import Connector


G1 = AndGate('G1')
G2 = AndGate('G2')
G3 = OrGate('G3')
G4 = NotGate('G4')

c1 = Connector(G1, G3)
c2 = Connector(G2, G3)
c3 = Connector(G3, G4)

print(G4.get_output())
