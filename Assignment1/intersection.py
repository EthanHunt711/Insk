class Intersection:
    def __init__(self, posting_list1, posting_list2):
        self.posting_list1 = posting_list1
        self.posting_lits2 = posting_list2
        self.answer = []

    def intersect_and(self):
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

    def intersect_or(self):
        if len(self.posting_list1) and len(self.posting_lits2) > 0:
            self.answer = self.posting_list1 + self.posting_lits2
            if len(set(self.answer)) > 0:
                return set(self.answer)
            return f'No match were found'
        else:
            return []

    def intersect_not(self):
        if len(self.posting_list1) and len(self.posting_lits2) > 0:
            self.answer = set(self.posting_list1) - set(self.posting_lits2)
            if len(self.answer) > 0:
                return self.answer
            return f'No match were found'
        else:
            return []