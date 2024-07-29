from pathlib import Path
import sys
import colorama

# TASK 3

if __name__ == "__main__":

    directory_path = sys.argv

    

    def show_directory_structure(directory):

      try:     

        print(f"{colorama.Fore.BLUE}{directory}/")

        for path in directory.iterdir():
           
           if path.is_dir():
             show_directory_structure(path)
             

           if path.is_file():
             print(f"{colorama.Fore.GREEN}  {path}")

      except PermissionError:
        print(colorama.Fore.RED + f"Error: Permission denied for directory '{path}'.")
        return
      
    try:
       if len(directory_path) > 1:
          directory = Path(directory_path[-1])

          if directory.exists():
           show_directory_structure(directory)
          else:
            raise NotADirectoryError
        
    except NotADirectoryError:
        print(colorama.Fore.RED + f"Error: Path '{directory}' is not a directory of not found.")
         
        
      
      
  

# def log_info(message):
#     print(f"{colorama.Fore.BLUE} [INFO] {Fore.RESET} {message}")

# def log_warning(message):
#     print(f"{Fore.YELLOW} [WARNING] {Fore.RESET} {message}")

# def log_error(message):
#     print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}")

# try:
#         entries = sorted(Path(path).iterdir(), key=lambda e: (not e.is_dir(), e.name))
#     except FileNotFoundError:
#         print(colorama.Fore.RED + f"Error: Directory '{path}' not found.")
#         return
#     except NotADirectoryError:
#         print(colorama.Fore.RED + f"Error: Path '{path}' is not a directory.")
#         return
#     except PermissionError:
#         print(colorama.Fore.RED + f"Error: Permission denied for directory '{path}'.")
#         return