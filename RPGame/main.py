import curses, time, random, os, sys, enemy, player

'''
Player name: 


'''

def init():
    global w, sh, sw, screen
    
    #p.askName()
    screen = curses.initscr()
    screen.clear()

    sh, sw = screen.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)

    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    #w.keypad(1)

    #update()


def update():
    playerH = int(sh/6)
    pw = int(sw/100)
    #w.addstr(0, 0, str(ph) + ", " + str(pw))
    mult = 20
    # Player stats
    w.addstr(playerH, mult * pw, "Player")
    w.addstr(playerH + 1, mult * pw + 8, "HP: {}".format(p.hp))
    w.addstr(playerH + 2, mult * pw + 5, "Armor: {}".format(p.armor))
    w.addstr(playerH + 3, mult * pw + 1, "AttackDMG: {}".format(p.aDmg))
    w.addstr(playerH + 4, mult * pw + 5, "Magic: {}".format(p.mDmg))
    w.addstr(playerH + 5, mult * pw + 6, "Gold: {}".format(p.gold))
    w.refresh()
    
    mult2 = 75

    # Enemy stats
    w.addstr(playerH, mult2 * pw, cEnemy.name)
    w.addstr(playerH + 1, mult2 * pw + 8, "HP: {}".format(cEnemy.hp))
    w.addstr(playerH + 2, mult2 * pw + 1, "AttackDMG: {}".format(cEnemy.dmg))
    w.addstr(playerH + 3, mult2 * pw + 6, "Gold: {}".format(cEnemy.gReward))
    w.addstr(playerH + 4, mult2 * pw + 8, "XP: {}".format(cEnemy.xpReward))
    w.refresh()
    time.sleep(2)

    mainMenu()

def mainMenu():
    global bh, bw
    
    w.clear()

    bh = int(sh/3)
    bw = int(sw/100)


    # Buttons
    # Play
    w.addstr(bh, 30 * bw, "Play")
    w.addstr(bh, 75 * bw, "Settings")
    w.addstr(bh + 3, 30 * bw, "Button3")
    w.addstr(bh + 3, 75 * bw, "Quit")

    cButtons = mMenuBtns

    w.refresh()
    time.sleep(2)
    return
    

mMenuBtns = [
    "Play",
    "Settings",
    "Button3",
    "Quit"
]


# Class instances
p = player.Player()
zombie = enemy.Enemy("Zombie", 60, 10, 10, 10)

cEnemy = zombie
cButtons = []



cursorLocation = 1

k = 0

init()
mainMenu()

print("aaa")

while True:
    
    print(k)

    if len(cButtons) == 4:
        # Arrow Down
        if k == curses.KEY_DOWN or k == curses.KEY_UP:
            if cursorLocation == 1:
                cursorLocation = 3
            elif cursorLocation == 2:
                cursorLocation = 4
            elif cursorLocation == 3:
                cursorLocation = 1
            elif cursorLocation == 4:
                cursorLocation = 2

        if k == curses.KEY_LEFT or k == curses.KEY_RIGHT:
            if cursorLocation == 1:
                cursorLocation = 2
            elif cursorLocation == 2:
                cursorLocation = 1
            elif cursorLocation == 3:
                cursorLocation = 4
            elif cursorLocation == 4:
                cursorLocation = 3

        if cursorLocation == 1:
            w.addstr(bh, 28 * bw, ">>")
        
        w.refresh()

        time.sleep(2)

    k = screen.getch()

    