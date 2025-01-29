import maya.cmds as cmds
import random as rnd
from random import randrange
import math

# File path of the OBJ
obj_file1 = 'D:\\Uni\\Work\\Technical Arts Production\\Coding MAYA\\Objects\\Roof.obj'
obj_file2 = 'D:\\Uni\\Work\\Technical Arts Production\\Coding MAYA\\Objects\\Roof_Corner.obj'
obj_file3 = 'D:\\Uni\\Work\\Technical Arts Production\\Coding MAYA\\Objects\\Window.obj'

# Import the OBJ file
import_node1 = cmds.file(obj_file1, i=True, type='OBJ', rnn=True)
import_node2 = cmds.file(obj_file2, i=True, type='OBJ', rnn=True)
import_node3 = cmds.file(obj_file3, i=True, type='OBJ', rnn=True)

# Rename the imported object
imported_object1 = cmds.ls(import_node1, dag=True)[0]
imported_object2 = cmds.ls(import_node2, dag=True)[0]
imported_object3 = cmds.ls(import_node3, dag=True)[0]

print(f"Imported and duplicated {obj_file1}.")

def buildBuildings(wBlock, dBlock, blockHeight):
    print(wBlock, dBlock, blockHeight)
    
    #How many times the code has looped in sections
    temp = 0
    Rec = 0
    Loop = 0
    
    #create the plane base of the cityblock
    blockBase = cmds.polyPlane(name="blockBase", width=wBlock+3, height=dBlock+3)
    
    #
    #
    #    This Section is for the creation building body and Roof
    #
    #
    
    #This is for the front and back
    for i in range(0,2):
        #Randomises how many buildings make up the left and right side
        tempL = randrange(3,math.floor(wBlock/2)+1)
        tempR = randrange(3,math.floor(wBlock/2))
        print(tempL)
        print(tempR)
        print(wBlock)
        #Finds the gap size
        gapSize = wBlock - (tempL+tempR)
        for i in range(0, tempL):
            #This generates and moves the buildings
            building = cmds.polyCube(name="Building", width=wBlock/wBlock, height=blockHeight, depth=dBlock/dBlock)
            if Rec == 0:
                cmds.move(temp-(wBlock/2)+1,blockHeight/2,dBlock/2,building)
            if Rec == 1:
                cmds.move((temp-(wBlock/2))+1,blockHeight/2,0-(dBlock/2),building)
            #This Generates and moves the rooves
            Roof = cmds.duplicate(imported_object1, name='Roof')
            if Rec == 0:
                cmds.move(temp-(wBlock/2)+1,blockHeight+0.5,dBlock/2,Roof)
                cmds.rotate(0,90,0,Roof)
                cmds.scale(0.5,0.5,0.5,Roof)
            if Rec == 1:
                cmds.move((temp-(wBlock/2))+1,blockHeight+0.5,0-(dBlock/2),Roof)
                cmds.rotate(0,90,0,Roof)
                cmds.scale(0.5,0.5,0.5,Roof)
            #This Generates and moves the Window
            for i in range(0, blockHeight-1):
                Window = cmds.duplicate(imported_object3, name='Window')
                if Rec == 0:
                    cmds.move(temp-(wBlock/2)+1,1.5+Loop,(dBlock/2)+1,Window)
                    cmds.rotate(0,270,0,Window)
                    cmds.scale(0.5,0.5,0.5,Window)
                if Rec == 1:
                    cmds.move((temp-(wBlock/2))+1,1.5+Loop,(0-(dBlock/2))-1,Window)
                    cmds.rotate(0,90,0,Window)
                    cmds.scale(0.5,0.5,0.5,Window)
                Loop += 1
            Loop = 0
            temp += 1
        temp += gapSize
        for i in range(0, tempR):
            #This generates and moves the buildings
            building = cmds.polyCube(name="Building", width=wBlock/wBlock, height=blockHeight, depth=dBlock/dBlock)
            if Rec == 0:
                cmds.move(temp-(wBlock/2),blockHeight/2,dBlock/2,building)
            if Rec == 1:
                cmds.move(temp-(wBlock/2),blockHeight/2,0-(dBlock/2),building)
            #This Generates and moves the rooves
            Roof = cmds.duplicate(imported_object1, name='Roof')
            if Rec == 0:
                cmds.move(temp-(wBlock/2),blockHeight+0.5,dBlock/2,Roof)
                cmds.rotate(0,90,0,Roof)
                cmds.scale(0.5,0.5,0.5,Roof)
            if Rec == 1:
                cmds.move(temp-(wBlock/2),blockHeight+0.5,0-(dBlock/2),Roof)
                cmds.rotate(0,90,0,Roof)
                cmds.scale(0.5,0.5,0.5,Roof)
            #This Generates and moves the Window
            for i in range(0, blockHeight-1):
                Window = cmds.duplicate(imported_object3, name='Window')
                if Rec == 0:
                    cmds.move(temp-(wBlock/2),1.5+Loop,(dBlock/2)+1,Window)
                    cmds.rotate(0,270,0,Window)
                    cmds.scale(0.5,0.5,0.5,Window)
                if Rec == 1:
                    cmds.move(temp-(wBlock/2),1.5+Loop,(0-(dBlock/2))-1,Window)
                    cmds.rotate(0,90,0,Window)
                    cmds.scale(0.5,0.5,0.5,Window)
                Loop += 1
            Loop = 0
            temp += 1
        temp = 0
        Rec += 1
    #Loop End
    
    gapSize = 0
    temp = 0
    Rec = 0
    
    ##This is for the left and right
    for i in range(0,2):
        #Randomises how many buildings make up the left and right side
        tempL = randrange(3,math.floor(dBlock/2)+1)
        tempR = randrange(3,math.floor(dBlock/2))
        print(tempL)
        print(tempR)
        #Finds the gap size
        gapSize = dBlock - (tempL+tempR)
        for i in range(0, tempL):
            #This generates and moves the buildings
            building = cmds.polyCube(name="Building", width=wBlock/wBlock, height=blockHeight, depth=dBlock/dBlock)
            if Rec == 0:
                cmds.move(wBlock/2,blockHeight/2,temp-(dBlock/2)+1,building)
            if Rec == 1:
                cmds.move(0-(wBlock/2),blockHeight/2,(temp-(dBlock/2))+1,building)
            #This Generates and moves the rooves
            Roof = cmds.duplicate(imported_object1, name='Roof')
            if Rec == 0:
                cmds.move(wBlock/2,blockHeight+0.5,temp-(dBlock/2)+1,Roof)
                cmds.scale(0.5,0.5,0.5,Roof)
            if Rec == 1:
                cmds.move(0-(wBlock/2),blockHeight+0.5,(temp-(dBlock/2))+1,Roof)
                cmds.scale(0.5,0.5,0.5,Roof)
            #This Generates and moves the Window
            for i in range(0, blockHeight-1):
                Window = cmds.duplicate(imported_object3, name='Window')
                if Rec == 0:
                    cmds.move((wBlock/2)+1,1.5+Loop,temp-(dBlock/2)+1,Window)
                    cmds.scale(0.5,0.5,0.5,Window)
                if Rec == 1:
                    cmds.move((0-(wBlock/2))-1,1.5+Loop,(temp-(dBlock/2))+1,Window)
                    cmds.rotate(0,180,0,Window)
                    cmds.scale(0.5,0.5,0.5,Window)
                Loop += 1
            Loop = 0
            temp += 1
        temp += gapSize
        for i in range(0, tempR):
            #This generates and moves the buildings
            building = cmds.polyCube(name="Building", width=wBlock/wBlock, height=blockHeight, depth=dBlock/dBlock)
            if Rec == 0:
                cmds.move(wBlock/2,blockHeight/2,temp-(dBlock/2),building)
            if Rec == 1:
                cmds.move(0-(wBlock/2),blockHeight/2,temp-(dBlock/2),building)
            #This Generates and moves the rooves
            Roof = cmds.duplicate(imported_object1, name='Roof')
            if Rec == 0:
                cmds.move(wBlock/2,blockHeight+0.5,temp-(dBlock/2),Roof)
                cmds.scale(0.5,0.5,0.5,Roof)
            if Rec == 1:
                cmds.move(0-(wBlock/2),blockHeight+0.5,temp-(dBlock/2),Roof)
                cmds.scale(0.5,0.5,0.5,Roof)
            #This Generates and moves the Window
            for i in range(0, blockHeight-1):
                Window = cmds.duplicate(imported_object3, name='Window')
                if Rec == 0:
                    cmds.move((wBlock/2)+1,1.5+Loop,temp-(dBlock/2),Window)
                    cmds.scale(0.5,0.5,0.5,Window)
                if Rec == 1:
                    cmds.move((0-(wBlock/2))-1,1.5+Loop,temp-(dBlock/2),Window)
                    cmds.rotate(0,180,0,Window)
                    cmds.scale(0.5,0.5,0.5,Window)
                Loop += 1
            Loop = 0
            temp += 1
        temp = 0
        Rec += 1
    #Loop End
    
    Rec = 0
    
    #The Corner building creation
    for i in range(0,4):
        building = cmds.polyCube(name="Building", width=wBlock/wBlock, height=blockHeight, depth=dBlock/dBlock)
        if Rec == 0:
            cmds.move(wBlock/2,blockHeight/2,dBlock/2,building)
        if Rec == 1:
            cmds.move(0-(wBlock/2),blockHeight/2,dBlock/2,building)
        if Rec == 2:
            cmds.move(wBlock/2,blockHeight/2,0-(dBlock/2),building)
        if Rec == 3:
            cmds.move(0-(wBlock/2),blockHeight/2,0-(dBlock/2),building)
        Rec += 1
    Rec = 0
    #The Corner building rooves creation
    for i in range(0,4):
        Roof_Corner = cmds.duplicate(imported_object2, name='Roof_Corner')
        #Front Right
        if Rec == 0:
            cmds.move(wBlock/2,blockHeight+0.5,dBlock/2,Roof_Corner)
            cmds.scale(0.5,0.5,0.5,Roof_Corner)
            cmds.rotate(0,270,0,Roof_Corner)
        #Front Left
        if Rec == 1:
            cmds.move(0-(wBlock/2),blockHeight+0.5,dBlock/2,Roof_Corner)
            cmds.scale(0.5,0.5,0.5,Roof_Corner)
            cmds.rotate(0,180,0,Roof_Corner)
        #Back Right
        if Rec == 2:
            cmds.move(wBlock/2,blockHeight+0.5,0-(dBlock/2),Roof_Corner)
            cmds.scale(0.5,0.5,0.5,Roof_Corner)
        #Back Left
        if Rec == 3:
            cmds.move(0-(wBlock/2),blockHeight+0.5,0-(dBlock/2),Roof_Corner)
            cmds.scale(0.5,0.5,0.5,Roof_Corner)
            cmds.rotate(0,90,0,Roof_Corner)
        Rec += 1
    #End
    
    cmds.delete('Mesh')
    cmds.delete('Roof_Corner_Mesh')
    cmds.delete('Window_Mesh')

# Reset all dynamic variables to zero
gapSize = 0
temp = 0
Rec = 0
Loop = 0

# Defines the OK button's action
def actionProc(winID, wBlock, dBlock, blockHeight, *pArgs):
    print ("Start action")
    cmds.deleteUI(winID)
    
    #Run Main Function
    buildBuildings(wBlock, dBlock, blockHeight)

# Defines the menu's cancel button's
def cancelProc(winID, *pArgs):
    print ("action is cancelled")
    cmds.deleteUI(winID)
    
# Creates the initial window for users to customise the blocks generation
def createUI():	
    winID = "CityBlock"
    if cmds.window(winID, exists=True):
        print("deleteUI", winID)
        cmds.deleteUI(winID)
        
    winName = cmds.window(winID, title = "City Block Generator", resizeToFitChildren=True)
    cmds.columnLayout()
    
    blockHeightControl = cmds.intSliderGrp(label='The max Building Height', minValue=1, maxValue=20, value=3, field=True)
    wblockControl = cmds.intSliderGrp(label='The max area Width', minValue=8, maxValue=20, value=8, field=True)
    dblockControl = cmds.intSliderGrp(label='The max area Depth', minValue=8, maxValue=20, value=8, field=True)
    
    print("Dimensions",blockHeightControl, wblockControl, dblockControl)
    
    # THE OK AND CANCEL BUTTONS
    cmds.button(label = "OK", command = lambda *args: actionProc(winID, cmds.intSliderGrp(wblockControl, query=True, value=True), cmds.intSliderGrp(dblockControl, query=True, value=True), cmds.intSliderGrp(blockHeightControl, query=True, value=True)))
    cmds.button(label = "Cancel", command = lambda *args: cancelProc(winID))
    
    cmds.showWindow()

if __name__ == "__main__":
	createUI()
