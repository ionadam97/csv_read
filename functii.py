import csv
from datetime import datetime


def introducere_fisier():
    # introducem un fisier csv si il transformam in lita data
    data = []
    file = input("Introdu fisierul in care cauti \n").replace('& ', '').replace("'", "").replace('"', '')
    with open(file) as csvf:
        csvreader = csv.DictReader(csvf, delimiter=";")
        for rows in csvreader:
            data.append(rows)
    return data


def transformare_ora(data):
    # transformam data in formatul dorit
    c = 0
    for element in data:
        date_obj = datetime.strptime(element["Transaction Time"], "%d.%m.%Y %H:%M:%S")
        element["timpul"] = date_obj.strftime("%d %H:%M:%S")
        element["data"] = date_obj.strftime("%d ")
        # numaram rindurile
        c += 1
        element["count"] = c
    return element["Outlet"], element["CT"], element["data"]


def introducere_ora(outlet, ct, data):
    # introducem ora evenimentului dorit in format %H:%M:%S
    data = int(data)-1
    print("Locatia: ", outlet)
    print('Data de: ', data)
    print("Aparat: ", ct)
    timp1 = input("Introdu timpul de inceput ->")
    # adaugam 0 la datele mai mici de 10
    timp2 = int(timp1[0])
    if timp2 == 0:
        data += 1
    if data <= 9:
        data = "0", str(data)
    else:
        data = str(data)
    timp = data + " " + timp1
    print('TIMP INTRODUS: ', timp, '\n')
    return timp


def cautare_sesiune(data, timp):
    # cautam sesiune de joc
    joc = 0
    t_1 = timp
    t_2 = timp
    for element in data:

        if timp < element["timpul"] and joc == 0:

            if "Remote-In" in element["Action"]:
                print(element["Action"], ",", element["timpul"])
                t_1 = element["timpul"]
                for element in data:
                    if t_1 < element["timpul"] and joc == 0:
                        if "Handpay" in element["Action"]:
                            print(element["Action"], ",", element["timpul"])
                            t_2 = element["timpul"]
                            joc = 1
                        elif "Remote-In" in element["Action"]:
                            print(element["Action"], ",", element["timpul"])
                            t_2 = element["timpul"]
                            a = element["count"] - 1
                            for element in data:
                                if a == element["count"]:
                                    print("Evenimentul precedent: ", element["Credits"], ", ", element["Action"],
                                          ", ", element["timpul"])
                            joc = 1
                        elif "End of Business Day" in element["Action"]:
                            print("Jucatorul a jucat toti banii: ", element["Action"], ", ", element["timpul"])
                            t_2 = element["timpul"]
                            a = element["count"] - 1
                            for element in data:
                                if a == element["count"]:
                                    print("Evenimentul precedent este:  ", element["Credits"], ", ",
                                          element["Action"], ", ", element["timpul"])
                            joc = 1
    return t_1, t_2


def numar_joc(data, t1, t2):
    # numaram cite jocuri sau efectuat
    numar_jocuri = 0
    for element in data:
        if (t1 < element["timpul"]) and (t2 > element["timpul"]):
            if "Game-Start" in element["Action"]:
                numar_jocuri += 1
    print("Numarul de jocuri jucate: ", numar_jocuri)


def nume_joc(data, t1, t2):
    # verificam in care jocuri sa jucat
    nume_j = []
    for element in data:
        if (t1 < element["timpul"]) and (t2 > element["timpul"]):
            if "Game-Start" in element["Action"]:
                description = element["Description"].replace("Game:", ", ")
                if description not in nume_j:
                    nume_j.append(description)
    print("Jocuri jucate: ", *nume_j)


def mizaj(data, t1, t2):
    # verificam pe ce mize sa jucat
    miza = []
    for element in data:
        if (t1 < element["timpul"]) and (t2 > element["timpul"]):
            if "Game-Start" in element["Action"]:
                mize = element["Amount"].replace(",00", "").replace("-", ", ")
                if mize not in miza:
                    miza.append(mize)
                    miza.sort()
    print("Mizele jucate: ", *miza)
