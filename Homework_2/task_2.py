class Buffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Очистка буфера.")
            self.buffer.clear()

    
    def get_data(self):
        if not self.buffer:
            print("Буфер пуст.")
        else:
            return self.buffer

buffer = Buffer()

buffer.add_data(1)
buffer.add_data(2)
buffer.add_data(3)
buffer.add_data(4)
buffer.add_data(5) 

data = buffer.get_data()  

buffer.add_data(6)
buffer.add_data(7)

data = buffer.get_data()  
print(data)