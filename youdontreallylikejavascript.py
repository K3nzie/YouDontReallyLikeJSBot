import praw
import pdb
import re
import os
import sys

from reply_to_posts import replyToPost
from reply_to_comments import replyToComment

botName = "YDRL JS 1.0 - You don't really like javascript"
reddit = praw.Reddit('youdontreallylikejs')
answer = "NO! You dont!"
query = "I love javascript|I like javascript|I like JS|I love JS"
subreddit = reddit.subreddit("ProgrammerHumor")

def showMenu(botName):
    choice = 0
    print("Benvenuto su ", botName, "!")
    print("Con questo bot puoi facilmente odiare chi utilizza Javascript")
    print("------------")
    print("-----------------------")
    while True:
        print("Fai la tua scelta :")
        print("1. Controlla i post")
        print("2. Controlla i commenti")
        print("3. Controlla tutti commenti (STREAM)")
        print("4. Controlla tutti i post (STREAM)")
        print("5. Esci")
        choice = int(input("Fai la tua scelta (1,2,3) : "))
        if(choice >= 1 and choice <= 5):
              return choice
              break
        else:
            choice = 0
            print("Devi scegliere tra uno dei numeri nel menù, riprova...")
            choice = int(input("Fai la tua scelta (1,2,3) : "))

def assertChoice(choice, subreddit, answer, query):
    if(choice == 1):
              replyToPost(subreddit, answer, query)
    if(choice == 2):
              replyToComment(subreddit, answer, query)
    if(choice == 5):
              print("Grazie per aver utilizzato YDRL JS Bot v0.1")
              print("Sono sicuro che hai passato un'altra inutile giornata!")
              print("Alla prossima...")
              sys.exit(0)


menuChoice = showMenu(botName)
assertChoice(menuChoice, subreddit, answer, query)
