import numpy as np
np.random.seed(0)
def resultats(nombre):
    notes=np.random.randint(0,20,nombre,int)
    etudiants=[]
    for i in range (1,nombre+1):
        etudiants.append("Etudiant_%d"%i)
    
    favorables={}
    defavorables ={}  
    mentions={} 

    for i in range(nombre):
        if notes[i]>=10:
            favorables[etudiants[i]]=notes[i]
        else:
            defavorables[etudiants[i]]=notes[i]

    for i in range(nombre):
        if notes[i]>=10 and notes[i]<12:
            mentions[etudiants[i]]="passable"
        elif notes[i]>=12 and notes[i]<14:
            mentions[etudiants[i]]="Assez bien"
        elif notes[i]>=14 and notes[i]<16:
            mentions[etudiants[i]]="Bien"
        elif notes[i]>=16 and notes[i]<18:
            mentions[etudiants[i]]="Très bien" 
        elif notes[i]>=18:
            mentions[etudiants[i]]="Excellent" 

    print("Etudiants = ",etudiants)       
    print()
    print("Notes = ",notes)       
    print()
    print("Favorables = ",favorables)
    print()
    print("Defavorables = ",defavorables)
    print()
    print("Mentions = ",mentions)

resultats(15)

