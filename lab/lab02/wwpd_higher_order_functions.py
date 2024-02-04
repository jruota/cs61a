def cake():
    print("beets")
    def pie():
        print("sweets")
        return "cake"
    return pie


chocolate = cake()
# beets

print(chocolate)
# Function

more_chocolate, more_cake = chocolate(), cake
# sweets

print(more_chocolate)
# cake


def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y


print(snake(10, 20))
# Function

snake(10, 20)()
# sweets

cake = "cake"
print(snake(10, 20))
# 30
