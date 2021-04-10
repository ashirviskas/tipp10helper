from keyboard_layout import KeyboardLayout


class DbGenerator:
    def __init__(self, primary_start=1000, **kwargs):
        self.primary_start = primary_start


class KeyboardLayoutsGenerator(DbGenerator):
    def __init__(self, layout='lt_qwerty_win', **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.kl = KeyboardLayout()

    def generate_all_layout(self):
        texts = ''
        for modifier_1 in [0, [41, 53]]:
            for modifier_2 in [0, [56, 58]]:
                texts += (
                    self.key_rows_to_db(modifier_1=modifier_1, modifier_2=modifier_2)
                    + '\n'
                )
        print(texts)
        return texts

    @staticmethod
    def get_int_or_first(element):
        """
        :param element:
        :return: if element not int, will return first instance
        """
        element = element if isinstance(element, int) else element[0]
        return element

    @staticmethod
    def select_based_on_side(modifier, position, total):
        if isinstance(modifier, int):
            return modifier

        if position < (total / 2):
            return modifier[1]
        else:
            return modifier[0]

    def key_rows_to_db(self, modifier_1=0, modifier_2=0):
        """
        :param modifier_1: int for single, list for splitting into more left or right
        :param modifier_2: same as above
        :return:
        """
        cur_modifier_1 = self.get_int_or_first(modifier_1)
        cur_modifier_2 = self.get_int_or_first(modifier_2)
        key_rows = self.kl.keys_to_unicode(
            modifier_1=cur_modifier_1, modifier_2=cur_modifier_2
        )
        db_rows = []
        for i, key_row in enumerate(key_rows):
            cur_modifier_1 = self.select_based_on_side(modifier_1, i, len(key_rows))
            cur_modifier_2 = self.select_based_on_side(modifier_2, i, len(key_rows))
            db_str = f'INSERT INTO keyboard_layouts VALUES({self.primary_start + i},{key_row[1]},{key_row[0]},{cur_modifier_1},{cur_modifier_2},\'{self.layout}\');'
            db_rows.append(db_str)
        self.primary_start += len(key_rows) + 1
        txt = '\n'.join(db_rows)
        return txt
