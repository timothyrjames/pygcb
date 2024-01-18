class Bitlist(object):
    def __init__(self):
        self.values = []

    def append(self, value):
        if type(value) is bool:
            if value:
                self.values.append(1)
            else:
                self.values.append(0)
        else:
            raise TypeError('Only boolean values can be appended.')
    
    def __getitem__(self, n):
        return self.values[n] == 1

    def __contains__(self, value):
        if type(value) is bool:
            if value:
                return 1 in self.values
            else: 
                return 0 in self.values
        else:
            raise TypeError('Only boolean values can be found.')

    def __setitem__(self, n, value):
        if type(value) is bool:
            if value:
                self.values[n] = 1
            else:
                self.values[n] = 0
        else:
            raise TypeError('Only boolean values can be set.')

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)
    

bits = Bitlist()
bits.append(True)
bits.append(False)
bits.append(True)
bits.append(True)
bits.append(False)

# use __setitem__
bits[2] = True

# use __str__
print(bits)

# use __getitem__
print(bits[3]) 

# use __len__
print('There are %s values in bits.' % len(bits))

# use __contains__
print('Is the value %s is in bits? %s' % (False, False in bits))