class Rotor(object):

    def __init__(self, settings):
        self.setting = settings[0]
        self.ringoffset = settings[1]
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings = {
                "I":    ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", ["R"], ["Q"]],
                "II":   ["AJDKSIRUXBLHWTMCQGZNPYFVOE", ["F"], ["E"]],
                "III":  ["BDFHJLCPRTXVZNYEIWGAKMUSQO", ["W"], ["V"]],
                "IV":   ["ESOVPZJAYQUIRHXLNFTGKDCMWB", ["K"], ["J"]],
                "V":    ["VZBRGITYUPSDNHLXAWMJQOFECK", ["A"], ["Z"]],
                "VI":   ["JPGVOUMFYQBENHZRDKASXLICTW", ["AN"], ["ZM"]],
                "VII":  ["NZJHGRCXMYSWBOUFAIVLPEKQDT", ["AN"], ["ZM"]],
                "VIII": ["FKQHTLXOCBJSPDZRAMEWNIUYGV", ["AN"], ["ZM"]]}
        self.turnovers = self.settings[self.setting][1]
        self.notch = self.settings[self.setting][2]
        self.sequence = None
        self.turnover = False
        self.reset()

    def reset(self):
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.sequence = self.sequence_settings()
        self.ring_settings()

    def sequence_settings(self):
        return self.settings[self.setting][0]

    def ring_settings(self):
        for _ in range(self.ringoffset):
            self.rotate()

    def forward(self, index):
        return self.base.index(self.sequence[index])

    def reverse(self, index):
        return self.sequence.index(self.base[index])

    def rotate(self):
        self.base = self.base[1:] + self.base[:1]
        self.sequence = self.sequence[1:] + self.sequence[:1]
        if(self.base[0] in self.turnovers):
            self.turnover = True