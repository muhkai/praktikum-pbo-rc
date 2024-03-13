def main():

    f = open("Me.txt", "w+")

    f.write("Nama                       : Muhammad Kaisar Teddy\n")
    f.write("NIM                        : 122140058\n")
    f.write("Resolusi Saya di Tahun ini : Saya ingin jago Python")

    f.close()

if __name__ == "__main__":
    main()