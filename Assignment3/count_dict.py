class Count_dict:
    def __init__(self, word_set, token_list):
        self.word_set = word_set
        self.token_list = token_list

    def count_dict(self):
        word_count = {}
        for word in self.word_set:
            word_count[word] = 1
            for token in self.token_list:
                if token in word_count:
                    word_count[token] += 1
        return word_count
