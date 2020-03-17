import json, random, copy

def make_match(surname, person):
    with open("names.json") as f:
        family = json.load(f)
    family_tmp = copy.deepcopy(family)  

    potential_recievers = []
    if surname == "family_surname_one":
        for family_name, name in family.items():
            if family_name != surname:
                for firstname, email in name.items():
                    potential_recievers.append([firstname, family_name])
    elif surname == "family_surname_two":
        for family_name, name in family.items():
            if family_name != surname:
                for firstname, email in name.items():
                    potential_recievers.append([firstname, family_name])
    else:
        for family_name, name in family.items():
            if family_name != surname:
                for firstname, email in name.items():
                    potential_recievers.append([firstname, family_name])
    reciever = random.choice(potential_recievers)

    for family_name, name in family.items():
        if family_name == reciever[1]:
            for firstname, email in name.items():
                if firstname == reciever[0]:
                    del family_tmp[family_name][firstname]
    with open('names.json', 'w') as f:
        data = json.dump(family_tmp, f)
    
    return reciever
