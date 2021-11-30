class info():
	#properties
	name = "" 
	age = 0
	#method
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def show(self):
		print ("My name is ", self.name)
		print ("I'm ", self.age)
        #self.name
	def run(self):
		print ("I'm running...")
	def go(self):
		print ("I'm going...")

me = info("ABC",19) 
me.show() 
me.run() 
me.go()
