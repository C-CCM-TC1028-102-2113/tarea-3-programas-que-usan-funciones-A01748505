def es_bisiesto(año):
    if (año%4==0 and año%100!=0) or (año%400==0):
        print("True")
    else:
        print("False")
def main():
    #escribe tu código abajo de esta línea
    año=int(input())
    es_bisiesto(año)
pass
if __name__=='__main__':
    main()
