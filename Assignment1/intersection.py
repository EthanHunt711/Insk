class Intersection:
    def __init__(self, posting_list1, posting_list2):
        self.posting_list1 = posting_list1
        self.posting_lits2 = posting_list2
        self.answer = []

    def intesect_and(self):
        i, j = 0, 0
        while i < len(self.posting_list1) and j < len(self.posting_lits2):
            if self.posting_list1[i] == self.posting_lits2[j]:
                self.answer.append(self.posting_list1[i])
                i += 1
                j += 1
            elif self.posting_list1[i] < self.posting_lits2[j]:
                i += 1
            else:
                j += 1
        return self.answer
