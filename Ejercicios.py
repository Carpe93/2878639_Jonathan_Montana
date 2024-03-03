#Todos los algoritmos se deben presentar en un unico programa con un menú. El progrma debe terminarse cuando el usuario elija la opción 99.

i=5
while i==5 :
        print("Ejercicios iniciales")
        print("1 Calcular el area de un triangulo")
        print("2 ingresar dos numeros y sumarlos")
        print("3 Ingresar un numero y visualizar el numero elevado al cuadrado ")
        print("4 Escribir un algoritmo que convierta de euros a dolares ")
        print("5 Escriba un algoritmo que pida el lado de un cuadrado y muestre el valor del area y del perimetro ")
        print("6 Escribir un algoritmo que determine el area y el volumen de un cilindro")
        print("7 Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el area (𝜋 * R) ² del circulo inscrito")
        print("8 Calcular el promedio de 3 numeros ingresados por teclado ")
        menu=int(input("Seleccionar un ejercicio\n"))

        if(menu==1):    
            print ("1 Calcular el area de un triangulo\n")
            base_triangulo= float(input("digite la base del triangulo\n"))
            altura_triangulo1= float(input("digite la altura del triangulo\n"))
            resultado= (base_triangulo*altura_triangulo) /2
            print(f"el area del triangulo es {resultado}")

        elif(menu==2):
            print ("2 ingresar dos numeros y sumarlos\n")
            num1= float(input("ingrese un numero\n"))
            num2= float(input("ingrese otro numero\n"))
            resultado= (num1+num2)
            print(f"la suma es resultado\n +{resultado}")
                

        elif(menu==3):
            print ("3 Ingresar un numero y visualizar el numero elevado al cuadrado\n")
            num1= float(input("ingrese un numero\n"))
            num2=float(input("elevacion\n"))
            #resultado = ( num1*num2 ) 
            #print("el resultado es\n"+ str (resultado))
            print("el resultado es\n")
            print(pow(num1,num2))

        elif(menu==4):
            print ("4 Escribir un algoritmo que convierta de euros a dolares\n")
            dolar=1.08
            num1=float(input("digite cantidad de euros a convertir\n"))
            resultado=(float(dolar*num1))
            print("el resultado es\n" + str (resultado))

        elif(menu==5):
            print("5 Escriba un algoritmo que pida el lado de un cuadrado y muestre el valor del area y del perimetro\n")
            num1=float(input("lado de un cuadrado\n"))
            resultado1=(num1*num1)
            resultado2=(num1+num1+num1+num1)
            print("el area de un cuadrado es\n" +str(resultado1))
            print("el perimetro de un cuadrado es\n"+str(resultado2))

        elif(menu==6):
            print("6 Escribir un algoritmo que determine el area y el volumen de un cilindro\n")
            num1=float(input("ingresar el radio de un cilindro\n"))
            num2=float(input("ingresar la altura de un cilindro\n"))
            resultado1=(3.1416*(num1*num1))
            resultado2=(3.1416*num2*(num1*num1))
            print("el area de un cilindro es\n"+str(resultado1))
            print("el volumen de un cilindro es\n"+str(resultado2))

        elif(menu==7):
            print("7 Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el area (𝜋 * R) ² del circulo inscrito\n")
            num1=float(input("ingresar el radio de una circunferencia\n"))
            resultado1=(2*3.1416 * num1)
            resultado2=2*(3.1416*num1)
            print("la longitud de la circunferencia es\n"+ str(resultado1))
            print("el area de un circulo es\n"+ str(resultado2))

        elif(menu==8):
            print("8 Calcular el promedio de 3 numeros ingresados por teclado\n")
            num1=float(input("ingresar un numero\n"))
            num2=float(input("ingresar otro numero\n"))
            num3=float(input("ingresar otro numero\n"))
            resultado=(num1+num2+num3/3)
            print("el promedio de sus 3 numeros es\n"+str(resultado))

        else:
            print("Digite un numero del 1 al 8")

        respuesta=input("¿Desea continuar? 1 para si 99 para no\n")
        if(respuesta =="99"): 

                print("Gracias")
                
                break
                    
                    
        else:
                print("Continuemos\n")  
                
                  

