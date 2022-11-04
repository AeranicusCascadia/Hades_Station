actions = ["look", "rest", "explore", "x"]
statusActions = ["health", "score","name"]

playerHealth = 10
playerScore = 0
playerName = "Player"

def getPlayerName():
	return playerName
	
def getPlayerHealth():
	return playerHealth	
		
def getPlayerScore():
	return playerScore

class Game:
	def __init__(self, name, running):
		self.name = name
		self.turn = 1
		
	def getName(self):
		return self.name
		
	def getTurn(self):
		return self.turn	
		
	def incrementTurn(self):	
		self.turn += 1
		
	def getCommand(self):
		playerCommand = input("Enter your command: ")
		playerCommand = playerCommand.lower()
		
		if playerCommand in actions:
			print(f" You chose: { playerCommand } ")
			self.incrementTurn()
		elif playerCommand in statusActions:
			
			#print(f" You chose: { playerCommand } ")
			if playerCommand == "score":
				print( getPlayerScore() )
			elif playerCommand == "health":
				print( getPlayerHealth() )
			elif playerCommand == "name":
				print( getPlayerName() )
		else:
			print("I don't know that command.")	
		
	
		
game = Game("Hades Station", True)
		

print("\n")

while game.getTurn() < 11:
	print(f"Turn: { game.getTurn() } ")
	game.getCommand()

print("\n")
print("That's your 10 turns!")
