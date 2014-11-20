#! /usr/bin/python

class Board():
    def __init__(self):
        pass

class PBN(Board):
    def __inti__(self, PBN):
        self._raw_pbn = self._clean_pbn(PBN)

    def _clean_pbn(self, PBN):
        """Searches for the deal within the string
        starting with the character for the first hand"""
        return PBN[PBN.find(":") - 1:]