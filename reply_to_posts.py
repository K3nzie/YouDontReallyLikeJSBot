import re
import os
import sys

def replyToPost(subreddit, answerToPost, query):
    if not os.path.isfile("posts_replied_to.txt"):
        print("Nessun file posts_replied_to.txt, verrà creato al primo controllo!")
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as f:
            print("File posts_replied_to.txt trovato! Si utilizzerà quello per popolare i post già visitati.")
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))

    print("Adesso controlliamo se qualcuno ha pubblicato qualche post che parla bene di Javascript...")
    print("Subreddit : ", subreddit.title)

    
    checked = 0
    commented = 0
    for submission in subreddit.hot(limit=25):
        print("Titolo Post : ", submission.title)
        print("Autore Post : ", submission.author)
        print("Upvotes : ", submission.score)
        print("Comments : ", submission.num_comments)
        print("---------------------------------------")
        if submission.id not in posts_replied_to:
            if re.search(query, submission.title, re.IGNORECASE):
                checked+=1
                commented+=1
                print("Questo post APPREZZA javascript!")
                print("Dobbiamo fare qualcosa! ", submission.author, " deve essere una persona molto stupida!")
                print("Fortuna che il nostro bot viene in aiuto!")
                print("Rispondo al post con ID : ", submission.id, ", risposta del bot :", answerToPost)
                print("...")
                submission.reply(answerToPost)
                print("...")
                print("Risposta aggiunta!")
                print("Aggiungo il post all'elenco dei post a cui il bot ha già risposto...")
                posts_replied_to.append(submission.id)
                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")
                print("Aggiunto id :", submission.id, "a posts_replied_to.txt")
                print("___________________________________________")
            else:
                checked+=1
                print("Il post non presenta apprezzamenti verso Javascript, bravo, ", submission.author, "!!")
                print("___________________________________________")
        else:
             checked+=1
             print("Il post è già stato commentato da dal bot! Salto...")
             print("__________________________________________")

    print("Finito!")
    print("Post controllati : ", checked)
    print("Post commentati :", commented)
    input("Inserisci qualunque cosa per continuare...")
    sys.exit(0)
        
            
            
