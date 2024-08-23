class eea:
    def __init__(self,b ,m):
        self.b = b
        self.m = m
        self.lista = [1,0,m]
        self.listb = [0,1,b]
    
    def findinverse(self):
        while True:
            if self.listb[2]==0:
                inverse = self.lista[2]
                return inverse 
            
            elif self.listb[2]==1:
                return self.listb[1]
            
            else:
                temp = [0,0,0]
                qotient = self.lista[2] // self.listb[2]
                for i in range (len(self.lista)):
                    temp[i]= self.lista[i] - qotient*self.listb[i]
                self.lista = self.listb
                self.listb = temp
    
'''
def main():
    test = eea(550, 1759)
    print("the inverse is ",test.findinverse())

if __name__ == "__main__":
    main()
'''