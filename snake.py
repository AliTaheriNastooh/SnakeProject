import os
from colorama import init
init()
import msvcrt
import time
import random
from colorama import Fore, Back, Style
def cheker_menu(inp,n,x):
    if inp=="w":
	if n==0:
	    n=4
	    x=13
	    return n,x
	else:
	    n=n-1
	    x=x-2
	    return n,x
    else:
	if inp=="s":
	    if n==4:
		n=0
		x=5
		return n,x
	    else:
		n=n+1
		x=x+2
		return n,x
	else:
	    return n,x	    
    
def menu():
    print(Back.BLACK + "\033[" + "5"+ ";" + "30" +"H5")
    print(Fore.WHITE + "\033[" + "5"+ ";" + "30" +"H5")
    os.system("cls")
    a=["start","type game","high score","instruction","exit"]
    x=5
    y=30
    n=0
    for i in a:
        print "\033[" + str(x)+ ";" + str(y) +"H"+i
        x=x+2
    x=5
    print(Back.RED + "\033[" + "5"+ ";" + "30" +"H"+a[0])
    while 1:
	if msvcrt.kbhit():
	    inp=msvcrt.getch()
	    if ord(inp)==13:
		if n==0:
		    start1(1,1)
		    menu()
		    break
		if n==1:
		    menu2()
		    break
		if n==2:
		    print(Back.BLACK + "\033[" + "5"+ ";" + "30" +"H5")
		    os.system('cls')
		    f=open("high_score.txt","r")
		    high_score=f.read()
		    print f.read()
		    print"\033[" + "12"+ ";" + "30" +"Hhigh score="+str(high_score)
		    time.sleep(5)
		    f.close()
		    menu()
		    break
		if n==3:
		    print(Back.BLACK + "\033[" + "5"+ ";" + "30" +"H5")
		    os.system("cls")
		    a='''use  W  A  S  D  to control the snake.
		        eat the food without collsing whit any obstacles
		        and eat bonus food to score extra point.
		        use  E  to quickly move and use Q  to  slowly move.
		        you can select the type game in menu and choose 
		        the arbitery opinion.
		        you can chose"stage by stage" and play all level if
		        you can to take Enough score and you can select the
		        special level and play until impact obstacle
		         
		         you can enjoy the game'''
		    print(Fore.GREEN + "\033[" + "11"+ ";" + "20" +"H"+a)
		    time.sleep(10)
		    menu()
		    break
		if n==4:
		    break
	    else:
		print(Back.BLACK + "\033[" + str(x)+ ";" + str(y) +"H"+a[n])
		n,x=cheker_menu(inp,n,x)
		print(Back.RED + "\033[" + str(x)+ ";" + str(y) +"H"+a[n])
def menu2():
    b=["stage by stage","level 1","level 2","level 3","level 4"]
    print(Back.BLACK + "\033[" + "5"+ ";" + "30" +"H5")
    os.system("cls")
    n=0
    x=5
    y=30
    for i in b:
	print "\033[" + str(x)+ ";" + str(y) +"H"+i 
	x=x+2
    x=5
    print(Back.RED + "\033[" + "5"+ ";" + "30" +"H"+b[0])
    while 1:
	if msvcrt.kbhit():
	    inp=msvcrt.getch()
	    if ord(inp)==13:
		if n==0:
		    start1(1,1)
		    menu()
		    break
		if n==1:
		    start1(1,0)
		    menu()
		    break
		if n==2:
		    start1(2,0)
		    menu()
		    break
		if n==3:
		    start1(3,0)
		    menu()
		    break
		if n==4:
		    start1(4,0)
		    menu()
		    break
	    else:
		if ord(inp)==27:
		    menu()
		    break
		else:
		    print(Back.BLACK + "\033[" + str(x)+ ";" + str(y) +"H"+b[n])
		    n,x=cheker_menu(inp,n,x)
		    print(Back.RED + "\033[" + str(x)+ ";" + str(y) +"H"+b[n])
def random1():
    x=random.randint(1,25)
    y=random.randint(1,60)
    return x,y

def jahat(inp,l,c):
    if inp==115:	    
        if l==25:
	    return 1,c
        else:
            return l+1,c
    else:
	if inp==100:
	    if c==60:
                return l,1
            else:
                return l,c+1
	else:
            if inp==119:
                if l==1:
                    return 25,c
                else:
                    return l-1,c
            else:
		if inp==97:
		    if c==1:
			return l,60
		    else:
			return l,c-1
def cheker_jahat(inp,inp_last):
    if inp==115:	    
        if inp_last==119:
	    return inp_last
        else:
            return inp
    else:
	if inp==119:
	    if inp_last==115:
                return inp_last
            else:
                return inp
	else:
            if inp==100:
                if inp_last==97:
                    return inp_last
                else:
                    return inp
            else:
		if inp==97:
		    if inp_last==100:
			return inp_last
		    else:
			return inp    
    return inp_last
def wall1():
    a=[]
    for i in range(1,61):
	a=a+[[12,i]]
    for j in range(1,26):
	a=a+[[j,30]]
    return a
def line_mark():
    a=[]
    b=[]
    for i in range(1,61):
	a=a+[[26,i]]
    for j in range(1,26):
	b=b+[[j,61]] 
    return a,b
def wall2():
    a=[]
    for i in range(1,11):
	a=a+[[1,i]]
	a=a+[[i,1]]
	a=a+[[i,60]]
	a=a+[[25,i]]
    for i in range(50,61):
	a=a+[[1,i]]
	a=a+[[25,i]]
    for i in range(15,26):
	a=a+[[i,1]]
	a=a+[[i,60]]
    for i in range(9,55):
	a=a+[[7,i]]
	a=a+[[12,i]]
	a=a+[[17,i]]
    return a
def wall3():
    a=[]
    for i in range(1,11):
	a=a+[[i,27]]
    for i in range(2,28):
	a=a+[[10,i]]
    for i in range(35,61):
	a=a+[[3,i]]
    for i in range(5,26):
	a=a+[[i,35]]
    for i in range(1,31):
	a=a+[[13,i]]
    for i in range(15,26):
	a=a+[[i,30]]
    return a



def start1(level_game,type_game):
    print(Back.BLACK + "\033[" + "5"+ ";" + "30" +"H5")
    os.system('cls')
    if level_game==1:
	wall=[]
	score=0
	speed=0.5
	speed_limit=0.32
	l=1
	c=1
	print"\033[" + "12"+ ";" + "30" +"Hlevel\t1"
	time.sleep(3)
    else:
	if level_game==2:
	    if type_game==0:
		score=0
	    else:
		score=70
	    speed=0.3
	    speed_limit=0.2
	    l=1
	    c=1
	    wall=wall1()
	    print"\033[" + "12"+ ";" + "30" +"Hlevel\t2"
	    time.sleep(3)
	else:
	    if level_game==3:
		if type_game==0:
		    score=0
		else:
		    score=140
		l=2
		c=2
		speed=0.15
		speed_limit=0.07
		wall=wall2()
		print"\033[" + "12"+ ";" + "30" +"Hlevel\t3"
		time.sleep(3)
	    else:
		if level_game==4:
		    if type_game==0:
			score=0
		    else:
			score=240
		    l=1
		    c=1
		    speed=0.11
		    speed_limit=0.08
		    wall=wall3()
		    print"\033[" + "12"+ ";" + "30" +"Hlevel\t4"
		    time.sleep(3)
    os.system("cls")
    f=open("high_score.txt","r")
    high_score=f.read()
    print f.read()
    print"\033[" + "27"+ ";" + "45" +"Hhigh score="+str(high_score)    
    if level_game!=1:
	for i1 in wall:
	    print"\033[" + str(i1[0])+ ";" + str(i1[1]) +"H#"
    print"\033[" + "27"+ ";" + "1" +"Hyour score="+str(score)
    line_markx,line_marky=line_mark()
    for i in line_markx:
	print"\033[" + str(i[0])+ ";" + str(i[1]) +"H-"
    for i in line_marky:
	print"\033[" + str(i[0])+ ";" + str(i[1]) +"H|"
    print"\033[" + "27"+ ";" + "17" +"Hturbo=off"
    print"\033[" + "27"+ ";" + "30" +"Hbrake=off"
    lst_basic=[]
    Length_snake=1
    lst_basic=lst_basic+[[l,c]]
    x_random,y_random=random1()
    while 1:
	if [x_random,y_random] in wall:
	    x_random,y_random=random1()
	else:
	    print"\033[" + str(x_random)+ ";" + str(y_random) +"HO"
	    break    
    flag_speed1=0
    flag_speed2=0
    x_random2=70
    y_random2=70
    flag_food=0
    flag_print_score=0
    print(Back.GREEN + "\033[" + str(l)+ ";" + str(c) +"H0")
    print(Style.RESET_ALL)
    while 1:
	if msvcrt.kbhit():
	    inp=ord(msvcrt.getch())	
	    if inp==cheker_jahat(inp,0):
		break    
    while 1:
	inp_last=inp
	print"\033[" + str(x_random)+ ";" + str(y_random) +"HO" 
	if msvcrt.kbhit():
	    inp=ord(msvcrt.getch())
	    if inp==101:
		if flag_speed1==0:
		    speed=speed-speed_limit
		    flag_speed1=1
		    print"\033[" + "27"+ ";" + "17" +"Hturbo=on "
		    
		else:
		    speed=speed+speed_limit
		    flag_speed1=0
		    print"\033[" + "27"+ ";" + "17" +"Hturbo=off"
	    if inp==113:
		if flag_speed2==0:
		    speed=speed+speed_limit
		    flag_speed2=1
		    print"\033[" + "27"+ ";" + "30" +"Hbrake=on "
		else:
		    speed=speed-speed_limit
		    flag_speed2=0
		    print"\033[" + "27"+ ";" + "30" +"Hbrake=off"
	    cheker=cheker_jahat(inp,inp_last)
	    if cheker==inp:
		inp_last=inp
	    inp=cheker 
	l,c=jahat(inp,l,c)
	lst_basic=lst_basic+[[l,c]]
	if l==x_random and c==y_random:
	    x_random,y_random=random1()
	    while 1:
		if [x_random,y_random] in wall:
		    x_random,y_random=random1()
		else:
		    print"\033[" + str(x_random)+ ";" + str(y_random) +"HO"
		    break
	    Length_snake+=1
	    score=score+5
	    print"\033[" + "27"+ ";" + "1" +"Hyour score="+str(score)
	if Length_snake%5==0 and flag_food==0:
	    x_random2,y_random2=random1()
	    while 1:
		if [x_random2,y_random2] in wall:
		    x_random2,y_random2=random1()
		else:
		    print(Back.RED + "\033[" + str(x_random2)+ ";" + str(y_random2) +"HO")
		    print(Style.RESET_ALL)
		    flag_food=1
		    break
	if l==x_random2 and c==y_random2:
	    print"\033[" + str(x_random2)+ ";" + str(y_random2) +"H "
	    flag_food=0
	    Length_snake+=1
	    score=score+10
	    print"\033[" + "27"+ ";" + "1" +"Hyour score="+str(score)
	    x_random2=70
	    y_random2=70
	    
	if (score==60 or score==65) and type_game==1:
	    start1(2,1)
	    flag_print_score=1
	    break
	else:
	    if (score==130 or score==135) and type_game==1:
		start1(3,1)
		flag_print_score=1
		break
	    else:
		if (score==230 or score==235) and type_game==1:
		    start1(4,1)
		    flag_print_score=1
		    break
	if score==340 or score==345:
	    print(Back.GREEN + "5")
	    os.system("cls")
	    for counter in range(8,25,3):
		print"\033[" + str(counter)+ ";" + "30" +"Hyoooou wiiiin"
	    time.sleep(8)
	    break
	    
	length_basic=len(lst_basic)
	lst_cleaner=lst_basic[length_basic-Length_snake-1]
	lst_snake=lst_basic[length_basic-Length_snake:]
	lst_basic=lst_basic[length_basic-Length_snake-1:]
	legth_snake=len(lst_snake)
	if [l,c] in lst_snake[:legth_snake-1]:
	    break
	if [l,c] in wall:
	    break

	print"\033[" + str(lst_cleaner[0])+ ";" + str(lst_cleaner[1]) +"H "
	print(Back.GREEN + "\033[" + str(lst_snake[legth_snake-1][0])+ ";" + str(lst_snake[legth_snake-1][1]) +"H0")
	counter=2
	for i in range(Length_snake-1):
	    print(Back.BLUE + "\033[" + str(lst_snake[legth_snake-counter][0])+ ";" + str(lst_snake[legth_snake-counter][1]) +"H0")
	    counter=counter+1
	time.sleep(speed)
	print(Style.RESET_ALL)
    os.system("cls")
    f.close()
    if flag_print_score==0:
	if score>int(high_score):
	    print"\033[" + "12"+ ";" + "30" +"H oooo you get high score\t"+str(score)
	    f=open("high_score.txt","w")
	    f.write(str(score))
	else:
	    print"\033[" + "12"+ ";" + "30" +"Hyour score\t"+str(score)
	time.sleep(5)
print(Back.CYAN + " ")
os.system("cls")
time.sleep(2)
for x in range(12,16,2):
    print(Fore.BLACK + "\033[" + str(x)+ ";" + "22" +"H SNAKE ")
time.sleep(3)
for x in range(12,16,2):
    print(Fore.BLACK + "\033[" + str(x)+ ";" + "30" +"H GAME")
time.sleep(4)
os.system("cls")
print(Fore.BLACK + "\033[" + "12"+ ";" + "22" +"H coded by ali taheri nastooh")
time.sleep(4)



menu()
print(Style.RESET_ALL)
os.system("cls")
print(Back.GREEN + "\033[" + "12"+ ";" + "30" +"Hend game")
print(Back.GREEN + "\033[" + "16"+ ";" + "20" +"H design by ali taheri nastooh")
time.sleep(9)

                
                
            
            
        
