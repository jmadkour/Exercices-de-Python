

def resultats(nombre):

    # importer numper
    import numpy as np
    np.random.seed(0)

 

    # simuler les notes et les stocker dans la liste notes

    notes = list( np.random.randint(low=0, high=20, size=nombre, dtype=int) )

    # créer la liste des étudiants

    etudiants = [ "etudiant_%d"%(i+1) for i in range(nombre) ]

    # initialisation des dictionnaires favorables et defavorables

    favorables = {etudiant : note for etudiant , note in zip(etudiants, notes) if note >= 10}

    defavorables = {etudiant : note for etudiant , note in zip(etudiants, notes) if note < 10}

    # Initailiser le dictionnaire mentions

    mentions = {}

    for etudiant in favorables.keys():
        if 10 <= favorables[etudiant] < 12 :
            mentions[etudiant] = "Passable"
        elif 12 <= favorables[etudiant] < 14 :
            mentions[etudiant] = "Assez bien"
        elif 14 <= favorables[etudiant] < 16 :
            mentions[etudiant] = "Bien"
        elif 16 <= favorables[etudiant] < 18 :
            mentions[etudiant] = "Très bien"
        else:
            mentions[etudiant] = "Excellent"

    return mentions


# Test de la fonction resultats(nombre)

les_mentions = resultats(10)

print('Les mentions obtenues par les étudiants : ' , les_mentions)


