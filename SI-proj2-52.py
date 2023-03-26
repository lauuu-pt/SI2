from searchPlus import *
from p2_aux import *

def result(self, state, action): 
        "Tanto as acções como os estados são representados por pares (x,y). from PL"
        (x,y) = state
        (dx,dy) = self.directions[action]
        return (x+dx,y+dy)
    
def actions(self, state):
        """Podes move-te para uma célula em qualquer das direcções para uma casa 
           que não seja obstáculo. from PL"""
        x, y = state
        return [act for act in self.directions.keys() if (x+self.directions[act][0],y+self.directions[act][1]) not in self.obstacles]
 
pacman=(1,1)
pastilha=(1,6)
l = line(2,2,1,0,6)
c = line(2,3,0,1,4)
fronteira = quadro(0,0,10)
obstaculos=fronteira | l | c   
print(display(pacman=(1,1),pastilha=(1,6),obstaculos=fronteira | l | c ,path=[]))

""" def modelo(pacman,pastilha):
        xpacman=pacman[0]
        ypacman=pacman[1]
        xpastilha=pastilha[0]
        ypastilha=pastilha[1]
        maiorx=max(xpacman,xpastilha)
        maiory=max(ypacman,ypastilha)
        menorx=min(xpacman,xpastilha)
        menory=min(ypacman,ypastilha)
        maiores=(maiorx,maiory)
        menores=(menorx,menory)
        return menores , maiores
print(modelo(pacman=(1,1),pastilha=(1,6))) """


def modelo(pacman,pastilha):
        xpacman=pacman[0]
        ypacman=pacman[1]
        xpastilha=pastilha[0]
        ypastilha=pastilha[1]
        maiorx=max(xpacman,xpastilha)
        maiory=max(ypacman,ypastilha)
        menorx=min(xpacman,xpastilha)
        menory=min(ypacman,ypastilha)
        maiores=(maiorx,maiory)
        nlinhas=maiorx
        ncolunas=maiory
        grid = [['.'] * ncolunas for i in range(nlinhas)]   
        for nlinhas in grid:
                print(' '.join([str(elem) for elem in nlinhas]))
                
                
       # return  grid
          
        
        
        
print(modelo(pacman=(1,1),pastilha=(1,6)))     
        

        
        
              
def planeia_online(pacman, pastilha, obstaculos):
    
    pass



def __init__(self, initial=(1, 1), goal=(7, 8), obstacles=()):
        self.initial=initial
        self.goal=goal 
        self.obstacles=set(obstacles) - {initial, goal}
        self.pacman = initial[0]
