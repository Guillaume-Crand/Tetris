import json

data = {
    "joueur1": {
        "record": {"niveau": 7, "ligne casse": 9, "temps": 850, "points": 10000},
        "derniere partie": {
            "niveau": 3,
            "ligne casse": 9,
            "temps": 850,
            "points": 10000,
        },
        "stats overall": {"ligne casse": 445, "temps": 850, "points": 10000},
    },
    "joueur2": {
        "record": {"niveau": 3, "ligne casse": 9, "temps": 850, "points": 10000},
        "derniere partie": {
            "niveau": 3,
            "ligne casse": 9,
            "temps": 850,
            "points": 10000,
        },
        "stats overall": {"ligne casse": 445, "temps": 850, "points": 10000},
    },
    "joueur3": {
        "record": {"niveau": 3, "ligne casse": 9, "temps": 850, "points": 10000},
        "derniere partie": {
            "niveau": 3,
            "ligne casse": 9,
            "temps": 850,
            "points": 10000,
        },
        "stats overall": {"ligne casse": 445, "temps": 850, "points": 10500},
    },
    "joueur4": {
        "record": {"niveau": 3, "ligne casse": 9, "temps": 850, "points": 10470},
        "derniere partie": {"niveau": 3, "ligne casse": 9, "temps": 850, "points": 100},
        "stats overall": {"ligne casse": 445, "temps": 850, "points": 10540},
    },
}


# écrit le dictionnaire contenant toutes les stats dans un fichier json
def ecriture_data(dico):
    with open("json/data.json", "w", encoding="utf-8") as f:
        json.dump(dico, f, indent=4)


def creation_data(dico):
    # sauvegarde de la dernière partie
    for joueur in dico.keys():
        for clefs, valeurs in dico[joueur]["derniere partie"].items():
            data[joueur]["derniere partie"][clefs] = valeurs

            # addition des stats
            try:
                data[joueur]["stats overall"][clefs] += valeurs
            except:
                pass
            # gestion du record
            if data[joueur]["derniere partie"][clefs] > data[joueur]["record"][clefs]:
                data[joueur]["record"][clefs] = valeurs


test = {
    "joueur4": {
        "derniere partie": {
            "niveau": 18,
            "ligne casse": 28,
            "temps": 152993,
            "points": 259520,
        }
    }
}


def lecture_data_record(dico):
    with open("json/data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        txt = str(data_dict["joueur1"]["record"])
        return "Joueur 1: " + txt


def lecture_data_record2(dico):
    with open("json/data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        txt2 = str(data_dict["joueur2"]["record"])
        return "Joueur 2: " + txt2


def lecture_data_lastgame(dico):
    with open("json/data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        txt = str(data_dict["joueur1"]["derniere partie"])
        return "Joueur 1: " + txt


def lecture_data_lastgame2(dico):
    with open("json/data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        txt2 = str(data_dict["joueur2"]["derniere partie"])
        return "Joueur 2: " + txt2


def lecture_data_overall(dico):
    with open("json/data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        txt = str(data_dict["joueur1"]["stats overall"])
        return "Joueur 1: " + txt


def lecture_data_overall2(dico):
    with open("json/data.json", "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        txt2 = str(data_dict["joueur2"]["stats overall"])
        return "Joueur 2: " + txt2


creation_data(test)
ecriture_data(data)
lecture_data_record(data)
lecture_data_lastgame(data)
lecture_data_overall(data)
lecture_data_record2(data)
lecture_data_lastgame2(data)
lecture_data_overall2(data)
