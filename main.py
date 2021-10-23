import requests
import threading

link = input("https://camo.githubusercontent.com/")
counter = 0

def start():
	global counter
	requests.get(f"https://camo.githubusercontent.com/{link}")
	counter += 1
	print(f'Boosted - {counter}')

for i in range(1000):
	start()
