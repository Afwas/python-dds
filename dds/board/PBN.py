class PBN:
    def __init__(self, PBN_text):
        self._raw_pbn = self._clean_pbn(PBN_text)

    def _clean_pbn(self, PBN_text):
        """Searches for the deal within the string
        starting with the character for the first hand"""
        return PBN_text[PBN_text.find(":") - 1:]

    def getDealer(self):
    	return self._raw_pbn[0]

    def _split(self):
    	return self._raw_pbn.split(' ')