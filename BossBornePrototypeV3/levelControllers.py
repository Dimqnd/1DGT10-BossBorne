# ALWAYS ONLY EVER RUN FROM THIS FILE!!!!

from levels.level0 import run_level0
from levels.level1 import run_level1
from levels.level2 import run_level2
from levels.level3 import run_level3
from levels.level4 import run_level4
import json
import os

currentLevel = 0
levelInfoDir = "levels\\levelInformation.json"

levelIndex = {
    0: run_level0,
    1: run_level1,
    2: run_level2, 
    3: run_level3,
    4: "unavaliable"
}

if __name__ == "__main__":
    runIndex = int(input("Enter an index to run the level: "))
    currentLevel = runIndex
    runInstance = levelIndex[runIndex]
    if isinstance(runInstance, str):
        os.system('cls||clear')
        print(runInstance)
        quit()
    else:
        os.system('cls||clear')
        tempJson = {"currentLevel": runIndex}
        with open(levelInfoDir, "w") as f: 
            json.dump(tempJson, f)
        runInstance()