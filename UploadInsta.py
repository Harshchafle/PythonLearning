# pip install instabot

from instabot import Bot

bot = Bot()

bot.login(username='kp15.04', password='SHIVAJI15')

bot.login()

# Get a list of users following the bot

followers = bot.get_user_followers('your_username')

# Get a list of users the bot is following

following = bot.get_user_following('your_username' )

# Get a list of users who are not following the bot

not_following = [user for user in followers if user not in following]

print(followers)
print(following)
print(not_following)

# to upload image files

bot.upload_photo('path_to_your_image.jpg', caption='Caption for your image')