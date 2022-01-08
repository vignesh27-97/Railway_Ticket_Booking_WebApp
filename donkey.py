print("Hello world")

class x:
    
    def __init__(self):
        self.x1=100
        

    def donk(self):
        print("from donk"+self.x1) 
        

class y(x):
    def __init__(self):
        x.__init__(self)
        print(self.x1)
        x.donk(self)

objectx=y()