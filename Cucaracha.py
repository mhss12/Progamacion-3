def meun():
    print """
 Menu 
 1 cantidad 
 2 reproducieron  
 3 aplastar 
 4 rociar 
 5 salir"""
def caculadora():
    menu()
opc= int(input("Selecione la opcion"))
while (opc >0 and opc <5):
    c = int(input("ingrese la cantidad"))
    r = int(input("10"))
    a = int (input("1"))
    RO = int(input("5"))
    if (opc==1):
        print "la cantidad de cucarechas",c
        opc = int(input("Seleccione la opcion\n"))
    elif(opc==2):
        print "se reproducieron: ",c+r
        opc = int(input("Seleccione la opcion\n"))
    elif(opc==3):
        print "se aplastaron:",c-a
        opc = int(input("Seleccione la opcion\n"))
    elif(opc==4):
        print "se rociaron:",RO-C
        opc = int(input("Seleccione la opcion\n"))

caculadora()        

