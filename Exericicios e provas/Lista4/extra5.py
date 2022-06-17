
def Floyd(n):
    
    count = 1 
    
    for i in range(1, n+1):
        print('='*20)
        
        for j in range(1, i+1):
            print(count,end=' ')
            count = count + 1
            
        print()



n = int(input('Digite um número: '))
Floyd(n)