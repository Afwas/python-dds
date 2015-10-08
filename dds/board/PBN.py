class PBN:
    def __init__(self, PBN_input):
        """self._raw_pbn is meant to always be available and may never be edited.
        self.PBN is a cleaned up and checked version of the current PBN"""
        self._raw_pbn = PBN_input
        self.PBN = self._convert_to_north_leader()

    def _convert_to_north_leader(self):
        if self._raw_pbn[1] == 'N':
            return self._raw_pbn
        hands = self._raw_pbn[3:-1].split(' ')
        if self._raw_pbn[1] == 'E':
            return "[N:" + hands[3] + ' ' + hands[0] + ' ' + hands[1] + ' ' + hands[2] + ']'
        if self._raw_pbn[1] == 'S':
            return "[N:" + hands[2] + ' ' + hands[3] + ' ' + hands[0] + ' ' + hands[1] + ']'
        if self._raw_pbn[1] == 'W':
            return "[N:" + hands[1] + ' ' + hands[2] + ' ' + hands[3] + ' ' + hands[0] + ']'

    def get_cards(self):
        return self.PBN[3:-1]

    def get_dealer(self):
    	return self.PBN[1] 

    def _split(self):
    	return self.PBN.split(' ')

    def get_hand(self, hand):
        return self.get_cards().split(' ')[hand]