from os import system
from time import sleep
import re


class Programming:
    def __init__(self):
        system("cls")
        system("color d")
        self.page = """
                            X       X  XXXXXXXXXXX   X           X                XXXXXXXXXX
                            X       X  X             X           X               X          X
                            X       X  X             X           X               X          X
                            XXXXXXXXX  XXXXXXX       X           X               X          X
                            X       X  X             X           X               X          X
                            X       X  X             X           X               X          X
                            X       X  XXXXXXXXXXX   XXXXXXXXXX  XXXXXXXXXXX      XXXXXXXXXX

                            code:
                                    exit
                                    help
                                    type---> int,string,double,bool
                                    example:  25+50=75 ☻

        """
        self.dictionary = {}
        print(self.page)
        sleep(3)
        print("starting code ...")
        sleep(3)
        system("cls")
        print("ok...")
        self.start()
    # start

    def start(self):
        system("color d")
        self.inpt = input("--->")
        if self.inpt.strip() != "":
            self.control()
        else:
            print("please not empty code ☻")
        self.start()
        self.array.clear()
    # control

    def control(self):
        self.symbol()
        b = self.inpt.replace("=", " = ")
        b = b.split()
        if self.inpt.lower() == "exit":
            system("cls")
            system("color c")
            print("system exit")
            sleep(2)
            exit()
        elif self.inpt.lower() == "clear":
            self.dictionary.clear()
            system("cls")
        elif self.inpt.lower() == "help":
            system("cls")
            print(self.help())
        else:
            if len(b) == 1:
                if self.inpt.isdigit():
                    print(self.inpt)
                else:
                    a = self.dictionary.get(b[0])
                    if a != None:
                        print(a)
                    else:
                        print(self.inpt+" not defined!")
            else:
                self.smash()

    def smash(self):
        self.array = re.split(' |=', self.inpt)
        if self.type() is not None:
            try:
                self.add()
            except:
                print("add error code !")
        elif self.update() is not None:
            self.dictionary[self.array[0]] = self.array[1]
        else:
            self.search()

    def search(self):
        if str(self.array[0]).isdigit() and str(self.array[2]).isdigit():
            print(self.math())
        elif str(self.array[0]).isdigit():
            self.x = self.dictionary.get(self.array[2])
            if self.x != None:
                self.array[2] = self.x
                self.search()
            else:
                print("not found")
        elif str(self.array[2]).isdigit():
            self.x = self.dictionary.get(self.array[0])
            if self.x != None:
                self.array[0] = self.x
                self.search()
            else:
                print("not found")
        else:
            self.x = self.dictionary.get(self.array[0])
            self.y = self.dictionary.get(self.array[2])
            if self.x == None or self.y == None:
                print("not defined!")
            else:
                self.array[0] = self.x
                self.array[2] = self.y
                if str(self.array[0]).isdigit() and str(self.array[2]).isdigit():
                    print(self.math())
                else:
                    print(self.array[0]+self.array[2])

    def add(self):
        if len(self.array) >= 3:
            if self.type() == 1:
                try:
                    self.dictionary[self.array[1]] = int(self.array[2])
                except:
                    print("types error!")
            elif self.type() == 2:
                i = 2
                kelime = ""
                while i < len(self.array):
                    kelime += self.array[i]+" "
                    i += 1
                self.dictionary[self.array[1]] = kelime
            else:
                self.dictionary[self.array[1]] = self.array[2]

        elif len(self.array) == 3:
            self.dictionary[self.array[1]] = self.array[2]
        else:
            print("code error!")
        self.start()

    def update(self):
        return self.dictionary.get(self.array[0])

    def symbol(self):
        if self.inpt.find("+") > 0:
            self.inpt = self.inpt.replace("+", " + ")
        elif self.inpt.find("-") > 0:
            self.inpt = self.inpt.replace("-", " - ")
        elif self.inpt.find("*") > 0:
            self.inpt = self.inpt.replace("*", " * ")
        elif self.inpt.find("/") > 0:
            self.inpt = self.inpt.replace("/", " / ")

    def type(self):
        return{
            "int": 1,
            "string": 2,
            "bool": 3,
        }.get(self.array[0], None)

    def help(self):
        return """
        help:
        **type
        int
        string
        bool 
        double
                        ------------------------------------------
                        int a=5
                        int c=25
                         a+c
                         |
                         |
                         |
                         V
                       output:30
                        ------------------------------------------
                        string words="hello world"
                         words
                         |
                         |
                         |
                         V
                        output: hello world
                        ------------------------------------------
                        bool a=false
                         a
                         |
                         |
                         |
                         V
                       output:false
                       ------------------------------------------
                        double a=5.25
                        double b=6.75
                         a+b
                         |
                         |
                         |
                         V
                       output:12.0
                       ------------------------------------------
                        exit
                            system close
                        clear 
                            code clear

            """

    def math(self):
        a = int(self.array[0])
        b = int(self.array[2])
        if self.array[1] == "+":
            return a+b
        elif self.array[1] == "-":
            return a-b
        elif self.array[1] == "/":
            try:
                return a/b
            except:
                print("math error num/zero")
        elif self.array[1] == "*":
            return a*b
        else:
            system("color c")
            return "error code"
            sleep(1)


if __name__ == '__main__':
    Programming()
