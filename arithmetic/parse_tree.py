from __future__ import annotations

from typing import Optional

operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x // y}


class ParseTree:
    def __init__(self, s: str, parent: Optional[ParseTree]):
        self.str = s
        self.tail = []
        self.parent = parent

    def __str__(self):
        if self.tail:
            child = " [" + " ".join(map(str, self.tail)) + "]"
        else:
            child = ""
        res = str(self.str) + child
        return res

    def eval(self):
        if self.str == 'n':
            assert len(self.tail) == 1
            return int(self.tail[0])
        if self.str == "G":
            assert len(self.tail) in [1, 3]
            if len(self.tail) == 1:
                assert self.tail[0].str == "n"
                return self.tail[0].eval()
            if len(self.tail) == 3:
                assert [x.str for x in self.tail] == "( E )".split()
                return self.tail[1].eval()
        if self.str == 'F':
            assert len(self.tail) in [1, 2]
            if len(self.tail) == 1:
                assert self.tail[0].str == 'G'
                return self.tail[0].eval()
            if len(self.tail) == 2:
                assert [x.str for x in self.tail] == "- F".split()
                return -self.tail[1].eval()
        if self.str == "T":
            assert len(self.tail) == 2
            assert [x.str for x in self.tail] == "G L".split()
            g, l = self.tail
            g_val = g.eval()
            while l.tail:
                assert [x.str for x in l.tail] in ["* G L".split(), "/ G L".split()]
                op_tree, g2, l2 = l.tail
                op = operators[op_tree.str]
                g2_val = g2.eval()
                g_val = op(g_val, g2_val)
                l = l2
            return g_val
        if self.str == "E":
            assert len(self.tail) in [2,3]
            assert self.tail[0].str in ['-','T']
            if self.tail[0].str == '-':
                assert self.tail[1].str == "F"
                return -self.tail[1].eval()
            else:
                assert [x.str for x in self.tail] == "T K".split()
                g, l = self.tail
                g_val = g.eval()
                while l.tail:
                    assert [x.str for x in l.tail] in ["+ T K".split(), "- T K".split()]
                    op_tree, g2, l2 = l.tail
                    op = operators[op_tree.str]
                    g2_val = g2.eval()
                    g_val = op(g_val, g2_val)
                    l = l2
                return g_val
