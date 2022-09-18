import sys
sys.path.append('c:\\users\\dougl\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import clipboard
import json


SAVED_DATA = "clipboard.json"

def saveData(filepath,data):
    with open(filepath, "w") as f:
        json.dump(data,f)

def loadData(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}

if len(sys.argv) == 2:

    command = sys.argv[1]
    data = loadData(SAVED_DATA)

    if command == "save":
        key = input("Enter a key to associate your clipboard with: ")
        data[key] = clipboard.paste()
        saveData(SAVED_DATA,data)
        print("Data Saved!")
    elif command == "list":
        print(data)
    elif command == "load":
        key = input("Enter your key:")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("key does not exist")
                  
    else:
        print("Unknown Command")
else:
    print("Please pass exactly one command")
