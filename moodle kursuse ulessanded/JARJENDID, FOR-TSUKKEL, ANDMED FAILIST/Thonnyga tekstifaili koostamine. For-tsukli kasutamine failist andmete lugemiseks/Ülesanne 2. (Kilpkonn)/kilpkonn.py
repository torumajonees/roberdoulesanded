# henripaul
import turtle


def juhised(oogabooga):  # avab kilpkonna.txt faili
    oogachaga = []
    with open(oogabooga, 'r') as booga:
        for rida in booga:
            command = rida.strip().split(' ')
            oogachaga.append(command)
    return oogachaga


def joonistab(chagataga, oogabooga):  # kilpkonna.txt tolgib loetavaks koodiks
    for command in chagataga:
        if command[0] == 'edasi':
            turtle.forward(int(command[1]))
        elif command[0] == 'tagasi':
            turtle.backward(int(command[1]))
        elif command[0] == 'paremale':
            turtle.right(int(command[1]))
        elif command[0] == 'vasakule':
            turtle.left(int(command[1]))


chaga = int(input("mitu korda kujundit joonistada? "))  # kusib mitu korda kujundit joonistada
ooga = juhised('kilpkonn.txt')

boogaooga = turtle.Turtle()
turtle.shape("turtle")
turtle.color("green")
turtle.speed(0)


for ooganen in range(chaga):
    joonistab(ooga, turtle)

turtle.exitonclick()
