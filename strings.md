# List of methods that can be used on strings

## Self-explanatory

    Note: [string] is a placeholder, it can either be a string ("poker-learning parrot") 
    or a variable containing a string (love = "I love sushi")

* [string].upper()
* [string].lower()
* [string].len()
* [string].str()    
        _turns 2 into "2"_

# Concatenation

Strings can be concatenated with the plus sign.

Remember to add spaces in between words.

    print "Life " + "is" + " fun!"

# String formatting with %s

Example:
 
    name = raw_input("What is your name?")
    quest = raw_input("What is your quest?")
    color = raw_input("What is your favorite color?")

    print "Ah, so your name is %s, your quest is %s, " \
    "and your favorite color is %s." % (name, quest, color)
