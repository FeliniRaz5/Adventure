import random
import time
from colored import *
import sys

sys.setrecursionlimit(10**6)

mf_color = fg('green')
current_lvl = 0
time1 = 0.0
time_now = time.time()
time.gmtime(0)

def show_world():
    global current_lvl
    if current_lvl == 1:
        print("Area 1: " + mf_color + "Forest")
    elif current_lvl == 5:
        print(attr('reset') + "Area 2: City")

def logo():
    print(mf_color + '                          /$$$$$$  /$$          ')
    print('                         /$$__  $$|__/          ')
    time.sleep(0.35)
    print(' /$$$$$$/$$$$   /$$$$$$ | $$  \__/ /$$  /$$$$$$ ')
    time.sleep(0.35)
    print('| $$_  $$_  $$ |____  $$| $$$$    | $$ |____  $$')
    time.sleep(0.35)
    print('| $$ \ $$ \ $$  /$$$$$$$| $$_/    | $$  /$$$$$$$')
    time.sleep(0.35)
    print('| $$ | $$ | $$ /$$__  $$| $$      | $$ /$$__  $$')
    time.sleep(0.35)
    print('| $$ | $$ | $$|  $$$$$$$| $$      | $$|  $$$$$$$')
    time.sleep(0.35)
    print('|__/ |__/ |__/ \_______/|__/      |__/ \_______/1.0.7')
    start()

def start():
    startq = input(attr('reset') + 'Do you want to start the game (y/n/info)? ')
    
    if startq == 'y':
        wq = int(input('Level width: '))
        hq = int(input('Level height: '))
        print('loading area... this may take a few seconds')
        level1(wq, hq)
    elif startq == 'n':
        quit()
    elif startq == 'info':
        print('▓ = wall; ▣ = you, the player; □ = door')
        start()
    else:
        print('Error: ' + startq + ' is not a valid answer')
        start()

def level1(wq, hq):
    layers = []
    ip = []

    for i in range(hq + 2):
        if i == 0 or i == hq + 1:
            lr = ''
            for i in range(wq + 2):
                lr += '▓'
            layers.append(lr)

        elif i == 1:
            lr = '▓▣'
            for j in range(wq - 1):
                x = random.randrange(2)
                if x == 1:
                    lr += '▓'
                else:
                    lr += ' '
            lr += '▓'
            layers.append(lr)

        elif i > 1 and i < hq:
            lr = '▓'
            for j in range(wq):
                x = random.randrange(2)
                if x == 1:
                    lr += '▓'
                else:
                    lr += ' '
            lr += '▓'
            layers.append(lr)
        elif i == hq:    
            lr = '▓'
            for j in range(wq):
                x = random.randrange(2)
                if x == 1:
                    lr += '▓'
                else:
                    lr += ' '
            lr += '□'
            layers.append(lr)
        
    posy = -1
    for i in range(hq + 2):
        posx = -1
        for j in layers[i]:
            if j in '▓':
                ip += [posy]
                ip += [posx]
            posx += 1
        posy += 1
                
    testlevel(ip, layers, wq, hq)

def testlevel(ip, layers, wq, hq):
    posy_undo = None
    posx_undo = None
    posy = 0
    posx = 0
    complete = False
    
    for t in range(9 * hq * wq):
        m = random.randrange(3)
        if m == 0:
            posy_undo = posy
            posy -= 1
            
        elif m == 1:
            posy_undo = posy
            posy += 1
            
        elif m == 2:
            posx_undo = posx
            posx += 1
            
        elif m == 3:
            posx_undo = posx
            posx -= 1

        for i in range(len(ip)):
            if ip[i] == posy and i % 2 == 0:
                if ip[i + 1] == posx:
                    if m == 0 or m == 1:
                        posy = posy_undo
                    elif m == 2 or m == 3:
                        posx = posx_undo

        if posy == hq - 1 and posx == wq:
            complete = True
            break
            
    if complete == True:
        moving(ip, layers, wq, hq)
    else:
        level1(wq, hq)
        
    
def moving(ip, layers, wq, hq):
    global current_lvl
    global time1
    global time_now
    current_lvl += 1
    show_world()
    print('info:')
    print('Level: ' + str(current_lvl) + ', Time: ' + str(int(time1)))
    for i in range(len(layers)):
        print(layers[i])
    layers_mod = [''] * len(layers)
    posy_undo = None
    posx_undo = None
    posy = 0
    posx = 0
    complete = False
    info = False

    while complete == False:
        moveq = input('Where do you want to move (a = left/d = right/w = up/s = down/r = reset)? ')
        if moveq == 'w':
            posy_undo = posy
            posy -= 1
            print('')
            
        elif moveq == 's':
            posy_undo = posy
            posy += 1
            print('')
            
        elif moveq == 'd':
            posx_undo = posx
            posx += 1
            print('')
            
        elif moveq == 'a':
            posx_undo = posx
            posx -= 1
            print('')

        elif moveq == 'r':
            current_lvl = 0
            logo()

        else:
            print('Error: ' + moveq + ' is not a valid answer')

        for i in range(len(ip)):
            if ip[i] == posy and i % 2 == 0:
                if ip[i + 1] == posx:
                    if moveq == 'w' or moveq == 's':
                        posy = posy_undo
                    elif moveq == 'd' or moveq == 'a':
                        posx = posx_undo
                    print('info: you can\'t move there!')
                    info = True

        if posy != 0:
            for i in layers[1]:
                if i == '▣':
                    layers_mod[0] += ' '
                else:
                    layers_mod[0] += i

        if posy == 0:
            counter = -1
            for i in layers[posy + 1]:
                if counter == posx:
                    layers_mod[posy + 1] += '▣'
                else:
                    if i == '▣':
                        layers_mod[posy + 1] += ' '
                    else:
                        layers_mod[posy + 1] += i
                counter += 1
                
            for i in range(hq):
                if posy + 1 == i + 1:
                    continue
                else:
                    if i + 1 == 1:
                        layers_mod[i + 1] = layers_mod[0]
                    else:
                        layers_mod[i + 1] = layers[i + 1]



        else:
            counter = -1
            for i in layers[posy + 1]:
                if counter == posx:
                    layers_mod[posy + 1] += '▣'
                else:
                    layers_mod[posy + 1] += i
                counter += 1
            for i in range(hq):
                if posy + 1 == i + 1:
                    continue
                else:
                    if i + 1 == 1:
                        layers_mod[i + 1] = layers_mod[0]
                    else:
                        layers_mod[i + 1] = layers[i + 1]

        
        if info == False:
            print('info:')
            
        time1 = time.time() - time_now
        print('Level: ' + str(current_lvl) + ', Time: ' + str(int(time1)))

        if posy == hq - 1 and posx == wq:
            complete = True

        print(layers[0])
        for i in range (1, hq + 1):
            print(layers_mod[i])
        print(layers[0])
        layers_mod = [''] * len(layers)
        info = False
    print('loading area... this may take a few seconds')
    for i in range(13):
        print('')
    level1(wq, hq)
                
logo()
