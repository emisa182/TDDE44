#!/usr/bin/env python3


class TodoApp(object):
    """Skapa en att-göra-lista.

    tasklist -- En lista av listor som innehåller beskrivning,
                ID och om uppgiften är gjord.
    commands -- Möjliga inputs för att använda programmet.
    """

    def __init__(self):
        """Skapa uppgiftslista samt kommandon."""
        self.tasklist = []                                                  # egen
        self.commands = {"?": self.show_commands, "visa": self.show_tasks,
                         "klar": self.mark_done, "ny": self.new_task}       # egen

    def show_commands(self):
        """Skriv ut möjliga kommandon."""
        print("Kommandon: ny, visa, klar, ?, q")

    def new_task(self):
        """Skapa ny uppgift."""
        while True:
            description = input("Beskriv uppgiften: ")
            message = \
                input("Du skrev '{}' är det OK? [j/n]: ".format(description))
            if message == "j":
                tasklist = TaskList(len(self.tasklist))
                task = tasklist.create_task(description)
                self.tasklist.append((task))
                break
            else:
                break

    def show_tasks(self):
        """Visa uppgifterna."""
        for task in self.tasklist:
            frase = "{}. [{}] {}. "
            if task[2] == True:
                print(frase.format(task[1], "X", task[0]))
            else:
                print(frase.format(task[1], " ", task[0]))

    def mark_done(self):
        """Markera uppgiften som klar."""
        while True:
            task_id = input("Vilken uppgift ska markeras som klar? ")
            if task_id == "q":
                break
            try:
                if int(task_id) < len(self.tasklist):
                    task = self.tasklist[int(task_id)]
                    uppg = TaskList(int(task_id))
                    task[2] = bool(uppg.mark_done(int(task_id)))
                    break
                else:
                    print("Finns ej i listan.")
            except ValueError:
                print("Du måste skriva en siffra.")

    def main(self):
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

    def __init__(self, task_counter=0):
        """Ta in en siffra som kan användas som ID-nummer."""
        self.task_counter = task_counter

    def create_task(self, description):
        """Skapa en uppgift och ge den ett ID-nummer."""
        task_id = self.task_counter
        task = Task(task_id)
        task.description = description
        return [task.description, task.task_id, task.done]

    def mark_done(self, task_id):
        """Markera uppgiften som färdig."""
        task = Task(task_id)
        return task.mark_done           # bool()


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
        return self.done


if __name__ == "__main__":
    app = TodoApp()
    app.main()
