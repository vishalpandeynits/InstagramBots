import argparse
try:
    from instabot import Bot
except ImportError:
    raise "Instabot module is not installed, try again after installing instabot module."

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p)
bot.unfollow_everyone()
