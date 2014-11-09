class Integer:
	def __init__(self, n):
		self.n = n
	def __iter__(self): 
		self.t = self.n
		return self
	def next(self):
		self.t=self.n
		if self.t == 0:
			raise StopIteration()
		else:
			r = self.t % 2
			self.t = self.t /2
			return r
			
k = Integer(255)	

for bit in k:
	print bit

# in python 3
class Integer3:
    def __init__(self, n):
        self.n = n
    def __iter__(self):  
        self.t = self.n   
        return self 
    def __next__(self): 
        self.t=self.n
        if self.t == 0:
            raise StopIteration()
        else:
            r = self.t % 2
            self.t = self.t /2
            return r
            
k = Integer3(255)     

for bit in k:
    print (bit ,end =' ')

