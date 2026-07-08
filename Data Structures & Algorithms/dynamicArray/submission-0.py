class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    # Get value at i-th index of the array
    def get(self, i: int) -> int:
        if 0 <= i < self.length:
            return self.arr[i]
        else:
            raise IndexError("Index out of bounds")

    # Set value n to array at index i
    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.length:
            self.arr[i] = n
        else:
            raise IndexError("Index out of bounds")

    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        # Resize if length reaches its current limit
        if self.length == self.capacity:
            self.resize()
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # Remove the last element in the array
    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]

    # Double the array capacity with old values kept
    def resize(self) -> None:
        # Double array capacity
        self.capacity = 2*self.capacity
        newArr = [0]*self.capacity
        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # Return the number of elements in the array
    def getSize(self) -> int:
        return self.length
        
    # Return capacity of the array
    def getCapacity(self) -> int:
        return self.capacity
