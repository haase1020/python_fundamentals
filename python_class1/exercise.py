# # lists
# list()

# names = ['mandi', 'timothy', 'noel']
# num_list = [1, 5, 4, 7, 9]
# # x = sorted(num_list)
# num_list.sort()  # this actually changes the list


# print('this is sorted', x)
# print(num_list)
# print(type(list()))
# print(names)

# # tuples: good when need keys that are immutable
# a = ()
# print(type(a))
# b = (1, 2)  # tuple needs a comma
# print(type(b))
# c = (1, 2, 3, 4, 5)
# print(type(c))
# student = ("mandi", 2, "history", 3.5)
# print(student[0])

# # sets
# my_set = set()
# names = {"nina", "max", "nina"}  # drops duplicates

# names_list = ["mandi", "mandi", "jon", "jon", "noel"]
# names_set = set(names_list)  # this creates a set from the list no dups

# print(names_set)
# print(hash("max"))  # sets use a hashlist
# print(names)
# print(type(my_set))

# # set operations
# colors = {"red", "blue", "yellow"}

# print("blue" in colors)  # returns True

# rainbow_colors = {"red", "orange", "yellow", "green", "blue", "purple"}
# favorite_colors = {"yellow", "blue", "white"}

# # rainbow_colors.union(favorite_colors) or can use the following syntax:
# combined = rainbow_colors | favorite_colors
# print(combined)

# # intersection
# intersections = rainbow_colors & favorite_colors
# print(intersections)

# # difference: creates new set with items in one set but not the other
# differences = rainbow_colors ^ favorite_colors
# print(differences)


# # make a list from a set
# rainbow_list = list(rainbow_colors)
# print(rainbow_list)

# # dictionary: keys are immutable types
# my_dict = {}
# your_dict = dict()  # can make dictionary this way too
# nums = {"one": 1, "two": 2, "three": 3}
# nums["four"] = 4


# print(nums["one"])
# print(nums.keys())
# print(nums.get("four", "default value"))

# # list slicing
# my_list = ["h","e","l","l","o"]
# my_list.append("!")
# my_list[:3] # starts at beginning
# my_list.remove("l")
# my_list.insert(2, "l")
# my_list.pop()
# my_list.sort(reverse=True)

# # dict operations
# my_dict = {"key": "value"}
# my_dict["hello"] = "world"
# my_dict["baz"]  # this will return a key error
# my_dict.get("baz")  # this won't return a key error, so be careful
# my_dict.get("foo", "default")  # will return "default"

# "T"<"t"  lower case are lower valued in ASCII

# "is" keyword is identity

# and, or, not
# [1] and [2]  # this will return [2] since first item was "truthy"

# looping over dictionaries
hex_colors = {"red": "#ff", "green": "#008"}

for color in hex_colors:
    print(color)  # just prints out keys

for label, hex in hex_colors.items():  # this unpacks the tuple with key/value pair
    print(label, hex)
