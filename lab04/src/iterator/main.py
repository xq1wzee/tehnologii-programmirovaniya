from iterator import ArrayIterator

def main():
    items = [10, 20, 30, 40, 50]
    iterator = ArrayIterator(items)
    while iterator.has_next():
        print(iterator.next())

if __name__ == "__main__":
    main()