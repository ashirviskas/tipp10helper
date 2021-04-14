import re


class LessonBuilder:
    def __init__(self, allowed_caharcters, words_dataset_fp, sentences_dataset_fp):
        self.allowed_caharcters = allowed_caharcters
        self.words_dataset = open(words_dataset_fp, 'r').read()
        self.sentence_dataset = open(sentences_dataset_fp, 'r').read()

    def get_words(self):
        allowed_characters_r = re.compile(
            '^[' + ''.join(self.allowed_caharcters) + ']+$'
        )
        all_words = re.split(r'\s', self.words_dataset)
        filtered_words = [w for w in all_words if allowed_characters_r.match(w)]
        return filtered_words


if __name__ == '__main__':
    lb = LessonBuilder(
        'asdfertyui',
        words_dataset_fp='../tmp/lt_test',
        sentences_dataset_fp='../tmp/lt_test',
    )
    print(lb.get_words())
