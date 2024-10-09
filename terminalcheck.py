import psutil

def get_console_name():
    # Get the current process
    current_process = psutil.Process()
    
    # Traverse up the process tree to find the parent processes
    parent_process = current_process.parent()
    
    # Collect the process names
    process_names = []
    
    while parent_process:
        process_names.append(parent_process.name())
        parent_process = parent_process.parent()
    
    return process_names

def check_old_terminal():
      detected_consoles = get_console_name()
      if 'WindowsTerminal.exe' not in detected_consoles or 'conhost.exe' in detected_consoles:
          print(f"WARNING! Your terminal might not support hiragana/katakana/kanjis! If you see nothing between these brackets [ひらがな カタカナ] Consider changing the font on your terminal\n Alternatively, download Windows Terminal: https://apps.microsoft.com/detail/9n0dx20hk701")
          input("Press Enter to continue...")

# Get the names of the parent processes
console_exes = get_console_name()

# Display the relevant process names (terminal/console executables)
print("Console Executables:", console_exes)
check_old_terminal()
