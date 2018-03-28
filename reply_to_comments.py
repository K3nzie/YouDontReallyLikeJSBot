import re
import os
import sys

def replyToComment(subreddit, answerToComment, query):
    if not os.path.isfile("comments_replied_to.txt"):
        print("Nessun file comments_replied_to.txt, verrà creato al primo controllo!")
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            print("File comments_replied_to.txt trovato! Si utilizzerà quello per popolare i commenti con già una risposta dal bot.")
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    print("Adesso controlliamo se qualcuno ha pubblicato qualche commento che parla bene di Javascript...")
    print("Subreddit : ", subreddit.title)
    
    checked = 0
    replied = 0
    for submission in subreddit.hot(limit=25):
        print("Titolo Post :", submission.title)
        print("Autore Post :", submission.author)
        print("Upvotes : ", submission.score)
        print("Comments : ", submission.num_comments)
        print("E adesso vediamo i commenti per il post con ID ", submission.id)
        print("---- Commenti...");
        submission.comments.replace_more(limit=25)
        for comment in submission.comments.list():
            print("Testo commento :", comment.body.encode("utf8", errors="ignore"))
            print("ID commento :", comment.id)
            if comment.id not in comments_replied_to:
                if re.search(query, comment.body, re.IGNORECASE):
                    checked+=1
                    replied+=1
                    print("Questo commento APPREZZA javascript!!")
                    print("Dobbiamo fare qualcosa! L'autore deve essere una persona molto stupida!")
                    print("Fortuna che il nostro bot viene in aiuto!")
                    print("Rispondo al commento con ID : ", comment.id, ", risposta del bot :", answerToComment)
                    print("...")
                    comment.reply(answerToComment)
                    print("...")
                    print("Commento aggiunto!")
                    print("Aggiungo il commento all'elenco dei commenti a cui il bot ha già risposto...")
                    comments_replied_to.append(comment.id)
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                    print("Aggiunto id :", comment.id, "a comments_replied_to.txt")
                    print("__________________________________________________")
                else:
                    checked+=1
                    print("Il commento non presenta apprezzamenti verso Javascript, bravo!!")
                    print("___________________________________________")
            else:
                checked+=1
                print("Il commento ha già avuto una risposta dal bot! Salto...")
                print("__________________________________________")

    print("Finito!")
    print("Commenti controllati : ", checked)
    print("Commenti a cui si ha dato risposta :", commented)
    input("Inserisci qualunque cosa per continuare...")
    sys.exit(0)
                
                
                
            
            
