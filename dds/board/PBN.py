class PBN(Board):
    def __init__(self, PBN):
        self._raw_pbn = self._clean_pbn(PBN)

    def _clean_pbn(self, PBN):
        """Searches for the deal within the string
        starting with the character for the first hand"""
        return PBN[PBN.find(":") - 1:]

    def getDealer(self):
    	return self.PBN[1]

    def _split(self):
    	return self._clean_pbn.split(' ')