

"""
Author: Chelsie Banton
#Part 2: Applications
#Objective:move the stack of disks (as shown in Figure-a) to a rod on the
#extreme right (as shown in Figure-b) following the below mentioned rules
# Only one disk can be moved at a time, A disk cannot be placed over a smaller disk
#Instructions:
Implementation using Stack:
Develop a class StackTower to implement Tower of Hanoi
• You will have to create three stack objects representing the rods
• You need to push the three disk objects onto the rods
• Then you will pop from one rod and push it onto another rod
• Repeat this process while making sure that you are not placing a disk over a smaller
one
Your program should print out the contents of the stack at the beginning. After each move
print out the contents of all the 3 stacks until the final step where the third rod is populated
with all the three disks. Show the simulation of solving Tower of Hanoi.
"""


#Develop a class "Stack Tower" to implement Tower of Hanoi
class StackTower:
    def __init__(self):
        print("Welcome to the Tower of Hanoi")
        print("Objective: Move all disks from Rod A to Rod C")
        print("Original:A=[3,2,1]       B=[]        C=[]")
        print("Goal: A=[]               B=[]        C=[3,2,1]")
        #Create three stack objects,A,B,C to represent rods
        self.A = []
        self.B = []
        self.C = []
    def tower(self, disk): #disk = 3
        self.A.append(disk)
        print("A=",self.A)
        print("Items in Tower A", '\n')

    #it takes 7 moves/passes to win so there will be 7 passes
    def pass1(self):
        #hold will hold popped variables
        self.hold = self.A.pop(2) #A now equals [3,2], self.hold holds [1]
        #append the popped value(1) back on to rod c
        self.C.append(self.hold) #C now equals [1] which is the smallest disk
        print("A=", self.A ,"     " "B=",self.B ,"      ","C=",self.C)
        print('Turn 1 Complete', '\n')
    #2nd pass will move the second disk from Rod A to Rod B
    def pass2(self):
        self.hold = self.A.pop(1) #A now equals [3] which is the biggest disk
        self.B.append(self.hold) #B now equals [2], each rod now has 1 disk
        print("A=", self.A ,"     " "B=",self.B ,"      ","C=",self.C)
        print('Turn 2 Complete', '\n')
    def pass3(self):
        self.hold = self.C.pop(0)#pops [1] from Rod C
        self.B.append(self.hold) #B now equals [2,1]
        print("A=", self.A ,"     " "B=",self.B ,"      ","C=",self.C)
        print('Turn 3 Complete', '\n')
    def pass4(self):
        self.hold = self.A.pop(0)#pops [3] from Rod A
        self.C.append(self.hold) #C now equals [3]
        print("A=", self.A ,"     " "B=",self.B ,"      ","C=",self.C)
        print('Turn 4 Complete', '\n')
    def pass5(self):
        self.hold = self.B.pop(1)#pops [1] from Rod B
        self.A.append(self.hold) #places [1] on rod A
        print("A=", self.A ,"     " "B=",self.B ,"      ","C=",self.C)
        print('Turn 5 Complete', '\n')
    def pass6(self):
        self.hold = self.B.pop(0)#pops [2] from Rod B
        self.C.append(self.hold) #places [2] on rod C
        print("A=", self.A ,"     " "B=",self.B ,"      ","C=",self.C)
        print('Turn 6 Complete', '\n')
    def pass7(self):
        self.hold = self.A.pop(0)#pops [1] from Rod A
        self.C.append(self.hold) #places [1] on rod C
        print("A=", self.A ,"     " "B=",self.B ,"      ","C=",self.C)
        print('Turn 7 Complete', '\n')






moves= StackTower()
moves.tower(3)
moves.tower(2)
moves.tower(1)
moves.pass1()
moves.pass2()
moves.pass3()
moves.pass4()
moves.pass5()
moves.pass6()
moves.pass7()
print("Goal Accomplished")
