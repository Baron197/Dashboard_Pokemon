def func(param='Kasihku'):
    print("func() in one.py " + param)

nama = 'Ajinomoto'
print("top-level in one.py")
print(__name__)

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")