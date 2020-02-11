class Student(object):
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.list_labs = [None] * self.conf["lab_num"]
        self.list_notes = [0] * self.conf["lab_num"]
        self.max_exam = 0

    def make_lab(self, m, n=None):
        if n is None:
            n = self.list_labs.index(None)
        if 0 <= n <= self.conf["lab_num"] and m <= self.conf["lab_max"]:
            self.list_labs[n] = m
            self.list_notes[n] += 1
        return self

    def make_exam(self, m):
        if m <= self.conf["exam_max"]:
            self.max_exam = m
        return self

    def is_certified(self):
        count = sum(self.list_notes) + self.max_exam
        passed = (count / (self.conf["exam_max"] + self.conf["lab_max"] *
                           self.conf["lab_num"])) >= self.conf["k"]
        return count, passed


