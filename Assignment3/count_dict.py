class Count_dict:
    def __init__(self, word_set, sentences):
        self.word_set = word_set
        self.sentences = sentences

    def count_dict(self):
        word_count = {}
        for word in self.word_set:
            word_count[word] = 0
            for sent in self.sentences:
                if word in sent:
                    word_count[word] += 1
        return word_count
