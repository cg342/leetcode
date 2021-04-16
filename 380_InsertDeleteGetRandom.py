class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ind = {}
        self.data = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ind:
            return False
        
        self.data.append(val)
        self.length += 1
        self.ind[val] = self.length-1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ind:
            pos = self.ind[val]
            last = self.data[self.length-1]
            self.data[pos] = last
            self.ind[last] = pos
            del self.ind[val]
            self.data.pop()
            self.length -= 1
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        pos = random.randint(0,self.length-1)
        return self.data[pos]