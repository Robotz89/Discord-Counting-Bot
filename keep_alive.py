from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I am now up and running as a Counting Bot!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

#this is optional, but if you want to, you can use this web server code to keep the bot always on
#all you have to do is copy the link up at the top when you run it, and copy it
#then go to this website: https://uptimerobot.com/
#create an account and add a monitor
#select HTTPS, and put in the link where it says: https://
#put a name in the section that is labeled: Friendly Name
#click Create Monitor, then hit it one more time
#you are done, and the bot will now be always running
