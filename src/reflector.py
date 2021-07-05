class Reflector(object):

    def __init__(self, setting):
        self.setting = setting
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings = {"A":   "EJMZALYXVBWFCRQUONTSPIKHGD",
                        "B":    "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                        "C":    "FVPJIAOYEDRZXWGCTKUQSBNMHL",
                        "D": 	"ESOVPZJAYQUIRHXLNFTGKDCMWB"}

        self.sequence = self.sequence_settings()

    def sequence_settings(self):
        return self.settings[self.setting]

    def forward(self, index):
        return self.sequence.index(self.base[index])