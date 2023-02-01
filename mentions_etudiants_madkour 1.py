
def resultats(nombre):

    import numpy as np

    np.random.seed(0)

    notes = np.random.randint(low=0, high=20, size=nombre, dtype=int)

    etudiants = [ 'etudiant_' + str(i+1) for i in range(len(notes)) ]

    favorables = { etudiant : note for etudiant , note in zip(etudiants , notes) if note >= 10 }

    defavorables = { etudiant : note for etudiant , note in zip(etudiants , notes) if note < 10 }

    mentions = {}

    for etudiant in favorables.keys():
        if ( favorables[etudiant] >= 10 ) & ( favorables[etudiant] < 12 ):
            mentions[etudiant] = 'Passable'
        elif ( favorables[etudiant] >= 12 ) & ( favorables[etudiant] < 14 ):
            mentions[etudiant] = 'Assez bien'
        elif ( favorables[etudiant] >= 14 ) & ( favorables[etudiant] < 16 ):
            mentions[etudiant] = 'Bien'
        elif ( favorables[etudiant] >= 16 ) & ( favorables[etudiant] < 18 ):
            mentions[etudiant] = 'Très bien'
        else:
            mentions[etudiant] = 'Excellent'
        
    return mentions

mention = resultats(20)

print(mention)
