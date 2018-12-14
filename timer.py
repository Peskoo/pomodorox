# -*- coding: utf-8 -*

import time
import sys



class Pomodoro:
	def __init__(self):
		self.timer = 25
		
	def start_timer(self):
		mins = 0
		while mins != self.timer:
			print('........ {} ........'.format(mins))
			time.sleep(60)
			mins += 1
		print('........ {} ........'.format(mins))
		print('Finito !')


	def set_timer(self):
		print('----------------------')
		print('Timer actuel : {} minutes'.format(self.timer))
		timer_choices = int(raw_input('[1] Régler | [2] Revenir > '))
		if timer_choices == 1:
			self.timer = int(raw_input('Combien de temps ? (minutes) > '))
		elif timer_choices == 2:
			pass	


try:
	pomodoro = Pomodoro()
	choices = 0
	while choices != 3:
		print('----------------------')
		print('[1] Démarrer le timer')
		print('[2] Régler le timer')
		print('[3] Quitter')
		choices = int(raw_input("Tapez 1, 2 ou 3 > "))
		if choices == 1:
			pomodoro.start_timer()
		elif choices == 2:
			pomodoro.set_timer()
		elif choices == 3:
			print('A bientot')
			sys.exit()
		else:
			print("Je n'ai rien compris. Au revoir.")
			sys.exit()
except ValueError:
	print("1, 2 ou 3, ce n'est pas très difficile quand même... :)")
