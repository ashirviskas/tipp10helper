class KeyboardLayout:
    def __init__(self):
        self.grid_starts = [0,
                            15,
                            29,
                            43]

    def key_to_unicode(self, modifier_1=0, modifier_2=0):
        # grid, unicode, str
        keypairs = []

        for i, r in enumerate(self.grid_starts):
            keys = input(f'Input {i} row keys from the top with modifiers {modifier_1} and {modifier_2}:\n')
            for j, key in enumerate(keys):
                keypairs.append([r + j, ord(key), key])
                print(keypairs[-1])
            print('Row total:', len(keys))
        return keypairs

