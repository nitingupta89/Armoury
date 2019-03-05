import random


class powerlist(list):
    def in_batches_of(self, batch_size=1):
        for i in range(0, len(self), batch_size):
            yield self[i:i+batch_size]

    def find(self, val):
        for item in self:
            if item == val:
                return item

    detect = find

    def filter(self, func):
        return [x for x in self if func(x)]

    def any(self, func):
        for item in self:
            if func(item):
                return True

        return False

    def all(self, func):
        for item in self:
            if not func(item):
                return False

        return True

    def reject(self, func):
        return [x for x in self if not func(x)]

    def select(self, func):
        return [x for x in self if func(x)]

    def flatten(self):
        flat_list = []
        for x in self:
            if isinstance(x, list):
                px = PowerList(x)
                flat_list += px.flatten()
            else:
                flat_list.append(x)
        return flat_list

    def shuffle(self):
        '''
        shuffles list in-place
        '''
        random.shuffle(self)

    def sample(self):
        return random.sample(self)

    def sort_by(self, attr, reverse=False):
        return sorted(self, key=lambda x: self._getattr(x, attr), reverse=reverse)

#    def pluck(self):
#        pass
#
#    def findWhere(listOfDicts, props):
#        pass
#
#    def invoke(self, func, args):
#        pass
#
#    def group_by(self):
#        pass
#
#    def count_by(self):
#        pass
#
#    def slice(self):
#        pass
#
#    def partition(self):
#        pass
#
#    def compact(self):
#        pass
#
#    def union(self):
#        pass
#
#    def intersection(self):
#        pass
#
#    def difference(self):
#        pass
#
#    def zip(self):
#        pass
#
#    def unzip(self):
#        pass

    '''
    private methods
    '''
    def _getattr(self, obj, attr):
        if isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, dict):
            return obj[attr]
        else:
            return obj.a.__getattribute__(attr)
