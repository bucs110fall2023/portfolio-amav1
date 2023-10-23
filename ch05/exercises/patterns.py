def star_pyramid():
    rows = int(input("Please input a number of rows:"))
    for i in range(rows):
        for x in range(rows + 1):
           print(x * "*")
           

def rstar_pyramid():
    rows = int(input("Please input a number of rows:"))
    for x in range(rows, 0, -1):
        print (x * "*")

star_pyramid()
rstar_pyramid()


