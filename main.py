import os

class Player:
    def __init__(self):
        pass


class GameRenderer():
    def __init__(self, __width: int, __height: int):
        self.is_running = True
        self.__width = __width
        self.__height = __height

    def getHeight(self):
        return self.__height

    def setHeight(self, __height: int):
        self.__height = __height
        return self.__height

    def getWidth(self):
        return self.__width

    def setWidth(self, __width: int):
        self.__width = __width
        return self.__width


    def create2D_List(self):
        self.height_list = []
        
        for element in range(0, (self.__width)):
            self.width_list = [0] * self.__width
            self.height_list.append(self.width_list)
        
        for row in self.height_list:
            if row[0] == 0 or row[len(row-1)-1]:
                row[0] = "|"
                row[len(row)-1] = "|"
                for element in range(1, len(row)-1):
                    row[element] = ""

            #print(row)
        return self.height_list
            
            
    def gameLoop(self):
        while self.is_running == True:
            os.system('clear')
            for row in self.height_list:
                print(row)
            

render = GameRenderer(20, 0)
render.create2D_List()
render.gameLoop()