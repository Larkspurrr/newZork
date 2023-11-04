from numpy import arange
from numpy.random import choice
from random import randint
from random import choice as randchoice
import traceback

# <-- Items START -->
class Leaflet:
	def __init__(self):
		self.grabbed = False

	def action(self):
		if self.grabbed:
			print("""\"WELCOME TO ZORK!

ZORK is a game of adventure, danger, and low cunning. In it you will explore
some of the most amazing territory ever seen by mortals. No computer should be
without one!\"\n""")


class Lantern:
	def __init__(self):
		self.grabbed = False
		self.on = False

	def action(self):
		if self.grabbed:
			self.on = not self.on
			if self.on:
				print("The brass lantern is now on.\n")
			else:
				print("The brass lantern is now off.\n")


class Sword:
	def __init__(self):
		self.grabbed = False
		self.weapon = True

	def action(self):
		if self.grabbed: print("Whoosh!")


class Axe:
	def __init__(self):
		self.grabbed = False
		self.weapon = True

	def action(self): 
		if self.grabbed: print("Whoosh!")


class JewelEncrustedEgg:
	def __init__(self):
		self.grabbed = False


leaflet = Leaflet()
lantern = Lantern()
sword = Sword()
axe = Axe()
jewelEgg = JewelEncrustedEgg()
# <-- Items END -->



# <-- Monsters START -->
class Troll:
	def __init__(self):
		self.alive = True
		self.wounds = 0

	def attack(self, player):
		atk_num = choice(arange(0, 3), p=[.4, .4, .2])
		if atk_num == 0:
			print("The troll's axe barely misses your ear.\n")
		elif atk_num == 1:
			print("The axe gets you right in the side. Ouch!\n")
			player.heals = 30
			player.wounds += 1
		elif atk_num == 2:
			print("The axe digs into your body, killing you instantly.\n")
			player.death()

	def hurt(self, player, weapon):
		try:
			if self.wounds == 2:
				atk_num = 3
			else:
				atk_num = choice(arange(0, 4), p=[.4, .4, .1, .1])

			if atk_num == 0:
				print("A quick stroke, but the troll is on guard.")
				self.attack(player)
			elif atk_num == 1:
				print("""The troll is confused and can't fight back.
The troll slowly regains his feet.""")
				self.wounds = 1
			elif atk_num == 2:
				print("The troll is battered into unconsciousness.\n")
				self.wounds = 2
			elif atk_num == 3:
				if self.wounds != 2:
					msg = [f"It's curtains for the troll as your {weapon.__class__.__name__} removes his head.",
					"The fatal blow strikes the troll square in the heart: He dies."]
					print(randchoice(msg))
				else:
					print("The unarmed troll cannot defend himself: He dies.")
				print("""Almost as soon as the troll breathes his last breath, a cloud of sinister
black fog envelops him, and when the fog lifts, the carcass has disappeared.""")
				if weapon == sword:
					print("Your sword is no longer glowing.\n")
				self.alive = False
		except Exception as e:
			tb = traceback.extract_tb(e.__traceback__)
			print(f"An error occurred on line {tb[-1].lineno}: {e}")


troll = Troll()


class Thief:
	def __init__(self):
		self.alive = True

	def spawn(self):
		spawn_num = randint(1, 20)
		if spawn_num in [1, 2]:
			print("")


troll = Troll()
thief = Thief()
# <-- Monsters END -->


items = {
	"leaflet": leaflet,
	"lantern": lantern,
	"sword": sword,
	"axe": axe,
	"egg": jewelEgg,
}


monsters = {
	"troll": troll,
	"thief": thief,
}
