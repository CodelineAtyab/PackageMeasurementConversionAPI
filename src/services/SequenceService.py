from ..models.Sequence import Sequence


class SequenceService:

    def __init__(self):
        self.sequence = Sequence()
        # self.sequence_history = SequenceHistory()

    def get_sequence(self, str_representation):
        self.sequence.set_sequence(str_representation)

        if self.sequence.is_valid():
            pass
        else:
            raise Exception

    def process_sequence(self):
        sequence = self.sequence.get_sequence_as_str()

        # print("sequence = " + sequence)

        # sequence = "aa" # [1]
        # sequence = "abbcc" # [2, 6]
        # sequence = "dz_a_aazzaaa" # [28, 53, 1]
        # sequence = "a_" # [0]
        # sequence = "abcdabcdab" # [2, 7, 7]
        # sequence = "abcdabcdab_" # [2, 7, 7, 0]
        # sequence = "zdaaaaaaaabaaaaaaaabaaaaaaaabbaa" # [34]
        # sequence = "zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_" # [26]
        # sequence = "za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa"  # [40, 1]

        # sequence = "_"  # [0]
        # sequence = "_ad"  # [0]
        # sequence = "a_"  # [0]
        # sequence = "_zzzb"  # [0]
        # sequence = "__________"  # [0]

        encoder = {"_": 0,  "a": 1,  "b": 2,  "c": 3,  "d": 4,  "e": 5,  "f": 6,  "g": 7,  "h": 8, 
                   "i": 9,  "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, 
                   "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

        output = []
        index = 0
        is_counting = False
        while index < len(sequence):
            if is_counting:
                if steps != 0:
                    if sequence[index] == 'z':
                        sum = sum + encoder[sequence[index]]
                    else:         
                        sum = sum + encoder[sequence[index]]
                        steps -= 1
                        if (index + 1) == len(sequence):
                            output.append(sum)
                else:
                    if steps == 0:
                        index -= 1
                    output.append(sum)
                    is_counting = False
            else:
                sum = 0
                steps = encoder[sequence[index]]

                if steps == 0 and index + 1 == len(sequence):
                    output.append(sum)
                else:
                    if sequence[index] == 'z':
                        steps = steps + encoder[sequence[index + 1]]
                        if sequence[index + 1] == 'z':
                            steps = steps + encoder[sequence[index + 2]]
                            index += 1
                        index += 1
                    is_counting = True
            index += 1

        return output