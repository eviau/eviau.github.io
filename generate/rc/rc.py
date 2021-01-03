import os

if __name__ == "__main__":
    destdir = "rc"
    files = [f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f))]
    for f in files:
        with open( f[0:-4] + ".html", "w") as extenso:
            with open("preambule.txt", "r") as preambule:
                row = preambule.readline()
                while (len(row) >0):
                    print(row, file=extenso)
                    row = preambule.readline()

            with open(destdir+ "/" + f, "r") as preambule:
                row = preambule.readline()
                while (len(row) >0):
                    print(row, file=extenso)
                    row = preambule.readline()

            with open("end.txt", "r") as end:
                row = end.readline()
                while (len(row) >0):
                    print(row, file=extenso)
                    row = end.readline()
