from classDefinitions import Storage, Door

def cmd_unlock(currentRoom, playerCommand, playerInventory):
    uObject = playerCommand[7:].lower()
    if uObject in ['north door', 'east door', 'south door', 'west door', 'north', 'east', 'south', 'west']:
        myEnum = {'north door': currentRoom._n, 'north': currentRoom._n, 'east door': currentRoom._e, 'east': currentRoom._e, 
                    'south door': currentRoom._s, 'south': currentRoom._s, 'west door': currentRoom._w, 'west': currentRoom._w}
        wDoor = myEnum[uObject]
        if not isinstance(wDoor, Door):
            print("That is not a door you can unlock.")
            return
        inputKey = input("What will you use to unlock this door?\n>").lower()
        completed = False
        for eachObject in playerInventory:
            if inputKey == eachObject._name.lower():
                try:
                    wDoor.unlockDoor(eachObject)
                    completed = True
                    break
                except:
                    print("You couldn't unlock that object because the key was wrong or the object wasn't locked.")
                    completed = True
                    break
        if completed != True:
            print(f"There is no such object with name {inputKey}")
    elif uObject in ['vents', 'vent', 'vent cover', 'air vents']:
        wDoor = currentRoom._e
        inputKey = input("What will you use to break open this vent?\n>").lower()
        completed = False
        for eachObject in playerInventory:
            if inputKey == eachObject._name.lower():
                try:
                    wDoor.unlockDoor(eachObject)
                    completed = True
                    break
                except:
                    print("You couldn't unlock that object because the key was wrong or the object wasn't locked.")
                    completed = True
                    break
        if completed != True:
            print(f"There is no such object with name {inputKey}")
    else:
        completed = False
        for eachObject in currentRoom._objects:
            if not isinstance(eachObject, Storage):
                continue
            if uObject == eachObject._name.lower():
                inputKey = input("What will you use to unlock this container?\n>").lower()
                completed1 = False
                for eachKey in playerInventory:
                    if inputKey == eachKey._name.lower():
                        eachObject.unlockContainer(eachKey)
                        completed1 = True
                        completed = True
                        break
                if completed1 != True:
                    print(f"There is no such object with name {inputKey}")
                    completed = True
        if completed != True:
            print('You need to specify a door or container to unlock. For doors, specify in the fashion \'north door\' or \'north\'. For a container, just specify it\'s name')