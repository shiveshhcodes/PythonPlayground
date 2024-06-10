# CAN BE USE TO CREATE A INSTAGRAM BOT and get insights...

from instabot import Bot
bot=Bot()
bot.login(username="shiveshhhhhhh" , password='zakmef-Jizjo7-topmyv')
# bot.follow('https://www.instagram.com/rajat_9629/#')
# bot.upload_photo("")
# bot.unfollow("")
# bot.send_message("HI" , ['warpaintjournal'])

# followers =bot.get_user_followers("shiveshhhhhhh")
# for follower in followers:
#     print(bot.get_user_info(follower))
    
following =bot.get_user_following("shiveshhhhhhh")
for Following in following:
    print(bot.get_user_info(Following))

