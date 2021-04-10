from keyboard_layout import KeyboardLayout


class DbGenerator:
    def __init__(self, primary_start=1000, **kwargs ):
        self.primary_start = primary_start



class KeyboardLayoutsGenerator(DbGenerator):
    def __init__(self, layout='lt_qwerty_win', **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.kl = KeyboardLayout()

    def generate_all_layout(self):
        texts = ''
        for modifier_1 in [0, 41]:
            texts += self.key_rows_to_db(modifier_1=modifier_1) + '\n'
        print(texts)
        return texts

    def key_rows_to_db(self, modifier_1=0, modifier_2=0):
        """
        :param modifier_1: lshift - 41, rshift - 53
        :param modifier_2:
        :return:
        """
        key_rows = self.kl.key_to_unicode(modifier_1=modifier_1, modifier_2=modifier_2)
        db_rows = []
        for i, key_row in enumerate(key_rows):
            db_str = f'INSERT INTO keyboard_layouts VALUES({self.primary_start + i},{key_row[1]},{key_row[0]},{modifier_1},{modifier_2},\'{self.layout}\');'
            db_rows.append(db_str)
        self.primary_start += len(key_rows) + 1
        txt = '\n'.join(db_rows)
        return txt


