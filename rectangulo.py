class Rectangular:
    def __init__(self,base,altura):
        
       self.__base=base
       self.__altura=altura
       
       if self.__base<=0 or self.__altura <=0:
          raise ValueError("La base y la altura no deben ser 0 o negativas.")
          
           
        
       if self.__base ==self.__altura:
          raise ValueError("La base y la altura no deben ser iguales.")
         
            
    def area(self):
        return self.__base*self.__altura 
    
    def perimetro(self):
        return 2 * (self.__base+self.__altura)
    
