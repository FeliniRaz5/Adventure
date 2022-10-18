import random
import time
from colored import *
import sys

sys.setrecursionlimit(10**6)

mf_color = fg('green')
current_lvl = 0

def show_world():
    global current_lvl
    if current_lvl == 1:
        print("Area 1: " + mf_color + "Forest")
    elif current_lvl == 5:
        print(attr('reset') + "Area 2: City")

def logo():
    print(mf_color + '                          /$$$$$$  /$$          ')
    print('                         /$$__  $$|__/          ')
    time.sleep(0.5)
    print(' /$$$$$$/$$$$   /$$$$$$ | $$  \__/ /$$  /$$$$$$ ')
    time.sleep(0.5)
    print('| $$_  $$_  $$ |____  $$| $$$$    | $$ |____  $$')
    time.sleep(0.5)
    print('| $$ \ $$ \ $$  /$$$$$$$| $$_/    | $$  /$$$$$$$')
    time.sleep(0.5)
    print('| $$ | $$ | $$ /$$__  $$| $$      | $$ /$$__  $$')
    time.sleep(0.5)
    print('| $$ | $$ | $$|  $$$$$$$| $$      | $$|  $$$$$$$')
    time.sleep(0.5)
    print('|__/ |__/ |__/ \_______/|__/      |__/ \_______/1.0.6')
    print(attr('reset') + 'resize your window to be 13 characters heigh!')
    start()

def start():
    startq = input('Do you want to start the game (y/n/info)? ')
    
    if startq == 'y':
        print('loading area... this may take a few seconds')
        level1()
    elif startq == 'n':
        quit()
    elif startq == 'info':
        print('▓ = wall; ▣ = you, the player; □ = door')
        start()
    else:
        print('Error: ' + startq + ' is not a valid answer')
        start()

def level1():
#          10123456789
    lr1 = '▓▓▓▓▓▓▓▓▓▓▓'#1
    lr2 = '▓▣'#         0
    lr3 = '▓'#          1
    lr4 = '▓'#          2
    lr5 = '▓'#          3
    lr6 = '▓'#          4
    lr7 = '▓'#          5
    lr8 = '▓'#          6
    lr9 = '▓'#          7
    lr10 ='▓'#          8
    lr11 ='▓▓▓▓▓▓▓▓▓▓▓'#9
    ip = []
    for i in range(9):
        if i == 0:
            for j in range(8):
                x = random.randrange(2)
                if x == 1:
                    lr2 += '▓'
                else:
                    lr2 += ' '
            lr2 += '▓'
            
        elif i == 1:
            for j in range(9):
                x = random.randrange(2)
                if x == 1:
                    lr3 += '▓'
                else:
                    lr3 += ' '
            lr3 += '▓'
            
        elif i == 2:
            for j in range(9):
                x = random.randrange(2)
                if x == 1:
                    lr4 += '▓'
                else:
                    lr4 += ' '
            lr4 += '▓'

        elif i == 3:
            for j in range(9):
                x = random.randrange(2)
                if x == 1:
                    lr5 += '▓'
                else:
                    lr5 += ' '
            lr5 += '▓'

        elif i == 4:
            for j in range(9):
                x = random.randrange(2)
                if x == 1:
                    lr6 += '▓'
                else:
                    lr6 += ' '
            lr6 += '▓'

        elif i == 5:
            for j in range(9):
                x = random.randrange(2)
                if x == 1:
                    lr7 += '▓'
                else:
                    lr7 += ' '
            lr7 += '▓'

        elif i == 6:
            for j in range(9):
                x = random.randrange(2)
                if x == 1:
                    lr8 += '▓'
                else:
                    lr8 += ' '
            lr8 += '▓'

        elif i == 7:
            for j in range(9):
                x = random.randrange(2)
                if x == 1:
                    lr9 += '▓'
                else:
                    lr9 += ' '
            lr9 += '▓'

        elif i == 8:
            for j in range(9):
                x = random.randrange(2)
                if x == 1:
                    lr10 += '▓'
                else:
                    lr10 += ' '
            lr10 += '□'
        
    for i in range(11):
        if i == 0:
            posy = -1
            posx = -1
            for j in lr1:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 1:
            posy = 0
            posx = -1
            for j in lr2:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 2:
            posy = 1
            posx = -1
            for j in lr3:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 3:
            posy = 2
            posx = -1
            for j in lr4:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 4:
            posy = 3
            posx = -1
            for j in lr5:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 5:
            posy = 4
            posx = -1
            for j in lr6:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 6:
            posy = 5
            posx = -1
            for j in lr7:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 7:
            posy = 6
            posx = -1
            for j in lr8:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 8:
            posy = 7
            posx = -1
            for j in lr9:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 9:
            posy = 8
            posx = -1
            for j in lr10:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1

        if i == 10:
            posy = 9
            posx = -1
            for j in lr11:
                if j in '▓':
                    ip += [posy]
                    ip += [posx]
                posx += 1
                
    testlevel(ip, lr1, lr2, lr3, lr4, lr5, lr6, lr7, lr8, lr9, lr10, lr11)

def testlevel(ip, lr1, lr2, lr3, lr4, lr5, lr6, lr7, lr8, lr9, lr10, lr11):
    posy_undo = None
    posx_undo = None
    posy = 0
    posx = 0
    complete = False
    
    for t in range(1000):
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

        if posy == 8 and posx == 9:
            complete = True
            break
            
    if complete == True:
        moving(ip, lr1, lr2, lr3, lr4, lr5, lr6, lr7, lr8, lr9, lr10, lr11)
    else:
        level1()
        
    
def moving(ip, lr1, lr2, lr3, lr4, lr5, lr6, lr7, lr8, lr9, lr10, lr11):
    global current_lvl
    current_lvl += 1
    show_world()
    print('info:')
    print('')
    print(lr1)
    print(lr2)
    print(lr3)
    print(lr4)
    print(lr5)
    print(lr6)
    print(lr7)
    print(lr8)
    print(lr9)
    print(lr10)
    print(lr11)
    lr2_mod = ''
    lr3_mod = ''
    lr4_mod = ''
    lr5_mod = ''
    lr6_mod = ''
    lr7_mod = ''
    lr8_mod = ''
    lr9_mod = ''
    lr10_mod = ''
    lr2_mod1 = ''
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
            for i in lr2:
                if i == '▣':
                    lr2_mod1 += ' '
                else:
                    lr2_mod1 += i
                                
        if posy == 0:
            counter = -1
            for i in lr2:
                if counter == posx:
                    lr2_mod += '▣'
                else:
                    if i == '▣':
                        lr2_mod += ' '
                    else:
                        lr2_mod += i
                counter += 1
            lr3_mod, lr4_mod, lr5_mod, lr6_mod, lr7_mod, lr8_mod, lr9_mod, lr10_mod = lr3, lr4, lr5, lr6, lr7, lr8, lr9, lr10

        elif posy == 1:
            counter = -1
            for i in lr3:
                if counter == posx:
                    lr3_mod += '▣'
                else:
                    lr3_mod += i
                counter += 1
            lr2_mod, lr4_mod, lr5_mod, lr6_mod, lr7_mod, lr8_mod, lr9_mod, lr10_mod = lr2_mod1, lr4, lr5, lr6, lr7, lr8, lr9, lr10

        elif posy == 2:
            counter = -1
            for i in lr4:
                if counter == posx:
                    lr4_mod += '▣'
                else:
                    lr4_mod += i
                counter += 1
            lr2_mod, lr3_mod, lr5_mod, lr6_mod, lr7_mod, lr8_mod, lr9_mod, lr10_mod = lr2_mod1, lr3, lr5, lr6, lr7, lr8, lr9, lr10

        elif posy == 3:
            counter = -1
            for i in lr5:
                if counter == posx:
                    lr5_mod += '▣'
                else:
                    lr5_mod += i
                counter += 1
            lr2_mod, lr3_mod, lr4_mod, lr6_mod, lr7_mod, lr8_mod, lr9_mod, lr10_mod = lr2_mod1, lr3, lr4, lr6, lr7, lr8, lr9, lr10

        elif posy == 4:
            counter = -1
            for i in lr6:
                if counter == posx:
                    lr6_mod += '▣'
                else:
                    lr6_mod += i
                counter += 1
            lr2_mod, lr3_mod, lr4_mod, lr5_mod, lr7_mod, lr8_mod, lr9_mod, lr10_mod = lr2_mod1, lr3, lr4, lr5, lr7, lr8, lr9, lr10

        elif posy == 5:
            counter = -1
            for i in lr7:
                if counter == posx:
                    lr7_mod += '▣'
                else:
                    lr7_mod += i
                counter += 1
            lr2_mod, lr3_mod, lr4_mod, lr5_mod, lr6_mod, lr8_mod, lr9_mod, lr10_mod = lr2_mod1, lr3, lr4, lr5, lr6, lr8, lr9, lr10

        elif posy == 6:
            counter = -1
            for i in lr8:
                if counter == posx:
                    lr8_mod += '▣'
                else:
                    lr8_mod += i
                counter += 1
            lr2_mod, lr3_mod, lr4_mod, lr5_mod, lr6_mod, lr7_mod, lr9_mod, lr10_mod = lr2_mod1, lr3, lr4, lr5, lr6, lr7, lr9, lr10

        elif posy == 7:
            counter = -1
            for i in lr9:
                if counter == posx:
                    lr9_mod += '▣'
                else:
                    lr9_mod += i
                counter += 1
            lr2_mod, lr3_mod, lr4_mod, lr5_mod, lr6_mod, lr7_mod, lr8_mod, lr10_mod = lr2_mod1, lr3, lr4, lr5, lr6, lr7, lr8, lr10

        elif posy == 8:
            counter = -1
            for i in lr10:
                if counter == posx:
                    lr10_mod += '▣'
                else:
                    lr10_mod += i
                counter += 1
            lr2_mod, lr3_mod, lr4_mod, lr5_mod, lr6_mod, lr7_mod, lr8_mod, lr9_mod = lr2_mod1, lr3, lr4, lr5, lr6, lr7, lr8, lr9

        if info == False:
            print('info:')

        print('')

        if posy == 8 and posx == 9:
            complete = True

        print(lr1)
        print(lr2_mod)
        print(lr3_mod)
        print(lr4_mod)
        print(lr5_mod)
        print(lr6_mod)
        print(lr7_mod)
        print(lr8_mod)
        print(lr9_mod)
        print(lr10_mod)
        print(lr11)
        lr2_mod = ''
        lr3_mod = ''
        lr4_mod = ''
        lr5_mod = ''
        lr6_mod = ''
        lr7_mod = ''
        lr8_mod = ''
        lr9_mod = ''
        lr10_mod = ''
        lr2_mod1 = ''
        info = False
    print('loading area... this may take a few seconds')
    for i in range(13):
        print('')
    level1()
                
logo()
