from discord_webhook import DiscordWebhook
import time



def main():
    url = input(">Please input the webhook you would like to spam> ")

    msg = input(">Please input the msg you would like to send> ")

    botName = input(">Please input the bot name> ")

    spam = input(">Please input the number of times you want to spam> ")
    spam = int(spam)

    webhook = DiscordWebhook(url=url, content=msg, username = botName)





    for i in range (spam):
        response = webhook.execute()
        time.sleep(1.5)
        print("sent ", i, " times!")

    

    main()

main()



