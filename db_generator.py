from keyboard_layout import KeyboardLayout


class DbGenerator:
    def __init__(self, primary_start=1000, **kwargs):
        self.primary_start = primary_start


class KeyboardLayoutsGenerator(DbGenerator):
    def __init__(self, layout='lt_qwerty_win', **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.kl = KeyboardLayout()

    def generate_full_layout(self):
        texts = ''
        for modifier_1 in [0, [41, 53]]:
            for modifier_2 in [0, 58]:
                texts += (
                    self.key_rows_to_db_format(
                        modifier_1=modifier_1, modifier_2=modifier_2
                    )
                    + '\n'
                )
        print(texts)
        return texts

    @staticmethod
    def get_first_if_list(element):
        element = element[0] if isinstance(element, list) else element
        return element

    @staticmethod
    def select_modifier_further_side(modifier, position, total):
        if isinstance(modifier, int):
            return modifier

        if position < (total / 2):
            return modifier[1]
        else:
            return modifier[0]

    @staticmethod
    def switch_modifiers(modifier_1, modifier_2):
        """
        If only one modifier exists, make it first one
        :param modifier_1:
        :param modifier_2:
        :return:
        """
        if not modifier_1:
            return modifier_2, 0
        return modifier_1, modifier_2

    def key_rows_to_db_format(self, modifier_1=0, modifier_2=0):
        """
        :param modifier_1: int for single, list for splitting into more left or right
        :param modifier_2: same as above
        :return:
        """
        cur_modifier_1 = self.get_first_if_list(modifier_1)
        cur_modifier_2 = self.get_first_if_list(modifier_2)

        key_rows = [
            self.kl.keys_to_unicode(
                modifier_1=cur_modifier_1, modifier_2=cur_modifier_2, row=r
            )
            for r in range(4)
        ]
        db_rows = []
        for i, key_row in enumerate(key_rows):
            for j, key in enumerate(key_row):
                cur_modifier_1 = self.select_modifier_further_side(
                    modifier_1, j, len(key_row)
                )
                cur_modifier_2 = self.select_modifier_further_side(
                    modifier_2, j, len(key_row)
                )
                cur_modifier_1, cur_modifier_2 = self.switch_modifiers(
                    cur_modifier_1, cur_modifier_2
                )
                db_str = f'INSERT INTO keyboard_layouts VALUES({self.primary_start},{key[1]},{key[0]},{cur_modifier_1},{cur_modifier_2},\'{self.layout}\');'
                db_rows.append(db_str)
                self.primary_start += 1
        txt = '\n'.join(db_rows)
        return txt
