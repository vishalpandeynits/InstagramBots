import argparse
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p)

# (The following functions apply if you have a private account)

# Approve users that requested to follow you
bot.approve_pending_follow_requests()

# Reject users that requested to follow you
bot.reject_pending_follow_requests()
