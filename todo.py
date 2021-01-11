
import os
import sys
import json
from datetime import date 

# function to create a file to store data
def filecreation(DIR):
    if 'data.txt' in os.listdir(DIR):
        return
    with open('data.json', 'w') as fp: 
        fp.write(json.dumps([], indent=4))
    dir_list = os.listdir(DIR) 

def write_json(data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 


def main():
    arguments = list(sys.argv)
    DIR = os.path.dirname(os.path.realpath(__file__))
    if 'data.json' not in list(os.listdir()):
        filecreation(DIR)
    #./todo and ./todo help
    if len(arguments) == 1 or (len(arguments)==2 and arguments[1] == 'help'):
        print('Usage :-')
        print('$ ./todo add \"todo item\"  # Add a new todo')
        print('$ ./todo ls               # Show remaining todos')
        print('$ ./todo del NUMBER       # Delete a todo')
        print('$ ./todo done NUMBER      # Complete a todo')
        print('$ ./todo help             # Show usage')
        print('$ ./todo report           # Statistics"')
        exit()
    elif len(arguments) > 1:
        #./todo add
        if arguments[1] == 'add' and len(arguments) == 3:
            dataval = {"todo":arguments[2], "status":"not done"}
            with open("data.json") as f:
                data = json.load(f)
            datacheck = []
            count = 1
            for i in range(len(data)-1,-1,-1):
                if dataval['todo'] == data[i]['todo']:
                    count += 1
            if count == 1:
                data.append(dataval)
                json.dumps(data, indent=4)
                write_json(data)
            print('Added todo: '+'"'+arguments[2]+'"')
            exit()
        elif arguments[1] == 'add' and len(arguments) != 3:
            print('Error: Missing todo string. Nothing added!')
        
        #./todo ls
        elif arguments[1] == 'ls':
            with open("data.json") as fview:
                data = json.load(fview)
            datacheck = []
            datalist = []
            count = 1
            datachecknum = 0
            for i in range(len(data)-1,-1,-1):
                if data[i] not in datacheck and (data[i]['status'] == 'not done'):
                    datacheck.append(data[i])
                    datachecknum += 1
                    count += 1
            if datachecknum == 0:
                print('There are no pending todos!')
            else:
                count1 = count
                for i in range (count-1):
                    print('['+str(count1-1)+'] '+datacheck[i]['todo'])
                    count1 -= 1
                
        #./todo del
        elif arguments[1] == 'del' and len(arguments) == 3:
            with open("data.json") as fdel:
                data = json.load(fdel)
            x = int(arguments[2])
            if x > len(data) or x<1:
                print('Error: todo #'+str(x)+' does not exist. Nothing deleted.')
            else:
                datadel = data[-int(arguments[2])]
                data.remove(datadel)
                write_json(data)
                print('Deleted todo #'+arguments[2])

        elif arguments[1] == 'del' and len(arguments) != 3:
            print("Error: Missing NUMBER for deleting todo.")

        #./todo done
        elif arguments[1] == 'done' and len(arguments) != 3:
            print("Error: Missing NUMBER for marking todo as done.")
        elif arguments[1] == 'done' and len(arguments) == 3:
            with open("data.json") as fdone:
                data = json.load(fdone)
            if len(data) >= int(arguments[2]) and int(arguments[2]) != 0:
                data[int(arguments[2])-1]['status'] = 'done'
                write_json(data)
                print('Marked todo #'+str(arguments[2])+' as done.')
            else :
                print('Error: todo #'+str(arguments[2])+' does not exist.')
            

        #./todo report
        elif arguments[1] == 'report':
            with open("data.json") as freport:
                data = json.load(freport)
            todo = 0
            done = 0
            for val in data:
                if val['status'] == "not done":
                    todo += 1
                if val['status'] == "done":
                    done += 1
            print(str(date.today())+' Pending : '+str(todo)+' Completed : '+str(done))




main()