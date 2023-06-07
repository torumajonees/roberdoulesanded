# henripaul
ooganen = open("sammud.txt", 'r')
oogachaga = ooganen.read()
booga = oogachaga.split()
booga = [int(ooga) for ooga in booga]
booga.sort()
oooga = booga[0]
boooga = booga[-1]
print("nadalas suurim sammude arv:", oooga)
print("nadala vaikseim sammude arv:", boooga)
