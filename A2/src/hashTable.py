
class HashTable():

    tab = None
    length = None

    def __init__(self):
        self.tab = dict()
        self.length = 0

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
            self.length +=1
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
            self.length += 1

    def __len__(self):
        return self.length

    def __contains__(self, key):
        if key in self.tab:
            l = self.tab[key]
            for i in l:
                if key == i[0]:
                    return True
        return False

    def dict_len(self):
        return len(self.tab)

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

