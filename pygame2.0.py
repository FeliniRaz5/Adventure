import random
import time
from colored import *
import sys

sys.setrecursionlimit(10**6)

mf_color = fg('green')
mf_color2 = fg('yellow')
mf_color3 = fg('chartreuse_2b')
logo_color1 = fg('light_goldenrod_1')
logo_color2 = fg('yellow_1')
logo_color3 = fg('gold_1')
logo_color4 = fg('orange_1')
logo_color5 = fg('dark_orange')
logo_color6 = fg('orange_red_1')
logo_color7 = fg('red_1')

current_lvl = 0
time1 = 0.0
time_now = time.time()
cash = 0

def show_world():
    global current_lvl
    if current_lvl == 1:
        print("Area 1: " + mf_color + "Forest")
    elif current_lvl == 5:
        print(attr('reset') + "Area 2: City")
    elif current_lvl == 15:
        print("Area 3: " + mf_color2 + "Desert")
    elif current_lvl == 34:
        print(attr('reset') + "Area 4: " + mf_color3 + "Field")

def logo():
    print(logo_color1 + '    :::     :::::::::  :::     ::: :::::::::: ::::    ::: ::::::::::: :::    ::: :::::::::  :::::::::: ')
    time.sleep(0.35)
    print(logo_color2 + '  :+: :+:   :+:    :+: :+:     :+: :+:        :+:+:   :+:     :+:     :+:    :+: :+:    :+: :+:        ')
    time.sleep(0.35)
    print(logo_color3 + ' +:+   +:+  +:+    +:+ +:+     +:+ +:+        :+:+:+  +:+     +:+     +:+    +:+ +:+    +:+ +:+        ')
    time.sleep(0.35)
    print(logo_color4 + '+#++:++#++: +#+    +:+ +#+     +:+ +#++:++#   +#+ +:+ +#+     +#+     +#+    +:+ +#++:++#:  +#++:++#   ')
    time.sleep(0.35)
    print(logo_color5 + '+#+     +#+ +#+    +#+  +#+   +#+  +#+        +#+  +#+#+#     +#+     +#+    +#+ +#+    +#+ +#+        ')
    time.sleep(0.35)
    print(logo_color6 + '#+#     #+# #+#    #+#   #+#+#+#   #+#        #+#   #+#+#     #+#     #+#    #+# #+#    #+# #+#        ')
    time.sleep(0.35)
    print(logo_color7 + '###     ### #########      ###     ########## ###    ####     ###      ########  ###    ### ########## 1.0.10')
    time.sleep(0.35)
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
        print('▓ = wall; ▣ = you, the player; □ = door; $ = money (you can collect it)')
        start()
    else:
        print('Error: ' + startq + ' is not a valid answer')
        start()

def level1(wq, hq):
    layers = []
    ip = []
    moneylist = []

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
                    x2 = random.randrange(7)
                    if x2 == 6:
                        lr += '$'
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
                    x2 = random.randrange(7)
                    if x2 == 6:
                        lr += '$'
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
                    x2 = random.randrange(7)
                    if x2 == 6:
                        lr += '$'
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
            elif j in '$':
                moneylist += [posy]
                moneylist += [posx]
            posx += 1
        posy += 1
    
    testlevel(ip, layers, wq, hq, moneylist)

def testlevel(ip, layers, wq, hq, moneylist):
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
        moving(ip, layers, wq, hq, moneylist)
    else:
        level1(wq, hq)
        
    
def moving(ip, layers, wq, hq, moneylist):
    global current_lvl
    global time1
    global time_now
    global cash
    current_lvl += 1
    show_world()
    print('info:')
    time1 = time.time() - time_now
    print('Level: ' + str(current_lvl) + ', Time: ' + str(int(time1)) + ', Cash: ' + str(float(cash)) + '$')
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

        for i in range(len(moneylist)):
            if moneylist[i] == posy and i % 2 == 0:
                if moneylist[i + 1] == posx:
                    cash += 1
                    moneylist[i] = -2
                    moneylist[i + 1] = -2
            

        if posy != 0:
            counter = -1
            for i in layers[1]:
                if i == '▣':
                    layers_mod[0] += ' '
                elif i == '$':
                    posym = 0
                    posxm = counter
                    for j in range(len(moneylist)):
                        if moneylist[j] == posym and j % 2 == 0:
                            if moneylist[j + 1] == posxm:
                                layers_mod[0] += i
                                break
                    else:
                        layers_mod[0] += ' '
                                                      
                else:
                    layers_mod[0] += i
                counter += 1

        if posy == 0:
            counter = -1
            for i in layers[posy + 1]:
                if counter == posx:
                    layers_mod[posy + 1] += '▣'
                else:
                    if i == '▣':
                        layers_mod[posy + 1] += ' '

                    elif i == '$':
                        posym = 0
                        posxm = counter
                        for j in range(len(moneylist)):
                            if moneylist[j] == posym and j % 2 == 0:
                                if moneylist[j + 1] == posxm:
                                    layers_mod[posy + 1] += i
                                    break
                        else:
                            layers_mod[posy + 1] += ' '
                    
                    else:
                        layers_mod[posy + 1] += i
                counter += 1
                
            for i in range(hq):
                if posy == i:
                    continue
                else:
                    if i == 0:
                        layers_mod[i + 1] = layers_mod[0]
                    else:
                        counter = -1
                        for k in layers[i + 1]:
                            if k == '$':
                                posym = i
                                posxm = counter
                                for j in range(len(moneylist)):
                                    if moneylist[j] == posym and j % 2 == 0:
                                        if moneylist[j + 1] == posxm:
                                            layers_mod[i + 1] += k
                                            break
                                else:
                                    layers_mod[i + 1] += ' '
                    
                            else:
                                layers_mod[i + 1] += k
                            counter += 1



        else:
            counter = -1
            for i in layers[posy + 1]:
                if counter == posx:
                    layers_mod[posy + 1] += '▣'
                else:
                    if i == '$':
                        posym = posy
                        posxm = counter
                        for j in range(len(moneylist)):
                            if moneylist[j] == posym and j % 2 == 0:
                                if moneylist[j + 1] == posxm:
                                    layers_mod[posy + 1] += i
                                    break
                        else:
                            layers_mod[posy + 1] += ' '
                    
                    else:
                        layers_mod[posy + 1] += i
                counter += 1

            for i in range(hq):
                if posy == i:
                    continue
                else:
                    if i == 0:
                        layers_mod[i + 1] = layers_mod[0]
                    else:
                        counter = -1
                        for k in layers[i + 1]:
                            if k == '$':
                                posym = i
                                posxm = counter
                                for j in range(len(moneylist)):
                                    if moneylist[j] == posym and j % 2 == 0:
                                        if moneylist[j + 1] == posxm:
                                            layers_mod[i + 1] += k
                                            break
                                else:
                                    layers_mod[i + 1] += ' '
                    
                            else:
                                layers_mod[i + 1] += k
                            counter += 1

        
        if info == False:
            print('info:')
            
        time1 = time.time() - time_now
        print('Level: ' + str(current_lvl) + ', Time: ' + str(int(time1)) + ', Cash: ' + str(float(cash)) + '$')

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
