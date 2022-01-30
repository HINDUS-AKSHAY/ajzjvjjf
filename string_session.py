from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("")
print("""Welcome To DeadlyBot String Session\nGenerator By @SAMEER_795\n\n""")
print("""LET'S GET START\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @Deadly_userbot For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing DeadlyBot Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +918983734834! Kindly Retry"
        )
        print("")
        continue
    break
