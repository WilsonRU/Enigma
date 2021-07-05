from rotors import *
from plugboard import *
from reflector import *

class Enigma(object):
    def __init__(self):
        self.numcycles = 0
        self.rotors = []
        '''Enigma Setup '''
        self.rotorsettings = [("VIII", 0),
                            ("V", 0),
                            ("II", 0),
                            ("IV", 0)]
        self.reflectorsetting = "C"

        self.plugboardsetting = []
        self.plugboard = Plugboard(self.plugboardsetting)
        for i in range(len(self.rotorsettings)):
            self.rotors.append(Rotor(self.rotorsettings[i]))
        self.reflector = Reflector(self.reflectorsetting)

    def print_setup(self):
        print("Rotors:")
        for r in self.rotors:
            print(r.setting, "\t", r.sequence)
        print("\nReflector: ")
        print(self.reflector.setting, "\t", self.reflector.sequence, "\n")
        print("\nPlugboard:")
        print(self.plugboard.mapping, "\n")

    def reset(self):
        self.numcycles = 0
        for r in self.rotors:
            r.reset()

    def encode(self, c):
        c = c.upper()
        if (not c.isalpha()):
            return c
        self.rotors[0].rotate()
        if self.rotors[1].base[0] in self.rotors[1].notch:
            self.rotors[1].rotate()
        for i in range(len(self.rotors) - 1):
            if(self.rotors[i].turnover):
                self.rotors[i].turnover = False
                self.rotors[i + 1].rotate()
        index = self.plugboard.forward(c)
        for r in self.rotors:
            index = r.forward(index)
        index = self.reflector.forward(index)
        for r in reversed(self.rotors):
            index = r.reverse(index)
        c = self.plugboard.reverse(index)
        return c

    def decode(self, d):
        d = d.upper()
        