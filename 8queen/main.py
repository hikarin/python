import copy

Empty = 0
Queen = 1

Size = 8

class Row:
    class Column:
        def __init__(self, index):
            self.id = index

    def __init__(self):
        self.columns = []

    def deepcopy(self, columns):
        tmp = Row()
        tmp.columns = copy.deepcopy(self.columns)
        return tmp

    def add(self, index):
        column = Row.Column(index)
        self.columns.append(column)

    def print_board(self):
        for y in range(Size):
            print '\n---------------------------------\n',
            print '|',
            for x in range(Size):
                if x == self.columns[y].id:
                    print '*',
                else:
                    print ' ',
                print '|',
        print '\n---------------------------------\n',
    def check(self, num):
        if num >= Size:
            return False

        l = len(self.columns)
        #check row
        for x in range(l):
            if self.columns[x].id == num:
                return False
        #check upleft to downright
        start = num - l
        for x in range(l):
            if self.columns[x].id == start+x:
                return False

        #check downleft to upright
        start = num + l
        for x in range(l):
            if self.columns[x].id == start - x:
                return False

        return True

if __name__ == '__main__':
    stack = []
    for x in range(Size):
        row = Row()
        row.add(x)
        stack.append(row)

    result = None

    while(True):
        if len(stack) == 0:
            print 'No solution'
            break
        tmp = stack[-1]
        for e in tmp.columns:
            e.id

        stack.remove(tmp)
        if len(tmp.columns) == Size:
            print 'Goal Found!'
            result = tmp
            break
        for x in range(Size):
            if tmp.check(x):
                cp = copy.deepcopy(tmp)
                cp.add(x)
                stack.append(cp)


    if result:
        result.print_board()
