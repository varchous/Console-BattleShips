from random import *
a1=[0,[1,2]]
a2=[1,2]
a3=[1,2]
a4=[1,2]
a5=[[1,2],[2,4]]
a6=[[1,2],[2,4]]
a7=[[1,2],[2,4]]
a8=[[1,2],[3,4],[5,6]]
a9=[[1,2],[3,4],[5,6]]
a10=[0,[[1,2],[3,4],[5,6],[7,8]]]
a=[a1,a5,a8,a10]
#print(a[0][0])
def show_1(p):
    for i in range(10):
        if(i==0):#Вывод букв а-к
            print('    ',end='')
            for j in range(10):
                print(s[j],end=' ')
            print()
        if(i==0):
            print('    ',end='')
            for j in range(10):
                print('-',end=' ')        
        print()
        if(i!=9):#Вывод цифр 1-10
            print(i+1,'|',end=' ')
        else:
            print(i+1,end='')
            print('|',end=' ')
        for j in range(10): #вывод поля 1 игрока
            if(p[i][j]==1):
                print('O',end=' ')
            elif(p[i][j]==2):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('|',end='')
    print()
    print('   ',end=' ')
    for i in range(10):
            print('-',end=' ')
    print()    
def start_manually(c,s): #Заполнение поля с клавиатуры
    p=[]
    for i in range(10):
        M=[]
        for j in range(10):
            M.append(0)
        p.append(M)      
    k=0
    while(k<=9):
        show_1(p) 
        if(k<4):
            print('Введите координаты для расположения 1 палубного корабля')
            flag=1
            while(flag==1):
                print('Введите координаты (1-по вертикали(1-10),2-по горизонтали(а-к))')
                print('1:',end='')
                x=input()
                print('2:',end='')
                y=input()
                if(x.isdigit()==1):
                    x=int(x)
                else:
                    print('Не верно заданны координаты')
                    continue
                if((x>=1 and x<=10) and (s.count(y)==1)):
                    x=x-1
                    y=s.index(y)
                    if(p[x][y]==0):
                        p[x][y]=1
                        c1=[]
                        c1.append(x)
                        c1.append(y)
                        c1.append(-1)
                        c.append(c1)
                        flag=0
                        if(x==0):
                            r1=x
                            r2=x+2
                        elif(x==9):
                            r1=x-1
                            r2=x+1
                        else:
                            r1=x-1
                            r2=x+2   
                        if(y==0):
                            r3=y
                            r4=y+2
                        elif(y==9):
                            r3=y-1
                            r4=y+1
                        else:
                            r3=y-1
                            r4=y+2
                else:
                    print('Не верно заданны координаты')
                if(flag==0):
                    for i in range(r1,r2):
                        for j in range(r3,r4):
                            if(p[i][j]!=1):
                                p[i][j]=2                    
        elif(k>=4 and k<7):
            print('Введите координаты для расположения 2-x палубного корабля')
            flag=1
            while(flag==1):
                print('Введите координаты начала(1-по вертикали(1-10),2-по горизонтали(а-к))')
                print('1:',end='')
                x=input()
                print('2:',end='')
                y=input()
                print('Введите координаты конца(3-по вертикали(1-10),4-по горизонтали(а-к), одна из координат должна быть равной начала, а вторая больше)')
                print('3:',end='')
                x2=input()
                print('4:',end='')
                y2=input()    
                if(x.isdigit()==1 and x2.isdigit()==1):
                    x=int(x)
                    x2=int(x2)
                else:
                    print('Не верно заданны координаты')
                    continue
                if((x>=1 and x<=10) and (x2>=1 and x2<=10) and (s.count(y)==1) and (s.count(y2)==1)):
                    x=x-1
                    x2=x2-1
                    y=s.index(y)
                    y2=s.index(y2)
                    if(x==x2 and ((y2-y)==1)):
                        if(p[x][y]==0 and p[x][y+1]==0):
                            p[x][y]=1
                            p[x][y+1]=1
                            c1=[]
                            c1.append(x)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x)
                            c1.append(y+1)
                            c1.append(-1)
                            c.append(c1)
                            flag=0
                            if(x==0):
                                r1=x
                                r2=x+2
                            elif(x==9):
                                r1=x-1
                                r2=x+1
                            else:
                                r1=x-1
                                r2=x+2   
                            if(y==0):
                                r3=y
                                r4=y+3
                            elif(y2==9):
                                r3=y-1
                                r4=y+2
                            else:
                                r3=y-1
                                r4=y+3
                    elif(y==y2 and ((x2-x)==1)):  
                        if(p[x][y]==0 and p[x+1][y]==0):
                            p[x][y]=1
                            p[x+1][y]=1
                            c1=[]
                            c1.append(x)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x+1)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            flag=0
                            if(x==0):
                                r1=x
                                r2=x+3
                            elif(x2==9):
                                r1=x-1
                                r2=x+2
                            else:
                                r1=x-1
                                r2=x+3    
                            if(y==0):
                                r3=y
                                r4=y+2
                            elif(y==9):
                                r3=y-1
                                r4=y+1
                            else:
                                r3=y-1
                                r4=y+2
                    else:
                        print('Не верно заданны координаты')
                    if(flag==0):
                        for i in range(r1,r2):
                            for j in range(r3,r4):
                                if(p[i][j]!=1):
                                    p[i][j]=2
                else:
                    print('Не верно заданны координаты')     
        elif(k>=7 and k<9):
            print('Введите координаты для расположения 3-x палубного корабля')
            flag=1
            while(flag==1):
                print('Введите координаты начала(1-по вертикали(1-10),2-по горизонтали(а-к))')
                print('1:',end='')
                x=input()
                print('2:',end='')
                y=input()
                print('Введите координаты конца(3-по вертикали(1-10),4-по горизонтали(а-к), одна из координат должна быть равной начала, а вторая больше)')
                print('3:',end='')
                x2=input()
                print('4:',end='')
                y2=input()    
                if(x.isdigit()==1 and x2.isdigit()==1):
                    x=int(x)
                    x2=int(x2)
                else:
                    print('Не верно заданны координаты')
                    continue
                if((x>=1 and x<=10) and (x2>=1 and x2<=10) and (s.count(y)==1) and (s.count(y2)==1)):
                    x=x-1
                    x2=x2-1
                    y=s.index(y)
                    y2=s.index(y2)
                    if(x==x2 and ((y2-y)==2)):
                        if(p[x][y]==0 and p[x][y+1]==0 and p[x][y+2]==0 ):
                            p[x][y]=1
                            p[x][y+1]=1
                            p[x][y+2]=1
                            c1=[]
                            c1.append(x)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x)
                            c1.append(y+1)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x)
                            c1.append(y+2)
                            c1.append(-1)
                            c.append(c1)
                            flag=0
                            if(x==0):
                                r1=x
                                r2=x+2
                            elif(x==9):
                                r1=x-1
                                r2=x+1
                            else:
                                r1=x-1
                                r2=x+2   
                            if(y==0):
                                r3=y
                                r4=y+4
                            elif(y2==9):
                                r3=y-1
                                r4=y+3
                            else:
                                r3=y-1
                                r4=y+4
                    elif(y==y2 and ((x2-x)==2)):  
                        if(p[x][y]==0 and p[x+1][y]==0 and p[x+2][y]==0 ):
                            p[x][y]=1
                            p[x+1][y]=1
                            p[x+2][y]=1
                            c1=[]
                            c1.append(x)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x+1)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x+2)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            flag=0
                            if(x==0):
                                r1=x
                                r2=x+4
                            elif(x2==9):
                                r1=x-1
                                r2=x+3
                            else:
                                r1=x-1
                                r2=x+4    
                            if(y==0):
                                r3=y
                                r4=y+2
                            elif(y==9):
                                r3=y-1
                                r4=y+1
                            else:
                                r3=y-1
                                r4=y+2
                    else:
                        print('Не верно заданны координаты')
                    if(flag==0):
                        for i in range(r1,r2):
                            for j in range(r3,r4):
                                if(p[i][j]!=1):
                                    p[i][j]=2
                else:
                    print('Не верно заданны координаты')                        
        else:
            print('Введите координаты для расположения 4-x палубного корабля')
            flag=1
            while(flag==1):
                print('Введите координаты начала(1-по вертикали(1-10),2-по горизонтали(а-к))')
                print('1:',end='')
                x=input()
                print('2:',end='')
                y=input()
                print('Введите координаты конца(3-по вертикали(1-10),4-по горизонтали(а-к), одна из координат должна быть равной начала, а вторая больше)')
                print('3:',end='')
                x2=input()
                print('4:',end='')
                y2=input()    
                if(x.isdigit()==1 and x2.isdigit()==1):
                    x=int(x)
                    x2=int(x2)
                else:
                    print('Не верно заданны координаты')
                    continue
                if((x>=1 and x<=10) and (x2>=1 and x2<=10) and (s.count(y)==1) and (s.count(y2)==1)):
                    x=x-1
                    x2=x2-1
                    y=s.index(y)
                    y2=s.index(y2)
                    if(x==x2 and ((y2-y)==3)):
                        if(p[x][y]==0 and p[x][y+1]==0 and p[x][y+2]==0 and p[x][y+3]==0):
                            p[x][y]=1
                            p[x][y+1]=1
                            p[x][y+2]=1
                            p[x][y+3]=1
                            c1=[]
                            c1.append(x)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x)
                            c1.append(y+1)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x)
                            c1.append(y+2)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x)
                            c1.append(y+3)
                            c1.append(-1)
                            c.append(c1)
                            flag=0
                            if(x==0):
                                r1=x
                                r2=x+2
                            elif(x==9):
                                r1=x-1
                                r2=x+1
                            else:
                                r1=x-1
                                r2=x+2   
                            if(y==0):
                                r3=y
                                r4=y+5
                            elif(y2==9):
                                r3=y-1
                                r4=y+4
                            else:
                                r3=y-1
                                r4=y+5
                    elif(y==y2 and ((x2-x)==3)):  
                        if(p[x][y]==0 and p[x+1][y]==0 and p[x+2][y]==0 and p[x+3][y]==0):
                            p[x][y]=1
                            p[x+1][y]=1
                            p[x+2][y]=1
                            p[x+3][y]=1
                            c1=[]
                            c1.append(x)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x+1)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x+2)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            c1=[]
                            c1.append(x+3)
                            c1.append(y)
                            c1.append(-1)
                            c.append(c1)
                            flag=0
                            if(x==0):
                                r1=x
                                r2=x+5
                            elif(x2==9):
                                r1=x-1
                                r2=x+4
                            else:
                                r1=x-1
                                r2=x+5    
                            if(y==0):
                                r3=y
                                r4=y+2
                            elif(y==9):
                                r3=y-1
                                r4=y+1
                            else:
                                r3=y-1
                                r4=y+2
                    else:
                        print('Не верно заданны координаты')
                    if(flag==0):
                        for i in range(r1,r2):
                            for j in range(r3,r4):
                                if(p[i][j]!=1):
                                    p[i][j]=2
                else:
                    print('Не верно заданны координаты')
                    
        k=k+1    
    return p        
def play_comp():#ход 2 игрока(компьютера)
    a=0
    b=9
    flag=1
    while(flag==1):
        x=randint(a,b)
        y=randint(a,b)
        if(p1[x][y]!=3 and p1[x][y]!=4):
            if(p1[x][y]==1):
                p1[x][y]=3
                for i in range(len(a1)):
                    if(a1[i][0]==x and a1[i][1]==y):
                        a1[i][2]=-2
            else:
                p1[x][y]=4
            flag=0
    print('Игрок 2 выстрелил по', x+1,s[y])    
def play():#ход 1 игрока
    print('Введите координаты выстрела')
    flag=1
    while(flag==1):
        print('По вертикали(1-10)',end=':')
        x=input()
        print('По горизонтали(а-к)',end=':')
        y=input()
        if(x.isdigit()==1):
            x=int(x)
        else:
            print('Не верные координаты')
            continue
        if((x>=1 and x<=10) and s.count(y)==1):
            print(x,y)
            x=x-1
            y=s.index(y)
            if(p2[x][y]!=3 and p2[x][y]!=4):
                if(p2[x][y]==1):
                    p2[x][y]=3
                    for i in range(len(a1)):
                        if(a2[i][0]==x and a2[i][1]==y):
                            a2[i][2]=-2
                else:
                    p2[x][y]=4
                flag=0
            else:
                print('Не верные координаты')
        else:
            print('Не верные координаты')    
def show():#Вывод поля
    for i in range(10):
        if(i==0):#Вывод букв а-к
            print('    ',end='')
            for j in range(10):
                print(s[j],end=' ')
            print('             ',end='')
            for j in range(10):
                print(s[j],end=' ')    
            print()
        if(i==0): 
            print('    ',end='')
            for j in range(10):
                print('-',end=' ')
            print('             ',end='')
            for j in range(10):
                print('-',end=' ')            
            print()    
        if(i!=9):#Вывод цифр 1-10
            print(i+1,'|',end=' ')
        else:
            print(i+1,end='')
            print('|',end=' ')

        for j in range(10): #вывод поля 1 игрока
            if(p1[i][j]==1):
                print('O',end=' ')
            elif(p1[i][j]==3):
                print('X',end=' ')
            elif(p1[i][j]==4):
                print('*',end=' ')
            else:
                print(' ',end=' ')    
        print('|        ',end='')

        if(i!=9):#Вывод цифр 1-10
            print(i+1,'|',end=' ')
        else:
            print(i+1,end='')
            print('|',end=' ')
        
        for j in range(10):#вывод поля 2 игрока
            if(p2[i][j]==4):
                print('*',end=' ')
            elif(p2[i][j]==3):
                print('X',end=' ')
            else:
                print(' ',end=' ')    
        print('',end='|')
        print()
    print('    ',end='')    
    for i in range(10):
        print('-',end=' ')
    print('             ',end='')
    for i in range(10):
        print('-',end=' ')
    print()
    print('------------------------------------------------------------')
    print('',end='  ')
    ch=1
    for i in range(4):#1
        if(a1[i][2]==-1):
            ch='O'
        elif(a1[i][2]==-2):
            ch='X'
        print(' ',ch,end='')
    print('',end='                      ')    
    for i in range(4):
        if(a2[i][2]==-1):
            ch='O'
        elif(a2[i][2]==-2):
            ch='X'
        print(' ',ch,end='')        
    print()
    print('',end='   ')
    for i in range(4,10):#2
        if(a1[i][2]==-1):
            ch='O'
        elif(a1[i][2]==-2):
            ch='X'
        if(i%2==0):    
            print('',ch,end='')
        else:
            print('',ch,end=' ')
    print('',end='                   ')         
    for i in range(4,10):
        if(a2[i][2]==-1):
            ch='O'
        elif(a2[i][2]==-2):
            ch='X'
        if(i%2==0):    
            print('',ch,end='')
        else:
            print('',ch,end=' ')           
    print()
    print('',end='   ')
    for i in range(10,16):#3
        if(a1[i][2]==-1):
            ch='O'
        elif(a1[i][2]==-2):
            ch='X'
        if(i%12==0):
            print('',ch,end=' ')
        else:
            print('',ch,end='')
    print('',end='                     ')
    for i in range(10,16):
        if(a2[i][2]==-1):
            ch='O'
        elif(a2[i][2]==-2):
            ch='X'
        if(i%12==0):
            print('',ch,end=' ')
        else:
            print('',ch,end='')
    print()
    print('',end='   ')
    for i in range(16,20):#4
        if(a1[i][2]==-1):
            ch='O'
        elif(a1[i][2]==-2):
            ch='X'
        print('',ch,end='')
    print('',end='                          ')
    for i in range(16,20):
        if(a2[i][2]==-1):
            ch='O'
        elif(a2[i][2]==-2):
            ch='X'
        print('',ch,end='')    
    print()    
    print('------------------------------------------------------------')                   
def start(c,s): #случайное заполнение
    p=[]
    a=0
    b=9
    for i in range(10):
        M=[]
        for j in range(10):
            M.append(0)
        p.append(M)
    x=randint(a,b)
    y=randint(a,b)   
    for i in range(4): #случайное заполнение 4 1-палубных кораблей
        while(p[x][y]!=0):
            x=randint(a,b)
            y=randint(a,b)
        p[x][y]=1
        c1=[]
        c1.append(x)
        c1.append(y)
        c1.append(-1)
        c.append(c1)
        if(x==0):
            r1=x
            r2=x+2
        elif(x==9):
            r1=x-1
            r2=x+1
        else:
            r1=x-1
            r2=x+2
        if(y==0):
            r3=y
            r4=y+2
        elif(y==9):
            r3=y-1
            r4=y+1
        else:
            r3=y-1
            r4=y+2
        for i in range(r1,r2):
            for j in range(r3,r4):
                if(p[i][j]!=1):
                    p[i][j]=2
    k2=0
    while(k2<3): #случайное заполнение 3 2-палубных кораблей
        flag=1
        while('''p[x][y]!=0''' and flag==1):
            x=randint(a,b)
            y=randint(a,b)
            f=randint(0,1)
            #print(f,'f')
            if(f==0 and y!=9):
                y2=y+1
                x2=x
            elif(f==1 and x!=9):
                x2=x+1
                y2=y
            else:continue    
            if(p[x2][y2]==0 and p[x][y]==0):
                p[x2][y2]=1
                flag=0
                p[x][y]=1
                c1=[]
                c1.append(x)
                c1.append(y)
                c1.append(-1)
                c.append(c1)
                c1=[]
                c1.append(x2)
                c1.append(y2)
                c1.append(-1)
                c.append(c1)
                if(f==1):
                    if(x==0):
                        r1=x
                        r2=x+3
                    elif(x2==9):
                        r1=x-1
                        r2=x+2
                    else:
                        r1=x-1
                        r2=x+3    
                    if(y==0):
                        r3=y
                        r4=y+2
                    elif(y==9):
                        r3=y-1
                        r4=y+1
                    else:
                        r3=y-1
                        r4=y+2
                if(f==0):
                    if(x==0):
                        r1=x
                        r2=x+2
                    elif(x==9):
                        r1=x-1
                        r2=x+1
                    else:
                        r1=x-1
                        r2=x+2   
                    if(y==0):
                        r3=y
                        r4=y+3
                    elif(y2==9):
                        r3=y-1
                        r4=y+2
                    else:
                        r3=y-1
                        r4=y+3                        
                for i in range(r1,r2):
                    for j in range(r3,r4):
                        if(p[i][j]!=1 and p[i][j]!=3):
                            p[i][j]=2           
        k2=k2+1        
    k3=0
    while(k3<2): #случайное заполнение 2 3-палубных кораблей
        flag=1
        
        while(flag==1):
            x=randint(a,b)
            y=randint(a,b)
            f=randint(0,1)
            #print(f,'f')
            if(f==0 and y<=7):
                y2=y+1
                x2=x
                y3=y+2
                x3=x
            elif(f==1 and x<=7):
                x2=x+1
                y2=y
                x3=x+2
                y3=y
            else:continue     
            if(p[x2][y2]==0 and p[x][y]==0 and p[x3][y3]==0 ):
                flag=0
                p[x][y]=1
                p[x2][y2]=1
                p[x3][y3]=1
                c1=[]
                c1.append(x)
                c1.append(y)
                c1.append(-1)
                c.append(c1)
                c1=[]
                c1.append(x2)
                c1.append(y2)
                c1.append(-1)
                c.append(c1)
                c1=[]
                c1.append(x3)
                c1.append(y3)
                c1.append(-1)
                c.append(c1)
                if(f==1):
                    if(x==0):
                        r1=x
                        r2=x+4
                    elif(x3==9):
                        r1=x-1
                        r2=x+3
                    else:
                        r1=x-1
                        r2=x+4    
                    if(y==0):
                        r3=y
                        r4=y+2
                    elif(y==9):
                        r3=y-1
                        r4=y+1
                    else:
                        r3=y-1
                        r4=y+2
                if(f==0):
                    if(x==0):
                        r1=x
                        r2=x+2
                    elif(x==9):
                        r1=x-1
                        r2=x+1
                    else:
                        r1=x-1
                        r2=x+2   
                    if(y==0):
                        r3=y
                        r4=y+4
                    elif(y3==9):
                        r3=y-1
                        r4=y+3
                    else:
                        r3=y-1
                        r4=y+4
                #print(r1,r2,r3,r4)
                for i in range(r1,r2):
                    #print(k2,"k2")
                    for j in range(r3,r4):
                        if(p[i][j]!=1 and p[i][j]!=3 and p[i][j]!=5):
                            p[i][j]=2
        k3=k3+1
    k4=0
    while(k4<1):#случайное заполнение 1 4-палубных кораблей
        flag=1
        while(flag==1):
            x=randint(a,b)
            y=randint(a,b)
            f=randint(0,1)
            if(f==0 and y<=6):
                y2=y+1
                x2=x
                y3=y+2
                x3=x
                y4=y+3
                x4=x
            elif(f==1 and x<=6):
                x2=x+1
                y2=y
                x3=x+2
                y3=y
                x4=x+3
                y4=y
            else:
                continue
            if(p[x2][y2]==0 and p[x][y]==0 and p[x3][y3]==0 and p[x4][y4]==0):
                flag=0
                p[x][y]=1
                p[x2][y2]=1
                p[x3][y3]=1
                p[x4][y4]=1
                c1=[]
                c1.append(x)
                c1.append(y)
                c1.append(-1)
                c.append(c1)
                c1=[]
                c1.append(x2)
                c1.append(y2)
                c1.append(-1)
                c.append(c1)
                c1=[]
                c1.append(x3)
                c1.append(y3)
                c1.append(-1)
                c.append(c1)
                c1=[]
                c1.append(x4)
                c1.append(y4)
                c1.append(-1)
                c.append(c1)
                if(f==1):
                    if(x==0):
                        r1=x
                        r2=x+5
                    elif(x4==9):
                        r1=x-1
                        r2=x+4
                    else:
                        r1=x-1
                        r2=x+5    
                    if(y==0):
                        r3=y
                        r4=y+2
                    elif(y==9):
                        r3=y-1
                        r4=y+1
                    else:
                        r3=y-1
                        r4=y+2
                if(f==0):
                    if(x==0):
                        r1=x
                        r2=x+2
                    elif(x==9):
                        r1=x-1
                        r2=x+1
                    else:
                        r1=x-1
                        r2=x+2   
                    if(y==0):
                        r3=y
                        r4=y+5
                    elif(y4==9):
                        r3=y-1
                        r4=y+4
                    else:
                        r3=y-1
                        r4=y+5
                for i in range(r1,r2):
                    for j in range(r3,r4):
                        if(p[i][j]!=1 and p[i][j]!=3 and p[i][j]!=5 and p[i][j]!=7):
                            p[i][j]=2                
        k4=k4+1    
    return p
def game_over():#Проверка на конец игры
    k1=0
    k2=0
    flag=0
    for i in range(len(a1)):
        if(a1[i][2]==-1):
            k1=k1+1
        if(a2[i][2]==-1):
            k2=k2+1
    if(k1==0):
        flag=1
    elif(k2==0):
        flag=2
    return flag
s=['а','б','в','г','д','е','ж','з','и','к']
flag=0
a1=[]
a2=[]
p1=[]
p2=[]
print('Выберите вариант заполнения поля')
print('1- случайно')
print('2- с клавиатуры')
g=0
while(g!=2 and g!=1):
    g=int(input())
    if(g==1):
        p1=start(a1,s)
    elif(g==2):
        p1=start_manually(a1,s)
    else:
        print('Ошибка')
p2=start(a2,s)
hod=1
while(flag==0):
    if(hod==1):
        show()
        play()
        hod=0       
    else:
        play_comp()
        hod=1
    flag=game_over()
if(flag==1):
    print('Победил 2 игрок')
elif(flag==2):
    print('Победил 1 игрок')
