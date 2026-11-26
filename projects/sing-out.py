queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]


def show_queue(queue):
    print()
    print("Current queue:")
    print()
    for singer in queue:
        name, song = singer
        print(f"{name} - {song}")
    print()


def add_singer(queue):
    name = input("Singer name: ")
    song = input("Song: ")
    queue.append((name, song))


def remove_singer(queue):
    name = input("Singer name to remove: ")

    for singer in queue:
        if singer[0].lower() == name.lower():
            queue.remove(singer)
            return

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)
        print("Options: add / remove / quit")
        command = input("> ")

        if command == "add":
            add_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        elif command == "quit":
            is_running = False
            print("Goodnight!")
        else:
            print("Unknown option.")


run_app(queue) 