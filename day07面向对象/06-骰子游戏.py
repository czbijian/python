import random
class Game:
	
	def __init__(self,player1,player2):
		self.player1 = player1
		self.player2 = player2
		print("游戏初始化成功,可以开始了")
	def start_game(self):
		self.player1.cast()
		self.player2.cast()
		print(self.player1)
		print(self.player2)
class Player:
	def __init__(self,name,sex,*dice):
		self.name = name
		self.sex = sex
		self.dices = dice#表示该玩家拥有的骰子列表(元祖)
	#玩家抛骰子
	def cast(self):
		for dice in self.dices:
			dice.move()
	def guess_dice(self):
		return (4,2)
	def __str__(self):
		play_dice_count_list = [self.dices[0].count,self.dices[1].count,self.dices[2].count]
		return "姓名为：%s,投掷的骰子点数信息为：%s"%(self.name,str(play_dice_count_list))

class Dice:
	def __init__(self):
		self.count = 0
	#骰子滚动的方法，滚动之后返回该骰子的点数确定了
	def move(self):
		self.count = random.randint(1,6)

#游戏开始之前准备六颗骰子
d1 = Dice()
d2 = Dice()
d3 = Dice()
d4 = Dice()
d5 = Dice()
d6 = Dice()
#每次游戏需要两个玩家对象
p1 = Player("player1","男",d1,d2,d3)
p2 = Player("player2","女",d4,d5,d6)
#一共要玩5次游戏
for i in range(1,6):
	game = Game(p1, p2)
	game.start_game()
	print("第%d次游戏的情况--------------------"%i)

