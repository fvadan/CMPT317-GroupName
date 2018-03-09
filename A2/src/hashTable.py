
class HashTable():

    tab = None

    def __init__(self):
        self.tab = dict()

    def __getitem__(self, key):
        if key not in self.tab:
            return None
        else:
            l = self.tab[key]
            if len(l) == 1:
                return l[0][1]
            else:
                for i in l:
                    if k == i[0]:
                        return i[1]

    def __setitem__(self, key, item):
        if key not in self.tab:
            self.tab[key] = [(key, item)]
        else:
            l = self.tab[key]
            for i in range(len(l)):
                if key == l[i][0]:
                    newItem = (key, item)
                    l[i] = newItem
                    return
            # Didn't find key: Safe to append:
            l.append((key, item))
            self.tab[key] = l

    def items(self):
        for k,v in self.tab.items():
            for i in v:
                yield i[0],i[1]

    def keys(self):
        for k,v in self.tab.items():
            for i in v:
                yield i[0]

    def __iter__(self):
        for k,v in self.tab.items():
            for i in v:
                yield i[1]

