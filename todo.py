# pip install redis
import redis
import json
from typing import List
r = redis.Redis()


class Task():
    def __init__(self, id:int, title:str, completed: bool):
        self.id = id
        self.title = title
        self.completed = completed     


def objectify(tasks: List[Task]):
    return list(
        map(
            lambda t: {
                "id": t.id,
                "title": t.title,
                "completed": t.completed
            },
            tasks
        ),
    )

def TaskToJson(task:Task):
    return { "id": task.id, "title": task.title, "completed": task.completed }

def writeToPersist(data):
    with open('db.json', 'w') as f:
        # if(f.tell() == 0):
        json.dump(data,f, indent=4, sort_keys=True)
    r.set('data',json.dumps(data, indent=4, sort_keys=True))
    pass

def readFromPersist():
    with open('db.json', 'r') as f:
        task_from_redis = r.get('data')
        if(f.tell() !=0):
            # Reading from json file 
            task_list = json.load(f)
            data = task_list
        elif(task_from_redis):
            task_list = r.get('data')
            data = json.loads(task_list)
        else:
            data = {"data":[]}
    return data        


def printListTodo():
    task_list = readFromPersist()
    if (task_list['data'] == []):
        print("You Didn't Have Task Yet Please Add New One")
    else:
        print(" Task Todo Today is ")
        for i in range(len(task_list['data'])):
            print(f'\t {i+1}. {task_list["data"][i]["title"]} ')
    pass


if __name__ == '__main__':
    q=0
    while True:
        print()
        printListTodo()
        print('Do you want to Add or Remove Task')
        print('If u want to Add Enter : add')
        print('If u want to Remove Enter : remove')
        print('If u want to Quit a Program Enter : q')
        choice = input('Your Input : ')
        task_list = readFromPersist()
        if(choice  == 'add' and task_list['data'] !=[]):
            task_title ='Title'
            index_new_task = 1
            while True:
                title_task:str = input(f'{index_new_task}. ')
                if(title_task == ''):
                    break
                index_new_task+=1
                range_list = len(task_list['data'])
                last_id = task_list['data'][range_list-1]['id']
                new_task = Task( id=last_id+1, title=title_task, completed= False)
                task_list['data'].append(TaskToJson(new_task))
                writeToPersist(task_list)
        elif(choice == 'remove'):
            if(task_list['data'] ==[]):
                pass
            else:
                printListTodo()
                index_remove = int(input('Select Task Which you want to remove : '))
                task_list['data'].pop(index_remove-1)
                writeToPersist(task_list)
            pass
        elif(choice == 'add' and task_list['data'] ==[]):
            # If Task List is Null
            task_title ='Title'
            index_new_task = 1
            while True:
                title_task:str = input(f'{index_new_task}. ')
                if(title_task == ''):
                    break
                new_task = Task( id=index_new_task, title=title_task, completed= False)
                index_new_task+=1
                task_list['data'].append(TaskToJson(new_task))
                writeToPersist(task_list)
        elif(choice == 'q'):
            break
        pass
