def mdc_recursive(x, y):
    if y == 0:
        return x
    else:
        return mdc_recursive(y, x % y)
    
x = int(input("Digite x: "))
y = int(input("Digite y: "))

print(mdc_recursive(x,y))