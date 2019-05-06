import ctypes

# Dynamic Array Class for creating ArrayList-Like Objects


class DynamicArray:

    # Initialise to empty array A of length equal to 1

    def __init__(self):
        self.n = 0
        self.size = 1
        self.A = self.create_array(self.size)

    # Overload len() to generate length for object

    def __len__(self):
        return self.n

    # Generate New Array of length arr_size

    @staticmethod
    def create_array(arr_size):
        return (arr_size * ctypes.py_object)()

    # Append item to end of array
    # Calls doubling function if array is full

    def append(self, ele):
        if self.n == self.size:
            self.double()
            self.A[self.n] = ele

        self.A[self.n] = ele
        self.n += 1

    # Doubling function : 'Dynamic' aspect of the array

    def double(self):
        A_temp = self.create_array(self.size * 2)
        for i in range(self.size):
            A_temp[i] = self.A[i]
        self.A = A_temp
        self.size = self.size * 2

    # Allow inspection of array elements

    def retrieve(self, ind):
        if not 0 <= ind < self.n:
            return IndexError('Not in Index')
        return self.A[ind]


# HashTable should allow for insertion, deletion, searching and collision


class Hash:

    def __init__(self, size, data_list):
        self.size = size
        self.hash_table = self.create_hash(data_list)

    def empty_hash(self):
        e_h = [[] for _ in range(self.size)]
        return e_h

    def hash_func(self, num):
        return num % self.size

    def create_hash(self, data):
        hash_table = self.empty_hash()
        for i in range(self.size):
            hash_table[self.hash_func(data[i][0])].append(data[i])
        return hash_table

    def append(self, data):
        for i in range(len(data)):
            self.hash_table[self.hash_func(data[i][0])].append(data[i])
        return self.hash_table

    def select(self, index):
        h = self.hash_func(index)
        bucket = self.hash_table[h]
        for i in range(len(bucket)):
            if index == bucket[i][0]:
                return bucket[i][1]
        raise KeyError

    def delete(self, index):
        h = self.hash_func(index)
        bucket = self.hash_table[h]
        for i in range(len(bucket)):
            if index == bucket[i][0]:
                del bucket[i]
                return  # Important to add as we cant loop through remainder of deleted bucket
        raise KeyError


# test = Hash(4, [(24, 'Hello'), (123541, 'There'), (2, 'World'), (100000003, '!')])
# test.append([(1, 2), (3, 4)])
# print(test.delete(3))
# print(test.hash_table)


class StackQueue:

    def __init__(self):
        self.structure = []

    def empty(self):
        if len(self.structure) == 0:
            return True
        return False


class Stack(StackQueue):

    def __init__(self, *args):
        super().__init__(*args)

    def push(self, ele):
        return self.structure.append(ele)

    def pop(self):
        if self.empty() is False:
            del self.structure[-1]
            return self.structure
        return "Pop Error: Stack Empty"


class Queue(StackQueue):

    def __init__(self, *args):
        super().__init__(*args)

    def queue(self, ele):
        if type(ele) != int:
            return "Type Error: Require Integer Input Type"
        self.structure = [ele] + self.structure
        return self.structure

    def dequeue(self):
        if self.empty() is False:
            del self.structure[-1]
            return self.structure
        return "Pop Error: Stack Empty"


s = Stack()
q = Queue()

s.push(1)
s.push(2)
s.push(3)
print(s.structure)

q.queue(1)
q.queue(2)
q.queue(3)
print(q.structure)
