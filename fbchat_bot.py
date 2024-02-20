from fbchat import Client
from fbchat.models import *

# CLASS FOR THE BOT


class MessBot(Client):

    # Read Messages, See Messages from other users
    def onMessage(self,
                  mid=None,
                  author_id=None,
                  message_object=None,
                  thread_id=None,
                  thread_type=ThreadType.USER,
                  **kwargs):
        try:
            msg = str(message_object).split(",")[15][14:-1]
            print(message_object)
            # If user sent video or else user sent text
            if ("//video.xx.fbcdn" in msg):
                msg = msg
            else:
                msg = str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
                print(msg)
            except:
                pass


# Reply to the user/send message


        def sendMsg():
            if (author_id != self.uid):
                self.send(Message(text=reply),
                          thread_id=thread_id,
                          thread_type=thread_type)

    # MESSAGE SENDING

        if (author_id != self.uid):
            if ("hi" in msg):
                reply = "Hello"
                sendMsg()
            elif ("how are you" in msg):
                reply = "Good!"
                sendMsg()
        else:
            pass


# Get Cookies Using GET TOKEN COOKIES (https://chrome.google.com/webstore/detail/get-token-cookie/naciaagbkifhpnoodlkhbejjldaiffcm)
session_cookies = {
    "sb": "QBrUZU2Y_vGtkhvlQODw8ZuN",
    "fr": "0BxUN5wUWSBhI9Ncj.AWU528xQFCgxKVDw877X3di8oMM.Bl1BpA.sD.AAA.0.0.Bl1NGy.AWWo1YK1hHM",
    "c_user": "100047811903486",
    "datr": "QBrUZUHkjP3eT-qmzrjTX56n",
    "xs": "16%3AUoZASSkKHr1mXw%3A2%3A1708445763%3A-1%3A15322"
}

bot = MessBot('jullianvanegas19@gmail.com', 'J55084300',
              session_cookies=session_cookies)
print(bot.isLoggedIn())

try:
    bot.listen()
except:
    bot.listen()
