queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

def show_queue(queue):
    """Print everyone currently in the queue"""
    print("[the queue goes here]")

# Function stubs go here 

def run_app(queue): 
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 4)

    is_running = True

    while is_running:
        show_queue(queue)
        print()
        print("Options: add / remove / quit") 
        command = input("> ")

        if command == "quit": 
            is_running =False 
            print("Goodnight!")
            # your commands go here

run_app(queue) 