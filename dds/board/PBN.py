class PBN:
    def __init__(self, PBN_input):
        """ @TODO At this point the class assumes starting PBN with N"""
        self._raw_pbn = PBN_input

    def get_cards(self):
        return self._raw_pbn[3:-1]

    def get_dealer(self):
    	return self._raw_pbn[1]

    def _split(self):
    	return self._raw_pbn.split(' ')

    def get_hand(self, hand):
        return self.get_cards().split(' ')[hand]