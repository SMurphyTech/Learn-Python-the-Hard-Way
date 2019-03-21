formatter = "{} {} {} {}"

#each print replaces the place holder {} in the formatter string and replaces them with
#each value in their sequence, then prints that out.

#replaces {} {} {} {} with 1 2 3 4
print(formatter.format(1, 2, 3, 4))
#replaces {} {} {} {} with one two three four
print(formatter.format("one", "two", "three", "four"))
#replaces {} {} {} {} with True False False True
print(formatter.format(True, False, False, True))
#replaces each {} in formatter with the same full formatter string, so essentially
#the string formatter is printed four times
print(formatter.format(formatter, formatter, formatter, formatter))
#replaces {} {} {} {} with each line in the poem
print(formatter.format(
    "Flowers are beautiful,",
    "the sky is beautiful,",
    "I am beautiful,",
    "Cheeseburger"
))