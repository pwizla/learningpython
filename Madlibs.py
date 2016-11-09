"""  In this project, we'll use Python to write a Mad Libs story! Mad Libs are
stories with blank spaces that a reader can fill in with their own words. The
result is usually a funny (or strange) story.
For this project, we'll provide you with the story (feel free to modify it), but
it will be up to you to build a program that does the following:

    1. Prompt the user for input
    2. Print the entire Mad Libs story with the user's input in the right places
    """

print "Mad Libs has started :-)"

name = raw_input("What's your name?  ")
adjective1 = raw_input("Please give me an adjective to start with:  ")
adjective2 = raw_input("Please give me another one:  ")
adjective3 = raw_input("Finally, please give me a third one:  ")
print "Thanks! \nNow to the verbs."
verb1 = raw_input("Give me a first verb:  ")
verb2 = raw_input("Another verb, please:  ")
verb3 = raw_input("And a final one, please:  ")
print "Thanks! \nWe also need nouns :-)"
noun1 = raw_input("Spell a first noun:  ")
noun2 = raw_input("Another noun please:  ")
noun3 = raw_input("Great! Just two more. Give me a third noun, please:  ")
noun4 = raw_input("And your final noun is:  ")
print("Perfect!\nTo spice up things, I'm gonna ask you some more specific words.")
animal = raw_input("Please name an animal:  ")
food = raw_input("Now give me a food noun:  ")
fruit = raw_input("A fruit, then:  ")
user_number = str(raw_input("Give me a number. Any number, small or large: "))
superhero = raw_input("Now name a superhero, you can invent one if you wish ^^:  ")
country = raw_input("I also need a country:  ")
dessert = raw_input("Great! We're almost done. I just need a dessert:  ")
user_year = raw_input(" and finally, choose a year:  ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."
                      
print STORY % (adjective1, name, verb1, adjective2, noun1,
noun2, animal, food, verb2, noun3, fruit, adjective3, name, verb3, user_number, name, superhero, superhero, name, country, name, dessert, name, user_year, noun4)
