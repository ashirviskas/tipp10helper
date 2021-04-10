import mappings

class KeyboardLayout:
    def __init__(self):
        # Which index each row starts with (for use with grid indexes)
        self.grid_starts = [0,
                            15,
                            29,
                            43]

    def key_to_unicode(self, modifier_1=0, modifier_2=0, use_rows=[0, 1, 2, 3]):
        """

        :param modifier_1:
        :param modifier_2:
        :param use_rows: which rows to use
        :return:
        """
        # grid, unicode, str
        keypairs = []

        for row in use_rows:
            keys = input(f'Input {row} row keys from the top with modifiers {mappings.modifiers[modifier_1]} and {mappings.modifiers[modifier_2]}:\n')
            for j, key in enumerate(keys):
                keypairs.append([self.grid_starts[row] + j, ord(key), key])
                print(keypairs[-1])
            print('Row total:', len(keys))
        return keypairs

