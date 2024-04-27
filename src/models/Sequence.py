
class Sequence:

    def __init__(self):
        self.sequence = ""

    def set_sequence(self, sequence):
        self.sequence = sequence

    def get_sequence_as_str(self):
        return str(self.sequence)

    def encoder(self, character):
        encoder = {"_": 0,  "a": 1,  "b": 2,  "c": 3,  "d": 4,  "e": 5,  "f": 6,  "g": 7,  "h": 8, 
                   "i": 9,  "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, 
                   "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
        
        return encoder[character]

    def is_valid(self):
        sequence = self.sequence

        steps = 0
        index = 0
        is_counting = False
        while index < len(sequence):
            if is_counting:
                steps = steps - 1
                if sequence[index] == 'z':
                    steps = steps + 1
                if steps == 0:
                    is_counting = False
            else:
                steps = self.encoder(sequence[index])
                if sequence[index] == 'z':
                        steps = steps + self.encoder(sequence[index + 1])
                        if sequence[index + 1] == 'z':
                            steps = steps + self.encoder(sequence[index + 2])
                            index += 1
                        index += 1
                is_counting = True

            index += 1


        if steps == 0:
            return True
        else:
            return False









        # value = "aa" # [1]
        # value = "abbcc" # [2, 6]
        # value = "dz_a_aazzaaa" # [28, 53, 1]
        # value = "a_" # [0]
        # value = "abcdabcdab" # [2, 7, 7]
        # value = "abcdabcdab_" # [2, 7, 7, 0]
        # value = "zdaaaaaaaabaaaaaaaabaaaaaaaabbaa" # [34]
        # value = "zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_" # [26]
        # value = "za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa"  # [40, 1]

        # value = "_"  # [0]
        # value = "_ad"  # [0]
        # value = "a_"  # [0]
        # value = "_zzzb"  # [0]
        # value = "__________"  # [0]