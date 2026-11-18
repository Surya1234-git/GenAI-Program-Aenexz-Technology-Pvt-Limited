marks = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks)

print("List:", marks, type(marks))
print("Tuple:", marks_tuple, type(marks_tuple))

highest = max(marks)
lowest = min(marks)
print("Highest mark:", highest)
print("Lowest mark:", lowest)

passed = (marks[0] >= 40) + (marks[1] >= 40) + (marks[2] >= 40) + (marks[3] >= 40) + (marks[4] >= 40)
print("Students with 40 or more:", passed)

valid = lowest >= 0 and highest <= 100
print("All marks between 0 and 100:", valid)

marks[1] = 45
print("List after change:", marks)
print("Tuple:", marks_tuple)

# Changing marks[1] worked because a list is mutable. Doing the same on the
# tuple, marks_tuple[1] = 45, gives a TypeError since tuples cannot be changed
# after they are created. I left that line out so the program runs fully.
