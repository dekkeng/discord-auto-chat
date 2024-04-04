from player import Player
from user import User
from time import sleep
from random import uniform

user = User("https://discord.com/channels/1019967843531497544/1137135988548841513")
player = Player(user)
sleep(30)
#player.bcc_first_task()

while True:
    player.thj_work()
    #sleep(uniform(3600,3700))
