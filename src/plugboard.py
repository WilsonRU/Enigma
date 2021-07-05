from settings import *

class Plugboard(object):

    def __init__(self, mapping):
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.mapping = {}
        for m in self.base:
            self.mapping[m] = m
        for m in mapping:
            self.mapping[m[0]] = m[1]
            self.mapping[m[1]] = m[0]

    def forward(self, c):
        return self.base.index(self.mapping[c])

    def reverse(self, index):
        return self.mapping[self.base[index]]