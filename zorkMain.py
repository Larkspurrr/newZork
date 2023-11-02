from zorkMisc import items as it
from zorkMisc import monsters as mon
from zorkMSG import *
import traceback

# Number of rooms: 10/15
# Number of proper items: 3
# Number of NPCs/Mobs: 2/5
	# Troll, Grue

directions = {
	"northCMD": ["go north", "north", "n"],
	"eastCMD": ["go east", "east", "e"],
	"southCMD": ["go south", "south", "s"],
	"westCMD": ["go west", "west", "w"],
	"downCMD": ["go down", "down", "d"],
	"upCMD": ["go up", "up", "u"],
}

grabCMD = ["grab", "take"]
actionCMD = ["read", "examine", "activate"]


class Player:
	def __init__(self):
		self.inventory = []
		self.position = ""
		self.wounds = 0
		self.heals = 0

	def openINV(self):
		if len(self.inventory) == 0:
			print("You have nothing.\n")
		else:
			print("Your inventory: ")
			for i in self.inventory:
				print("A", i.__class__.__name__)

	def diagnostics(self):
		if self.wounds == 0:
			print("You are in perfect health.")
			print("You can be killed by a serious wound.\n")
		elif self.wounds == 1:
			print(f"You have a light wound, which can be cured after {self.heals} moves.")
			print("You can be killed by one more light wound.\n")

	def grab(self, cmd, obj):
		if hasattr(self.position, "opened"):
			if (obj in self.position.items) and (self.position.opened) and (cmd in grabCMD):
				print("Taken.\n")
				obj.grabbed = True
				self.inventory.append(obj)
				self.position.items.remove(obj)
			elif (obj in self.position.dItems):
				print("Taken.\n")
				obj.grabbed = True
				self.inventory.append(obj)
				self.position.dItems.remove(obj)
			else:
				print(f"You can't see any {obj.__class__.__name__} here!\n")
		else:
			if (obj in self.position.items) and (cmd in grabCMD):
				print("Taken.\n")
				obj.grabbed = True
				self.inventory.append(obj)
				self.position.items.remove(obj)
			elif (obj in self.position.dItems):
				print("Taken.\n")
				obj.grabbed = True
				self.inventory.append(obj)
				self.position.dItems.remove(obj)
			else:
				print(f"You can't see any {obj.__class__.__name__} here!\n")

	def drop(self, cmd, obj):
		if (obj in self.inventory):
			self.position.dItems.append(obj)
			obj.grabbed = False
			self.inventory.remove(obj)
			print("Dropped.\n")
		elif (len(self.inventory) > 0) and (obj not in self.inventory):
			print(f"You don't have a/an {obj.__class__.__name__}.\n")
		elif len(self.inventory) == 0:
			print("You have nothing to drop.\n")

	def action(self, obj):
		if len(self.inventory) > 0:
			self.inventory.obj.action()

	def death(self):
		self.position = nHouse
		self.wounds = 0
		self.heals = 0
		print(deathMSG)
		self.position.enter()

	def attack(self, monster, weapon, player):
		if monster in mon:
			mon[monster].hurt(player, weapon)

	def pos(self): print(self.position)


class WHouse:
	def __init__(self):
		self.items = [it["leaflet"]]
		self.dItems = []
		self.entered = False
		self.opened = False
	
	def enter(self):
		print("West of House")
		if self.entered == False:
			print("""You are standing in an open field west of a white house, with a boarded front door.
There is a small mailbox here.\n""")
		else:
			print("There is a small mailbox here.\n") 
		self.entered = True

	def open(self, obj):
		if (self.opened == False) and (obj == "mailbox"):
			self.opened = True
			print("Opening the small mailbox reveals a leaflet.\n")
		elif self.opened == True:
			print("It is already opened.\n")

	def n(self): return nHouse

	def e(self): print("The door is boarded and you can't remove the boards.\n")

	def s(self): return sHouse

	def w(self): print("PLACEHOLDER: FOREST\n")
wHouse = WHouse()

class NHouse:
	def __init__(self):
		self.dItems = []
		self.entered = False

	def enter(self):
		print("North of House")
		if self.entered == False:
			print(nHouseMSG)
		self.entered = True
		print("\n")

	def n(self): return forestPath

	def e(self): return behindHouse

	def s(self): print("The windows are all boarded.\n")

	def w(self): return wHouse
nHouse = NHouse()

class ForestPath:
	def __init__(self):
		self.entered = False
		self.dItems = []

	def enter(self):
		print("Forest Path")
		if self.entered == False:
			print(forestPathMSG)
		print("\n")

	def n(self): print("PLACEHOLDER: CLEARING\n")

	def e(self): print("PLACEHOLDER: FOREST 1\n")

	def s(self): return nHouse

	def w(self): print("PLACEHOLDER: FOREST 2\n")

	def u(self): return upATree
forestPath = ForestPath()

class UpATree:
	def __init__(self):
		self.entered = False
		self.items = [it["egg"]]
		self.dItems = []

	def enter(self):
		print("Up a Tree")
		if self.entered == False:
			print(treeMSG)
		print("\n")

	def u(self): return forestPath
upATree = UpATree()

class SHouse:
	def __init__(self):
		self.dItems = []
		self.entered = False

	def enter(self):
		print("South of House")
		if self.entered == False:
			print("You are facing the south side of a white house. There is no door here, and all the windows are boarded.")
		self.entered = True
		print("\n")

	def n(self): print("The windows are all boarded.\n")

	def e(self): return behindHouse

	def s(self): print("PLACEHOLDER: FOREST\n")

	def w(self): return wHouse
sHouse = SHouse()

class BehindHouse:
	def __init__(self):
		self.dItems = []
		self.entered = False
		self.openWindow = False

	def enter(self):
		print("Behind House")
		if self.entered == False:
			print("You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar.")
			self.entered = True
		print("\n")

	def open(self, obj):
		self.openWindow = True
		print("With great effort, you open the window far enough to allow entry.\n")

	def n(self): return nHouse

	def e(self): print("PLACEHOLDER: CLEARING\n")

	def w(self):
		if self.openWindow == False:
			print("The kitchen window is closed.\n")
		else:
			return kitchen

	def s(self): return sHouse
behindHouse = BehindHouse()

class Kitchen:
	def __init__(self):
		self.items = ["bottle", "bag"]
		self.dItems = []
		self.entered = False

	def enter(self):
		print("Kitchen")
		if self.entered == False:
			self.entered = True
			print(kitchenMSG)
		if "bag of chilis" in self.items:
			print("On the table is an elongated brown sack, smelling of hot peppers.")
		if "bottle" in self.items:
			print("""A bottle is sitting on the table.
The glass of bottle contains:
	A quantity of water""")
		print("\n")

	def grab(self, cmd, obj):
		if (obj in self.items) and (cmd in grabCMD):
			if obj == "bag":
				print("Taken.\n")
				
				player.inventory.append("bag of chilis")
				self.items.remove(obj)
			else:
				print("Taken.\n")
				
				player.inventory.append(obj)
				self.items.remove(obj)
		else:
			print(f"You can't see any {obj} here!\n")

	def n(self): print("You can't go that way.\n")

	def e(self): return behindHouse

	def s(self): print("You can't go that way.\n")

	def w(self): return livingRoom
kitchen = Kitchen()

class LivingRoom:
	def __init__(self):
		self.items = [it["sword"], it["lantern"]]
		self.dItems = []
		self.moved = False
		self.entered = False
		self.dOpened = False
		self.tOpened = False

	def enter(self):
		print("Living Room")
		if self.entered == False:
			self.entered = True
			print(livingRoomMSG)

		if it["sword"] in self.items: print("Above the trophy case hangs an elvish sword of great antiquity.")
		if it["lantern"] in self.items: print("A battery-powered brass lantern is on the trophy case.")

		print("\n")

	def grab(self, cmd, obj):
		if (obj in self.items) and (cmd in grabCMD):
			print("Taken.\n")
			obj.grabbed = True
			
			player.inventory.append(obj)
			self.items.remove(obj)
		else:
			print(f"You can't see any {obj} here!\n")

	def move(self, obj):
		if obj == "rug":
			print("""With great effort, the rug is moved to one side of the room, revealing the
dusty cover of a closed trap door.\n""")
			self.moved = True

	def open(self, obj):
		if obj == "trapdoor":
			self.tOpened = True
			print("The door reluctantly opens to reveal a rickety staircase descending into darkness.\n")

	def n(self): print("You can't go that way.\n")

	def e(self): return kitchen

	def s(self): print("You can't go that way.\n")

	def w(self):
		if self.dOpened == False:
			print("The door is nailed shut.\n")
		else:
			print("PLACEHOLDER \n")

	def d(self):
		if self.moved == False:
			print("You can't go that way.\n")
		elif (self.tOpened == False) and (self.moved):
			print("The trapdoor is closed.\n")
		elif self.tOpened:
			return cellar
livingRoom = LivingRoom()

class Cellar:
	def __init__(self):
		self.entered = False
		self.dItems = []

	def enter(self):
		if player.position == livingRoom:
			livingRoom.tOpened = False
			print("The trap door crashes shut, and you hear someone barring it.\n")

			player.position = cellar

		if ((it["lantern"] in player.inventory) and (it["lantern"].on == False)) or (it["lantern"] not in player.inventory):
			print("You have moved into a dark place.")
			print("It is pitch black and you're likely to be eaten by a grue.")
		else:
			print("Cellar")
			if self.entered == False:
				print(cellarMSG)
				if (it["sword"] in player.inventory) and (mon["troll"].alive == True):
					print("Your sword is glowing with a faint blue glow.")
			print("\n")

	def n(self):
		if ((it["lantern"] in player.inventory) and (it["lantern"].on == False)) or (it["lantern"] not in player.inventory):
			print("""Oh no! A lurking grue slithered into the room and devoured you!\n""")
			player.death()
		else: 
			return trollRoom

	def e(self): print("You can't go that way.\n")

	def s(self): print("PLACEHOLDER: EAST OF CHASM\n")

	def w(self): print("You try to ascend the ramp, but it is impossible, and you slide back down.\n")

	def u(self): print("The trapdoor is closed. \n")
cellar = Cellar()

class TrollRoom:
	def __init__(self):
		self.entered = False
		self.dItems = []

	def enter(self):
		print("Troll Room")
		if self.entered == False:
			print(trollRoomMSG)
		if mon["troll"].alive:
			print("A nasty looking troll, brandishing a bloody axe, blocks all passages out of the room.")
			if it["sword"] in player.inventory:
				print("Your sword has begun to glow very brightly.\n")

	def n(self): print("You can't go that way.\n")

	def e(self):
		if mon["troll"].alive:
			print("The troll fends you off with a menacing gesture.")
			mon["troll"].attack(player)
		else:
			print("PLACEHOLDER: EAST-WEST PASSAGE")

	def s(self): return cellar

	def w(self):
		if mon["troll"].alive:
			print("The troll fends you off with a menacing gesture.")
			mon["troll"].attack(player)
		else:
			print("PLACEHOLDER: MAZE")
trollRoom = TrollRoom()

wHouse.enter()

player = Player()
player.position = wHouse

def heal():
	if player.wounds == 1:
		if player.heals > 0:
			player.heals -= 1
		else:
			player.wounds -= 1
	elif player.wounds == 2:
		player.death()

while True:
	try:
		x = input(">")
		
		if x == "quit": break
		elif x == "inventory": player.openINV()
		elif x == "diagnostics": player.diagnostics()

		# For debugging purposes
		elif x == "pos": player.pos()
		elif x == "troll attack":
			mon["troll"].attack(player)

		x_parts = x.split()
		if (len(x_parts) == 4) and (x_parts[0].strip() == "attack"):
			player.attack(x_parts[1].strip(), x_parts[3].strip(), player)

		if (len(x_parts) == 2) and (x_parts[1].strip() != "troll"):
			cmd, obj = x_parts[0].strip(), x_parts[1].strip()
			cmd = cmd.lower()
			obj = obj.lower()
			if cmd in grabCMD:
				obj = it[obj]
				player.grab(cmd, obj)
			elif cmd == "drop":
				obj = it[obj]
				player.drop(cmd, obj)
			elif cmd == "open":
				player.position.open(obj)
			elif cmd == "move":
				player.position.move(obj)
			elif cmd in actionCMD:
				obj = it[obj]
				obj.action()

		for key in directions:
			if x in directions[key]:
				direction = directions[key][2]
				new_pos = getattr(player.position, direction)()
				new_pos.enter()
				player.position = new_pos
				heal()
				
		if it["axe"] or it["egg"] in player.inventory:
			# mon["thief"].spawn()
			pass

		if len(player.position.dItems) > 0:
			for i in player.position.dItems:
				print(f"There is a/an {i.__class__.__name__} on the ground")
			print("\n")

	except Exception as e:
		tb = traceback.extract_tb(e.__traceback__)
		print(f"An error occured on line {tb[-1].lineno}: {e}")
