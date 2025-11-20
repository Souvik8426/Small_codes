import pyautogui as pg
import time
import random

def get_messages():
    """Gets a list of messages from the user."""
    messages = []
    while True:
        message = input("Enter a message to spam (or press Enter to finish): ")
        if not message:
            break
        messages.append(message)
    return messages

def get_names():
    """Gets a list of names to tag from the user."""
    names = []
    while True:
        name = input("Enter a name to tag (or press Enter to finish): ")
        if not name:
            break
        names.append(name)
    return names

def countdown(seconds):
    """Prints a countdown from the given number of seconds."""
    for i in range(seconds, 0, -1):
        print(f"Spamming in {i}...")
        time.sleep(1)
    print("Spamming now!")

def main():
    """The main function."""
    print("--- Welcome to the Message Spammer ---")
    print("This script will spam messages in any application.")
    print("Please make sure you have the target application in focus.")
    print()

    messages = get_messages()
    if not messages:
        print("No messages to spam. Exiting.")
        return

    tag_enabled = input("Do you want to tag users? (y/n): ").lower() == 'y'
    names = []
    if tag_enabled:
        names = get_names()

    try:
        num_messages = int(input("Enter the number of messages to send: "))
        delay = float(input("Enter the delay between messages (in seconds): "))
        start_delay = int(input("Enter the initial delay before spamming starts (in seconds): "))
    except ValueError:
        print("Invalid input. Please enter numbers only. Exiting.")
        return

    countdown(start_delay)

    for i in range(num_messages):
        message = random.choice(messages)
        if tag_enabled and names:
            name = random.choice(names)
            pg.write(f"@{name} ")

        pg.write(message)
        pg.press("enter")
        time.sleep(delay)

    print("--- Spamming finished ---")

if __name__ == "__main__":
    main()
