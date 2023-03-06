#henripaul
with open("sammud.txt", "r") as booga: #avab tekstifaili "sammud.txt"
    ooga = [int(line.strip()) for line in booga]
oogabooga = sum(ooga) #liidab koik numbrid
print (oogabooga) #edastab liidetud numbrid