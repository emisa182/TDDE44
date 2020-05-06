#!/usr/bin/env python3


class TodoApp(object):
    """Skapa en att-göra-lista.

    tasklist -- En lista av listor som innehåller beskrivning,
                ID och om uppgiften är gjord.
    commands -- Möjliga inputs för att använda programmet.
    """

    def __init__(self):
        """Skapa uppgiftslista samt kommandon."""
        self.tasklist = TaskList()                                          # egen
        self.commands = {"?": self.show_commands, "visa": self.show_tasks,
                         "klar": self.mark_done, "ny": self.new_task}       # egen


    def show_commands(self):                                                #bra
        """Skriv ut möjliga kommandon."""
        print("Kommandon: ny, visa, klar, ?, q")

    def new_task(self):
        """Skapa ny uppgift."""
        while True:
            description = input("Beskriv uppgiften: ")
            message = \
                input("Du skrev '{}' är det OK? [j/n]: ".format(description))
            if message == "j":
                #få tas_counter att räkna upp
                #tasklist = TaskList(len(self.tasklist))
                self.tasklist.create_task(description)
                break
            else:
                break

    def show_tasks(self):                       #taskcounter räknar ej upp och det markeras inte som klart.
        """Visa uppgifterna."""
        self.tasklist.is_it_done()

    def mark_done(self):
        """Markera uppgiften som klar."""
        while True:
            task_id = input("Vilken uppgift ska markeras som klar? ")
            if task_id == "q":
                break
            try:
                if int(task_id) < len(self.tasklist.task_list):
                    self.tasklist.mark_done(task_id)
                    #task = self.tasklist[int(task_id)]  #borde vara instans
                    #uppg = TaskList(int(task_id))
                    #task[2] = bool(uppg.mark_done(int(task_id)))
                    break
                else:
                    print("Finns ej i listan.")
            except ValueError:
                print("Du måste skriva en siffra.")

    def main(self):                                                     #bra
        """Kör interaktionsloopen och ta emot kommandon."""
        while True:
            user_input = \
                input("Ange kommando (q = avsluta, ? = hjälp): ").lower()
            if user_input == "q":
                break
            try:
                self.commands[user_input]()
            except KeyError:
                print("Okänt kommando.")


class TaskList(object):
    """Skapa uppgifter till en att-göra-lista.

    task_counter -- En siffra vi kan använda till uppgifts-ID
    """

    def __init__(self):
        """Ta in en siffra som kan användas som ID-nummer."""
        self.task_list = []
        self.task_counter = len(self.task_list)

    def create_task(self, description):
        """Skapa en uppgift och ge den ett ID-nummer."""
        task_id = self.task_counter
        task = Task(task_id)
        task.description = description
        self.task_list.append(task)

    def mark_done(self, task_id):
        """Markera uppgiften som färdig."""
        task = Task(task_id)
        task.mark_done()

    def is_it_done(self):
        for task in self.task_list:
            frase = "{}. [{}] {}. "

            if task.done == True:
                print(frase.format(task.task_id, "X", task.description))
            else:
                print(frase.format(task.task_id, " ", task.description))

class Task(object):
    """Definiera uppgiften som ska läggas till i att-göra-listan.

    task_id     -- Uppgiftens ID
    description -- Beskriving av uppgiften
    done        -- Beskriver om uppgiften är klar eller inte
    """

    def __init__(self, task_id):
        """Definiera uppgifts-ID, uppgifts-beskrivning och om den är gjord."""
        self.task_id = task_id          # int
        self.description = ""           # str
        self.done = False               # boolean

    def mark_done(self):
        """Markera uppgiften som färdig."""
        self.done = True


if __name__ == "__main__":
    app = TodoApp()
    app.main()
