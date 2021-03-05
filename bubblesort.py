def bubblesort(self):
    for i in range(len(self)):
        for j in range(0, len(self) - i - 1):
            if self[j] > self[j + 1]:
                self[j], self[j + 1] = self[j + 1], self[j]
    return self
array= [12, 3, 89, 10, 75, 30, 55, 1]
print(bubblesort(array))
#    Output
# -> [1, 3, 10, 12, 30, 55, 75, 89]