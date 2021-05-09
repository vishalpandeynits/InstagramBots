import time
from getpass import getpass 

try:
    from instabot import Bot
except ImportError:
    raise "Instabot module is not installed, try again after installing instabot module."

bot = Bot(message_delay=10)
username  = input("Please enter your username: ")
password = getpass()
bot.login(username = username,password = password)
history = bot.get_user_followers(username)
while 1:
    if history == bot.get_user_followers(username):
        print("No change in followers list")
    else:
        my_followers = bot.get_user_followers(username)
        new_followers = set(my_followers).difference(set(history))
        print(new_followers)
        if len(new_followers)>0 and bot.send_message("Hi",new_followers):
            print(f"Message sent to {new_followers}")
            history = my_followers
    time.sleep(10*60)
