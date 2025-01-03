import random


greetings = ["hello", "sup", "howdy", "greetings"]
goodbyes = ["bye", "goodbye", "CU soon", "CU later"]

keywords = ["music", "pet", "book", "game", "hello", "linux", "minecraft", "windows", "python", "sonic", "all keywords"]
responses = ["music is so relaxing", "cats are my favorite", "idk im not really a reading person", "i love video games im even collecting them", "hello i hope your having a wonderful day", "ahh yes linux the os for programmmer, you should really use it if you are programming", "minecraft is the best game in the world", "windows is good but flawed there sure is a room for improvment", "to start coding with python type print('hello world')", "Blue Streak...speeds by, Sonic the Hedgehog!", "music,pet,book,game,hello,linux,minecraft,windows,python,sonic"]

print(random.choice(greetings))

print('welcome to thisbot ai coded by thiscat')
print('enter some keywords to start chatting')
user = input("say something(or type bye to quit): ")
user = user.lower()


while (user != "bye"):
    keyword_found = False

    for index in range(len(keywords)):
        if (keywords[index] in user):
            print("bot: " + responses[index])

            keyword_found = True
            


    if (keyword_found == False):
        new_keyword = input("im not sure how to respond what keyword should i respond to?: ")
        keywords.append(new_keyword)
        new_response = input("how should i respond to " + new_keyword + "? ")
        responses.append(new_response)

    user = input("Say something (or type bye to quit): ")
    user = user.lower()
    


            





