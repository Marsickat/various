import json

MODE = "pve"  # "pve" or "pvp"
TYPE = "Shooter"  # "Guardian" or "Shooter" or "Carrier"

with open("ants.json", encoding="utf-8") as f:
    data = json.load(f)
    lst_Splus, lst_S, lst_Aplus, lst_A, lst_Bplus, lst_B, lst_Cplus, lst_C, lst_Dplus, lst_D, lst_F = [], [], [], [], [], [], [], [], [], [], []
    for ant in data:
        for name, chars in ant.items():
            for c in chars:
                if c["available"]:
                    if c["type"] == TYPE or c["type"] == "Universal":
                        if c[MODE] == "S+":
                            lst_Splus.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "S":
                            lst_S.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "A+":
                            lst_Aplus.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "A":
                            lst_A.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "B+":
                            lst_Bplus.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "B":
                            lst_B.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "C+":
                            lst_Cplus.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "C":
                            lst_C.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "D+":
                            lst_Dplus.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "D":
                            lst_D.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
                        elif c[MODE] == "F":
                            lst_F.append(f"{c['translate']}, {c['skill_1']}-{c['skill_2']}-{c['skill_3']}")
print(lst_Splus, lst_S, lst_Aplus, lst_A, lst_Bplus, lst_B, lst_Cplus, lst_C, lst_Dplus, lst_D, lst_F, sep="\n")
