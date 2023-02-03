from COLS import COLS
from ROW import ROW
from csv import csv
from lists import map, kap, sort
from utils import getThe, cosine, many, any
import math

class DATA:
    def __init__(self, src, cols, rows):
        self.rows, self.cols = [], None
        map(csv(src), lambda x: self.add(x)) if src is not None else map(cols+rows, lambda x: self.add(x))            

    def add(self, t):
        if not self.cols is None:
            t = t if isinstance(t, ROW) else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)
        return t, None

    def clone(self):
        data = DATA(None, [self.cols.names], [row.get_cells() for row in self.rows])
        return data

    def stats(self, what, cols, nPlaces):
        def fun(k, col): return col.rnd(col.mid() if (what == 'mid') else col.div(), nPlaces), col.get_name()
        return kap(self.cols.ycols if (cols is None or len(cols) == 0) else cols, fun)
    
    def better(self, row1, row2):
        s1, s2, ys = 0, 0, self.cols.ycols
        x, y = 0, 0
        for _, col in enumerate(ys):
            x = col.norm(row1.cells[col.get_pos()])
            y = col.norm(row2.cells[col.get_pos()])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (y-x)/len(ys))
        return s1/len(ys) < s2/len(ys)

    def dist(self, row1, row2, cols):
        n, d = 0, 0
        for _, col in enumerate(cols if cols is not None else self.cols.xcols):
            n += 1
            d += col.dist(row1.cells[col.get_pos()], row2.cells[col.get_pos()])**getThe()['p']
        return (d/n)**(1/getThe()['p'])

    def around(self, row1, rows):
        def fun(row2):
            ret = dict()
            ret['row'] = row2
            ret['dist'] = self.dist(row1, row2, self.cols.xcols)
            return ret, None
        mapped_val = map(rows if rows is not None else self.rows[1:], fun)
        sorted_val = sort(mapped_val, 'dist')

        return dict(sorted_val)

    def half(self, rows, cols, above):
        A, B, c = 0, 0, 0
        left, right = [], []
        def project(row):
            ret = {}
            ret['row'] = row
            ret['dist'] = cosine(self.dist(row, A, cols), self.dist(row, B, cols), c)
            return ret, None
        rows = rows if rows is not None else self.rows
        some = many(rows, getThe()['Sample'])
        A = above if above is not None else any(some)
        B = self.around(A, some)[math.floor(getThe()['Far'] * len(rows)/1)]['row']
        c = self.dist(A, B, None)

        for n, (r, t) in enumerate(dict(sort(map(rows, project), 'dist')).items()):
            if n <= math.floor(len(rows)/2):
                left.append(t['row'])
                mid = t['row']
            else:
                right.append(t['row'])
        return left, right, A, B, mid, c

    def cluster():
        pass

    def sway():
        pass