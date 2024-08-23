class polynomial:
    # define irreducible polynomial
    m_irr = {2: 0b111, 3: 0b1101, 4: 0b11001, 5: 0b100101, 6: 0b1000011, 7: 0b10000011, 8: 0b1000110110}

    def __init__(self,f,g,n):
        self.m = self.m_irr.get(n)
        self.f= f
        self.g= g

    def multiplication(self):
        result = 0
        temp_f = self.f  
        temp_g = self.g  

        while temp_f > 0:
            if temp_f & 1:
                result ^= temp_g
            temp_g <<= 1
            temp_f >>= 1

        result = self.mod_reduction(result)
        return result

    def addition(self):
        return bin(self.f ^ self.g)[2:]

    def substitution(self):
        return bin(self.f ^ self.g)[2:]

    def mod_reduction(self, h):
        h_str = bin(h)[2:]  

        m_used = self.m
        m_str = bin(m_used)[2:]  

        while len(h_str) >= len(m_str):
            shift = len(h_str) - len(m_str)
            h ^= m_used << shift
            h_str = bin(h)[2:]

        return bin(h)[2:] 

    def division(self):
        temp_f = self.f  
        temp_g = self.g 
        
        f_str = bin(temp_f)[2:]  

        g_str = bin(temp_g)[2:]  

        while len(f_str) >= len(g_str):
            shift = len(f_str) - len(g_str)
            temp_f ^= temp_g << shift
            f_str = bin(temp_f)[2:]

        return bin(temp_f)[2:] 
    
    def inverse(self):
        #write code here
        pass

def main():
    obj = polynomial(0b101,0b111,3)
    print(obj.addition())
    print(obj.substitution())
    print(obj.multiplication())
    print(obj.division())

    return 0

if __name__ == "__main__":
    main()