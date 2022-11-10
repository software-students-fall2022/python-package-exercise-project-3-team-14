from dailydose import hang
from dailydose import fact
from dailydose import news
from dailydose import battleship


print("Here's a fun fact\n\n")
one_fact= fact.get()
for (i, random_fact) in enumerate(one_fact):
    print(f"{'-' * 15}")
    print(f"Random Fun Fact #{i+1}:")
    print(random_fact['heading'])
    print("\n"+random_fact['content'])

print("\nMultiple fun facts without details!\n")
more_facts = fact.get(3,False)
for (i, random_fact) in enumerate(more_facts):
    print(f"{'-' * 15}")
    print(f"Random Fun Fact #{i+1}:")
    print(random_fact['heading'])

print("Here's the news!\n")

print("\n\nHere's some new about business and finance\n")
subject = "business-and-finance"
titular = "BUSINESS AND FINANCE"
news.get_headlines(subject, titular)


x=input("\n\nDo you want to start a game of hangman? (y/n)")
if x=="y":
    hang.hangman("5")

x=input("\n\nDo you want to start a game of battleship? (y/n)")
if x=="y":
    battleship.main("2","5")


