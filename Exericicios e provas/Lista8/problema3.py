def mdc_recursive(x, y):
    return x if y == 0 else mdc_recursive(y, x % y)
    
x = int(input("Digite x: "))
y = int(input("Digite y: "))

print(mdc_recursive(x,y))