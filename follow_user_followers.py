import argparse
try:
    from instabot import Bot
except ImportError:
    raise "Instabot module is not installed, try again after installing instabot module."

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("users", type=str, nargs="+", help="users")
args = parser.parse_args()

bot = Bot(
    filter_users=True,
    filter_private_users=False,
    filter_previously_followed=True,
    filter_business_accounts=True,
    filter_verified_accounts=True,
)
bot.login(username=args.u, password=args.p)

for username in args.users:
    bot.follow_followers(username)
