from os import system, name
from keyboard import wait
def cls():
	"""
	Clears the console.

	"""
	system("cls" if name == "nt" else "clear")

def pause(hotkey = "enter", text = None):
	"""
	Pauses the program until the specified key is pressed.

	"""
	if text is None:
		text = f'Press "{hotkey}" to continue...'
	print(text)
	wait(hotkey)