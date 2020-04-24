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
            description = input("Beskriv uppgiften: ")
            message = input("Du skrev '{}' är det OK? [j/n]: ".format(description))
            if message == "j":
                tasklist = TaskList(len(self.tasklist))
                task, id = tasklist.create_task(description)
                self.tasklist.append((task, id))
                tasklist.task_counter += 1
                return tasklist.task_counter
                break
            else:
                break


    def show_tasks(self):
        for task in self.tasklist:
            print(task)

    def mark_done(self):
        return

    def main(self):
        while True:
            user_input = input("Ange kommando (q = avsluta, ? = hjälp): ").lower()
            if user_input == "q":
                break
            try:
                self.commands[user_input]()
            except KeyError:
                print("Okänt kommando.")


class TaskList(object):

    def __init__(self, task_counter = 0):
        self.task_counter = task_counter

    def create_task(self, description):
        task_id = self.task_counter
        task = Task(task_id)
        task.description = description
        return task.description, task.task_id

    def mark_done(self, task_id):
        task = Task(task_id)
        return task.mark_done           # bool()


class Task(object):

    def __init__(self, task_id):
        self.task_id = task_id          # int
        self.description = ""           # str
        self.done = False               # boolean

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
