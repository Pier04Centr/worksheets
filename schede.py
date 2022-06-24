import random as r
from secrets import choice


allenamento = []
n_ess = 4
reps = [8,6,10]


def fondamentale(linee):
    x=linee[r.randint(0, len(linee)-1)]
    while ("*" in x) == False:
        x=linee[r.randint(0, len(linee)-1)]
    return x.replace("*","") 


def normale():
    global allenamento
    for i in range(g):
        allenamento.append("giorno " + str(i+1))
        for x in range(n_muscoli):
            allenamento.append("muscolo allenato: " + muscoli[x])
            with open (path + muscoli[x] + ".txt", "r") as f:
                linea = f.readlines()
                f.close()
            for _ in range(n_ess):
                all = (linea[r.randint(0, len(linea)-1)].replace("\n","")).replace("*","") + " reps : " + str(r.randint(3,4)) + " x " + str(choice(reps)) + " rec : 1.15"
                if all not in allenamento:
                    allenamento.append(all)
                else :
                    _ -=1
        for a in range(n_muscoli):
            muscoli.pop(0)

def superserie():
    global allenamento
    for i in range(g):
        allenamento.append("giorno " + str(i+1))
        for x in range(n_muscoli):
            allenamento.append("muscolo allenato: " + muscoli[x])
            superserie=True
            with open (path + muscoli[x] + ".txt", "r") as f:
                linea = f.readlines()
                f.close()
            for _ in range(n_ess):
                if superserie:
                    if muscoli[x] == "Petto" or muscoli[x] == "Dorso" or muscoli[x] == "Gambe":
                        all = "super serie con " + str(fondamentale(linea)).replace("\n","") + " e " + (linea[r.randint(0, len(linea)-1)].replace("\n","")).replace("*","") + " reps : " + str(r.randint(3,4)) + " x " + str(reps[r.randint(0,1)]) + " rec : 1.45"
                    else:
                        all = "super serie con " + (linea[r.randint(0, len(linea)-1)].replace("\n","")).replace("*","") + " e " + (linea[r.randint(0, len(linea)-1)].replace("\n","")).replace("*","") + " reps : " + str(r.randint(3,4)) + " x " + str(choice(reps)) + " rec : 1.15"
                    superserie=False
                else:
                    all = (linea[r.randint(0, len(linea)-1)].replace("\n","")).replace("*","") + " reps : " + str(r.randint(3,4)) + " x " + str(choice(reps)) + " rec : 1.15"
                if all not in allenamento:
                    allenamento.append(all)
                else :
                    _ -=1
        for a in range(n_muscoli):
            muscoli.pop(0)

def forza():
    global allenamento
    for i in range(g):
        allenamento.append("giorno " + str(i+1))
        for x in range(n_muscoli):            
            allenamento.append("muscolo allenato: " + muscoli[x])
            if muscoli[x] == "Petto" or muscoli[x] == "Dorso" or muscoli[x] == "Gambe":
                forza = True
            with open (path + muscoli[x] + ".txt", "r") as f:
                linea = f.readlines()
                f.close()
            for _ in range(n_ess):
                if forza:
                    fond = fondamentale(linea)
                    all = str(fond).replace("\n","") + " reps : 10 - 8 - 6 - 4 - 1 rec : 1.30 - 1.30 - 1.45 - 1.45 - 2.30"
                    forza=False
                else:
                    all = (linea[r.randint(0, len(linea)-1)].replace("\n","")).replace("*","") + " reps : " + str(r.randint(3,4)) + " x " + str(choice(reps)) + " rec : 1.15"
                if all not in allenamento:
                    allenamento.append(all)
                else :
                    _ -=1
        for a in range(n_muscoli):
            muscoli.pop(0)


def rest():
    global allenamento
    for i in range(g):
        allenamento.append("giorno " + str(i+1))
        for x in range(n_muscoli):            
            allenamento.append("muscolo allenato: " + muscoli[x])
            if muscoli[x] == "Petto" or muscoli[x] == "Dorso" or muscoli[x] == "Gambe":
                rest = True
            with open (path + muscoli[x] + ".txt", "r") as f:
                linea = f.readlines()
                f.close()
            for _ in range(n_ess):
                if rest:
                    fond = fondamentale(linea)
                    rep = str(choice([8,6]))
                    all = str(fond).replace("\n","") + " reps : 3 x (" + rep + "-" + rep + "-" + rep + ") rec : 20/30sec tra una serie e l'altra 1.15"
                    rest=False
                else:
                    all = (linea[r.randint(0, len(linea)-1)].replace("\n","")).replace("*","") + " reps : " + str(r.randint(3,4)) + " x " + str(choice(reps)) + " rec : 1.15"
                if all not in allenamento:
                    allenamento.append(all)
                else :
                    _ -=1
        for a in range(n_muscoli):
            muscoli.pop(0)

g = int(input("inserici il numero di giorni: "))

while g <=1 or g >4:
    g = int(input("il numero di giorni deve essere maggiore di 1 e minore di 5\ninserici il numero di giorni: "))

n_muscoli = int(6 / g)
if g == 2:
    muscoli = [
        "Petto",
        "Bicipiti",
        "Spalle",
        "Gambe",
        "Dorso",    
        "Tricipiti"
    ]
elif g == 3:
    muscoli = [
        "Petto",
        "Bicipiti",
        "Gambe",
        "Spalle",
        "Dorso",    
        "Tricipiti"
    ]
else:
    m=input("inserisci il tuo muscolo carente: ").capitalize()
    muscoli = [
        "Petto",
        "Bicipiti",
        "Gambe",
        "Spalle",
        "Dorso",    
        "Tricipiti",
        "Gambe",
    ]
    while m not in muscoli or m == "Gambe":
        m = input("muscolo non valido\ninserisci il tuo muscolo carente: ").capitalize()
    muscoli.append(m)
    n_muscoli = 2


path = "./esercizi/"
while True:
    try:
        scelta = int(input("scegli il tipo di allenamento \n 1. normale \n 2. con superserie \n 3. rest pause \n 4. forza \n"))
    except:
        print("inserisci un numero")
    break

if scelta == 1:
    normale()
elif scelta == 2:
    superserie()
elif scelta == 3:
    rest()
else:
    forza()

with open(path +"Addominali.txt", "r") as f:
    linee = f.readlines()
    f.close()

allenamento.append("Addome tutti i giorni")
for i in range(3):
    allenamento.append(linee[r.randint(0, len(linee)-1)].replace("\n","") + " reps : " + str(r.randint(3,4)) + " x " + str(choice(reps)) + " rec : 1:00")

for z in allenamento:
    print(z)

input("")