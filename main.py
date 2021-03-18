def main():
    investInit = float(input("Entrer le montant d'argent à investir"))
    rendement = float(input("Entrer le rendement annuel"))
    time = float(input("Entrer le rendement annuel"))
    tempTime = time
    annualInvest = investInit
    while (tempTime > 0):
        annualInvest = annualInvest *(1 + rendement/1/100)
        tempTime -= 1
    print("resultat annuel : ", investInit)