class testMaps:
    
    def __init__(self):
        pass
    
    def test(self):
        contador = 1
        with open ("./src/Maps/map.txt","w") as file:
            for i in range (1,37):
                for j in range (1,100):
                    file.write(str(contador)+",")
                    contador =contador +1
            file.write("\n")    
t = testMaps()         
t.test()    