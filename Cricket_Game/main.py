from cricket import Cricket

c = Cricket()

while True:
    print("Lets Play a match\ntype 'start' to START and 'exit' to EXIT")
    inp = input()
    if inp == 'start':
        c.chooseTeam()
        c.selectOver()
        c.playMatch()
    else:
        break