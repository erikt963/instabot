from instabot import Bot
# import os 
# import glob
# cookie_del = glob.glob("config/*cookie.json")
# os.remove(cookie_del[0])
bot = Bot()
bot.login(username="eriktbo981",
          password="new.bot.848")
 
# Follow
 
message = "hboooooosh"
bot.send_message(message, "heba_astef")
followers = bot.get_user_followers("heba_astef")
print("her followers")
print(len(followers))