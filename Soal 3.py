for i in range(10,25):
    a = i % 2 and i % 3
    if a == 0:
        print("%d bukan prima" %i )
    else:
        print("%d adalah bilangan prima"%i )