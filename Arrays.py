import ctypes

# Dynamic Array Class for creating ArrayList-Like Objects

class DynamicArray():

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


# F = DynamicArray()

# F.append(5)
# print(F.retrieve(0))


