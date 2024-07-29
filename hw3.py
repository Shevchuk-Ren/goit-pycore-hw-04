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
         
        
      
