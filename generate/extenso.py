import pandas as pd

def log(text):
    print(text, file=extenso)

def append_to_file(item):
    item = '<a href="'+ item["link"] + '">' + item["title"] + '</a>' + "<p>" + item["description"] + "</p>"
    log("<li class='extenso-item'> ")
    log(item)
    log("</li>")

if __name__ == "__main__":
    with open("extenso.html", "w") as extenso:
        with open("preambule.txt", "r") as preambule:
            row = preambule.readline()
            while (len(row) >0):
                print(row, file=extenso)
                row = preambule.readline()
        df = pd.read_csv("extenso.csv",delimiter=";",header=0)

        for year in [2020,2019,2018]:
            log("<h3>"+ str(year) + "</h3>")
            log("<ul id='ul-main'>")
            for index,item in df[df["year"] == str(year)].iterrows():
                append_to_file(item)
            log("</ul>")

        with open("end.txt", "r") as end:
            row = end.readline()
            while (len(row) >0):
                print(row, file=extenso)
                row = end.readline()

