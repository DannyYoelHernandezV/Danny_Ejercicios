from rectangulo import Rectangular
def main():
    try:
    
        base= float(input("Introduce la base del rectángulo :"))
        altura=float(input("Introduce la altura del rectángulo: "))

        rect= Rectangular(base,altura)
        rect2=Rectangular(base,altura)

        print(f"El área del rectángulo es: {rect.area()}")
        print(f"El perímetro del rectángulo es: {rect.perimetro()}")
        
        print(f"El área del segundo rectángulo es: {rect2.area()}")
        print(f"El perímetro segundo del rectángulo es: {rect2.perimetro()}")
        
        
        
        
         

    except ValueError as e:
        print(e)
        
if __name__=="__main__":
    main()       
