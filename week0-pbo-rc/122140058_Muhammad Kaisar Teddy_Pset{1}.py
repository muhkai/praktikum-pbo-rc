def SegitigaSamaKaki():
    heigth = int(input("Height: "))

    for i in range(1, heigth + 1):
        for j in range(heigth, i, -1):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print()

if __name__ == "__main__":
    SegitigaSamaKaki()
