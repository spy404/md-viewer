import os
from rich.console import Console
from rich.markdown import Markdown
from pystyle import Center
from colorama import Fore

file = input("File location: \n>>> ")

os.system("cls" if os.name == "nt" else "clear")
if os.name == "nt": os.system("title Markdown viewer - spy404#6985")

console = Console()

f = open(file, "r")
lines = f.readlines()
output = ""

for i in lines:
	output = output + lines + "\n"

console.print(Markdown(output))
print(Center.XCenter(Fore.RED + "\n\nDeveloped with love by spy404"))
