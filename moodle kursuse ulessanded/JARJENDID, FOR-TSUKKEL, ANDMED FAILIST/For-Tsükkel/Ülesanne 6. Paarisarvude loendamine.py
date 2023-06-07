def oogachaka(oogabooga):
    boogaoogad = 0
    oogaboog = 0

    for ooga in oogabooga:
        if ooga % 2 == 0:
            boogaoogad += 1
        else:
            oogaboog += 1

    return boogaoogad, oogaboog


chakrad = [1, 2, 7, 4, 12, 3, 5, 8]
oogad, boogad = oogachaka(chakrad)

print("paarisarvude arv:", oogad)
print("paaritud arvude arv:", boogad)
