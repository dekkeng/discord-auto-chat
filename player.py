from time import sleep
from random import uniform,choice


class Player:
    def __init__(self, user):
        self.user = user

    def bcc_first_task(self):
        try:
            self.user.send_message('!daily')
        except Exception:
            pass
        
    def bcc_task(self):
        try:
            self.user.send_message('!work')
        except Exception:
            pass

    def infamous_task(self):
        try:
            self.user.goto("https://discord.com/channels/1028434699644833842/1031039506264105021")
            sleep(15)
            self.user.select_text("ACTIVATE")
            sleep(2)
            self.user.select_dropdown("Select your target")
            sleep(5)
            self.user.select_dropdown_random_option()
            sleep(2)
            self.user.select_text(choice(("Use Geo Location", "Deploy Radar", "Activate Drones")))
            sleep(0.01)
        except Exception:
            pass
        
    def ape_task(self):
        try:
            self.user.select_text("😰")
            sleep(0.01)
        except Exception:
            pass
    def ape_fish(self):
        try:
            self.user.select_text("Fish!")
            sleep(uniform(11,12))
            self.user.select_text("PULL")
        except Exception:
            pass

    def eoe_task(self):
        try:
            self.user.select_text("RECHARGE SHIELDS")
            sleep(uniform(2,3))
            self.user.select_text("ACTIVATE SHIELDS")
            sleep(uniform(2,3))
        except Exception:
            pass

    def kumo_work(self):
        self.user.goto("https://discord.com/channels/878620883076399134/948710889882783764")
        sleep(uniform(20,30))

        try:
            self.user.send_message('!work')
            sleep(uniform(2,5))
            self.user.send_message('!collect')
            sleep(uniform(2,5))
            self.user.send_message('!dep all')
            sleep(uniform(2,5))
        except Exception:
            pass

    def wonderpal_work(self):
        self.user.goto("https://discord.com/channels/918526092875300944/958151810646958131")
        sleep(uniform(20,30))

        self.user.send_message('$work')
        sleep(uniform(15,20))
        self.user.send_message('$collect')
        sleep(uniform(0,5))
            
    def tokyoclone_work(self):
        self.user.goto("https://discord.com/channels/940399190004105267/940399193510518808")
        sleep(uniform(20,30))

        self.user.send_message('.daily')
        sleep(uniform(10,15))
        self.user.send_message('.pick')
        sleep(uniform(0,5))
            
    def thj_work(self):
        self.user.goto("https://discord.com/channels/1135545260538339420/1225447775286726676")
        sleep(uniform(20,30))

        msgs = ['ok','gogogo', 'bera','bear', 'yes', 'nice', 'lets go', 'now', 'LFG']

        for _ in range(200):
            self.user.send_message(choice(msgs))
            sleep(uniform(10,20))
        sleep(uniform(10,15))
