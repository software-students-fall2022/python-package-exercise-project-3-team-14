from dailydose import hang
from dailydose import fact
from dailydose import news
from dailydose import battleship


print("Here's a fun fact!")
one_fact= fact.get()

print("Multiple fun facts without details!")
more_facts = fact.get(3,False)

print("Here's the news!\n")

print("Here's some new about business and finance")
subject = "business-and-finance"
titular = "BUSINESS AND FINANCE"
news.get_headlines(subject, titular)


x=input("Do you want to start a game of hangman? (y/n)")
if input=="y":
    hang.hangman(5)

x=input("Do you want to start a game of battleship? (y/n)")
if input=="y":
    battleship.main("4","10")


