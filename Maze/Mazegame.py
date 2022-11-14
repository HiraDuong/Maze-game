
import pygame
from random import randint
import random
from Maze import maze
import time

pygame.init()

# const
WIDTH,HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()
font = pygame.font.SysFont('sans',20)
hito_img = pygame.image.load('D:/NEWCODE/Game learning/Maze/hito.png')
hito_img = pygame.transform.scale(hito_img,(30,30))
running = True
#color
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)


# Create Matrix
A = []
list = []
Before = []
hito = [0,0]
pausing = False
counts = 0
help = False
# 1 is wall , 0 = 20 px

def in_Maze(Mat,r,c):
        if 0<=r<len(Mat) and 0<=c<len(Mat[0]):
            return True
        else: return False
    
def BFS(Mat,r,c,end):
    # Tạo before để truy vết
        end_x,end_y = end[0],end[1]
        #Before = [(0,0)]*len(Mat)
        for i in range(len(Mat)):
            Before.append([(0,0)]*len(Mat[0]))

        '''for j in range(len(Mat)):
            Before[j] = [(0,0)]*len(Mat[0])
'''
        Queue = [(r,c)]
        #print(Queue)
        # up,down,right,left
        move = [(-1,0),(1,0),(0,1),(0,-1)]
        count = 0
        while Queue:
        #  duyet tung dinh(start BFS)
            x,y = Queue[0][0],Queue[0][1]
            
            #print (str(x)+" "+str(y))
            #count +=1

            if in_Maze(Mat,x,y) :
                for i in (move):
                    if in_Maze(Mat,x + i[0],y+i[1])and Mat[x+i[0]][y+i[1]]==0:
                        if (x + i[0],y+i[1]) not in Queue:
                            Before[x + i[0]][y+i[1]] = (x,y)
                            Queue.append((x + i[0],y+i[1]))
                Mat[x][y] = 2 # 2 mean visited
                Queue.pop(0)
                '''
                check thứ tự duyệt 
                print(Queue)'''
                if x == 19 and y == 19:        
                    #in ra điểm cuối của đường ngắn nhất
                    #print(count)
                    break
                # tức là nếu vẫn đang trong mê kyuu mà hết đỉnh duyệt (hết đường đi)
                # - >  không còn đường chạy -> chúc mừng bạn quay vào -1
                if len(Queue) == 0 :
                    print("-1")
                    print("There is no way to nigerou outside of Matrix :))")
                    return 0

        #print("done "+str(x+1)+" "+str(y+1))
        '''for i in range(len(Before)):
            print(Before[i])
            '''
        # Truy vết :
        print("The shortest path is: ")
        while (x,y) != (r,c):
            print(str((x+1,y+1)),end="<-")
            (x,y) = Before[x][y]
            count+=1
        print(str((r+1,c+1)))
        print("with "+str(count+1)+" steps ")


def draw_path(Mat,r,c,x,y):
    pygame.draw.rect(screen,RED,(0+5,0+5,20,20))
    #print("The shortest path is: ")
    while (x,y) != (r,c):
        (x,y) = Before[x][y]
       
        pygame.draw.rect(screen,RED,(y*30+10,x*30+10,10,10))

   
def check_wall(i,j):
    return A[i][j]


# Create Matrix
def Create_Mat():

    for k in range(20):
        list = []
        for i in range (20):
            list.append(0)
        
        for i in range(10):
            j = randint(0,19)
            list[j] = 1

        A.append(list)
    A[0][0] = 0 
        # start = (0,0)
    A[19][19] = 0
        # end =(19,19)    
        
    '''for i in range(len(A)):
        print(A[i])'''

def New_Game():  
    
    Create_Mat()
    while BFS(A,0,0,(19,19)) == 0:
        A.clear()
        Create_Mat()


def Create_Hito():
    #pygame.draw.rect(screen,YELLOW,(hito[1]*30,hito[0]*30,30,30))
    screen.blit(hito_img,(hito[1]*30,hito[0]*30))

def Win():
    return True if hito[0] == 19 and hito[1] == 19 else False

def Matrix():
    for i in range(len(A)):
        for j in range (len(A[i])):
            if A[i][j]==1:
                pygame.draw.rect(screen,BLACK,(j*30,i*30,30,30)) 



#  Windows 
New_Game()

while running:
#   

    screen.fill(GREEN)
    clock.tick(60)
    
    Matrix()
    if help:
        draw_path(A,0,0,19,19)
    Create_Hito()    
    if Win() :
        pausing = True
    if pausing:
        gameover = font.render("GAME DONE! STEPS = " + str(counts),True,BLACK)
        retry = font.render ("Press Space to try again",True,BLACK)
        pygame.draw.rect(screen,WHITE,(100,200,400,200))
        screen.blit(gameover,(100,250))
        screen.blit(retry,(250,300))


      

    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if check_wall(hito[0]-1,hito[1]) !=1:
                    counts +=1
                    print("UP")
                    hito[0]-=1
                
                    print([i+1 for i in hito])
            if event.key == pygame.K_DOWN:
                if check_wall(hito[0]+1,hito[1]) !=1:
                    counts +=1
                    print("DOWN")
                    hito[0]+=1
                    print([i+1 for i in hito])
            if event.key == pygame.K_RIGHT:
                if check_wall(hito[0],hito[1]+1) !=1:
                    counts +=1
                    print("RIGHT")
                    hito[1]+=1
                    print([i+1 for i in hito])
            if event.key == pygame.K_LEFT:
                if check_wall(hito[0],hito[1]-1) !=1:
                    counts +=1
                    print("LEFT")
                    hito[1]-=1
                    print([i+1 for i in hito])
            if event.key == pygame.K_SPACE:
                pausing = False
                hito = [0,0] 
                help = False
                New_Game()
            if event.key == pygame.K_h:
                help = True
                

    pygame.display.flip()
pygame.quit()
