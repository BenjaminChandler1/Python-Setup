def hello():
    print("Hello")

def pack(x, y, z):
    return [x, y, z]

def eat_lunch(food):
    if len(food) == 0:
        print("Lunchbox is empty")
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"First I eat {food[0]}")
            else:
                print(f"Next I eat {food[i]}")
                      
hello()
print(pack("x", "y", "z"))
eat_lunch(["chips", "burger", "soda"])                      