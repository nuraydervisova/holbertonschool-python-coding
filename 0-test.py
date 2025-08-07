Rectangle = __import__('0-rectangle').Rectangle

try:
    r = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    r = Rectangle("2", 3)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

r = Rectangle(2, 3)
print(r.width, r.height)

try:
    r.width = -1
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    r.height = "4"
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))
