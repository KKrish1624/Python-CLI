import sys
import os.path
from datetime import date

# Function that prints the specified todo menu: 
def help_text():
    help_text = '''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''

    sys.stdout.buffer.write(help_text.encode('utf8'))

# Function that adds a todo's to the todo.txt file: 
def add_task(args):

    with open("todo.txt", "a") as file:
        file.write(args + "\n")
    
    print('''Added todo: "{}"'''.format(args))
        
# Function that lists the todo's in the file: 
def list_pending_todos(filename = "todo.txt"):
    for i,line in reversed(list(enumerate(open(filename)))):
        sys.stdout.buffer.write("[{}] {}\n".format(i+1,line.rstrip()).encode('utf8'))
        
# Function that deletes the specified todo number from the file: 
def del_task(num):
    num = int(num)
    with open("todo.txt", "r") as file:
        lines = file.readlines()
        count = len(lines)
    if (num-1)>= 0 and count > num-1:
        del lines[num-1]
        with open("todo.txt", "w") as new_file:
            for new_lines in lines:
                new_file.write(new_lines)
        print("Deleted todo #{}".format(num))
    else:
        print("Error: todo #{} does not exist. Nothing deleted.".format(num))


# Function that marks a todo as done and adds it to the done.txt file according to the given format: 
def done_todo(num):
     num = int(num)
     with open("todo.txt", "r") as file:
        lines = file.readlines()
        count = len(lines)
        if (num-1) >= 0 and count > (num-1):
            task_done = lines[num-1]
            with open("done.txt", "a") as done:
                today = date.today()
                done_task = "x " + str(today) + " " + task_done 
                done.write(done_task)
            del lines[num-1]
            with open("todo.txt", "w") as new_file:
                for new_lines in lines:
                    new_file.write(new_lines)
            print("Marked todo #{} as done.".format(num))

        else:
            print("Error: todo #{} does not exist.".format(num))

# Function that returns the pending and completed todos: 
def report():
    today = date.today()
    if os.path.isfile('todo.txt') and os.path.isfile('done.txt'):
        with open("todo.txt", "r") as file:
            lines = file.readlines()
            count_todo = len(lines)
        with open("done.txt", "r") as file:
            lines = file.readlines()
            count_done = len(lines)   
        print(today, "Pending :", count_todo, "Completed :", count_done)

    else:
        print(today, "Pending :", 0, "Completed :", 0)


# Main class that uses all the function and calls them when the respective keywords are input by the used in CL.
class CommandLine:
    def __init__(self):
        list_argv = sys.argv
        list_argv.pop(0)

        if "help" in list_argv:
            help_text()

        if len(list_argv) == 0:
            help_text()

        if "add" in list_argv:
            if len(list_argv) < 2 :
                print("Error: Missing todo string. Nothing added!")

            else: 
                add_task(list_argv[1])


        if "ls" in list_argv:
            if os.path.isfile('todo.txt'):
                with open("todo.txt", "r") as file:
                    lines = file.readlines()
                    count_todo = len(lines)

                if count_todo != 0:
                    list_pending_todos()
                else:
                    print("There are no pending todos!")

            else:
                print("There are no pending todos!")

        if "del" in list_argv:
            list_argv.pop(0)
            if os.path.isfile('todo.txt'):
                if len(list_argv) == 0: 
                    print("Error: Missing NUMBER for deleting todo.")
                else:
                    del_task(list_argv[0])
            else:
                print("Error: Missing NUMBER for deleting todo.")


        if "done" in list_argv:
            if os.path.isfile('todo.txt'):
                if len(list_argv) < 2 :
                    print("Error: Missing NUMBER for marking todo as done.")

                else: 
                    done_todo(list_argv[1])
            else:
                print("Error: Missing NUMBER for marking todo as done.") 
                

        if "report" in list_argv:
            report()


# Runs the application: 
if __name__ == '__main__':
    app = CommandLine()


    