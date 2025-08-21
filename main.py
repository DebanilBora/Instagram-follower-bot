


import os
from dotenv import load_dotenv
from insta_follower import InstaFollower

# Load credentials from .env file
load_dotenv()

USERNAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")
TARGET_ACCOUNT = os.getenv("TARGET_ACCOUNT", "chefsteps")

bot = InstaFollower()
bot.login(USERNAME, PASSWORD)
bot.find_followers(TARGET_ACCOUNT)
bot.follow()




