class Character ():
    
    '''
    Tiene que tener unas coordenadas de inicio
    un personaje se puede mover
    un personaje tiene una representación 
    un personaje puede tener sprite y se puede gestionar desde aquí
    
    '''
    
    def __init__(self,x=10,y=10, direction='right'):
        self.x
        self.y
        self.direction = direction
        pass
    
    
    def movements(self):
        
        if (self.direction == 'right'):
            self.x += 5
            
        ''' hay que seguir poniendo direcciones'''    