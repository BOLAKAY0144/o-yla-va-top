import random as t
def oyin_1():
    n1=0
    while True:
        print('O\'lanishi kerak son oralig\'ini kiriting yani a va b larni')
        a1=int(input('a='))
        b1=int(input('b='))
        a=t.randrange(a1,b1)
        while True:
            n1+=1
            n=int(input('Tahmin qiling: '))
            if n==a:
                print('Urra topdiz !!!')
                n1=0
                a=t.randrange(a1,b1)
                print('1: Yana o\'ynash \t 2: Bosh menyuga qaytish')
                qayta=input('Nma buyurasiz: ')
            elif n>a:
                print('Kiritgan soniz  o\'ylangan sondan katta ???')
            elif n<a:
                print('Kiritgan soniz  o\'ylangan sondan kichik ???')
            
            if n1!=a:
                n1+=1
                continue
            
            if int(qayta)==1:
                continue
            elif int(qayta)==2:
                break
def main():
    oyin_1()
main()
    
        