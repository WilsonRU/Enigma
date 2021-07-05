import sys
from rotors import *
from enigma import *
from plugboard import *
from reflector import *

class Init(object):

	def __init__(self):
		enigma = Enigma()
		recv = ""
		try:
			setup = sys.argv[1]
			enigma.print_setup()
			for char in setup:
				recv += enigma.encode(char)
			enigma.reset()
			setup = ""
			for char in recv:
				setup += enigma.encode(char)
		except IndexError:
			for setup in sys.stdin:
				for char in setup:
					sys.stdout.write(enigma.encode(char))

	def main(self):
		self.__init__()

if __name__ == "__main__":
	run = Init()