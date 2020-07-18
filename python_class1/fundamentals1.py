# don't do the following:
# def foo(a, b=[]):

# instead do:
#  def foo(a, b=None):
#     if b is None:
#         b = []

# ex 1
def calc_nums(x, y, operation="add"):
    if operation == "add":
        print(x+y)
    if operation == "subtract":
        print(x-y)


calc_nums(4, 5, "subtract")
