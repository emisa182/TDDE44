#!/usr/bin/env python3
import sys

class TodoApp(object):

    def __init__(self):
        self.tasklist = []
        self.commands = {"?" : self.show_commands, "visa" : self.show_tasks,
                         "klar" : self.mark_done, "ny" : self.new_task}


    def show_commands(self):
        print("Kommandon: ny, visa, klar, ?, q")
        return


    def new_task(self):
        while True:
            description = input("Beskriv uppgiften:")
            print(type(description))
            message = input("Du skrev '{}' är det OK? [j/n]:".format(description))
            if message == "j":
                tasklist = TaskList()
                task = tasklist.create_task(description) #förhoppningsvis gör den vad den ska
                self.tasklist.append(task)
                break
            else:
                break


    def show_tasks(self):
        for task in self.tasklist:
            print(task)
        return

    def mark_done(self):
        return

    def main(self):
        while True:
            user_input = input("Ange kommando (q = avsluta, ? = hjälp):").lower()
            if user_input == "q":
                break
            try:
                self.commands[user_input]()
            except KeyError:
                print("Okänt kommando.")


class TaskList(object):

    def __init__(self, task_counter = 0):
        self.task_counter = task_counter
        return

    def create_task(self, description):
        self.task_counter += 1
        task_id = self.task_counter
        task = Task(task_id)
        task.description = description
        return task.description

    def mark_done(self, task_id):
        task = Task(task_id)
        return task.mark_done           # bool()


class Task(object):

    def __init__(self, task_id):
        self.task_id = task_id          # int
        self.description = ""           # str
        self.done = False               # boolean

        return


    def mark_done(self):
        self.done = True
        return self.done

#tasklist = TaskList()
#print(tasklist.create_task("Koka kaffe"))

#task = Task(1)
#print(task.done)
#print(tasklist.mark_done(1))
if __name__ == "__main__":
    app = TodoApp()
    app.main()
