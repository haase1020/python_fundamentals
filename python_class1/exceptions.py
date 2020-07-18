# this will throw an error
try:
    int("a")
except ValueError as e:  # put exact error you are expecting
    print("oops, you can't do that!", e)

print("this is the end of my program")


# install python -m pip install requests
# using requests libraray can request APIs
