def on_dict():
    #h = {}
    #h = dict()
    #h.keys() renvoie un itérable en python3 alors que c'est une liste en python2
    #h.values() renvoie un itérable en python3
    #h.items() renvoie un tuple clé/valeuren python3

    h = {'nom': 'Last name', 'prenom': 'Surname'}
    h['age'] = '?'
    h['prenom'] = '*'
    del h['age']
    #h['taille'] renvoie error
    #h.get('taille') renvoie None
    #h.get('taille', 172) renvoie une valeur par défaut
    for key, value in h.items():
        print(key, value)
    for item in h.items():
        print(item[0], item[1])
    a, b = {'toto': 1, 'titi' : 2}
    #a = toto, b = titi
    c, d = {'toto': 1, 'titi' : 2}.items()
    #a = (toto, 1) b = (titi, 2)
    #for i, ville in enumerate
    #zip parcours de plusieurs listes for q, a in zip(questions, answers)
    #zip renvoie un tuple et prend en entrée des itérables de même taille