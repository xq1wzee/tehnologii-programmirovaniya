from strategy import Sorter, BubbleSortStrategy, QuickSortStrategy

def main():
    sorter = Sorter()
    sorter.set_strategy(BubbleSortStrategy())
    array1 = [5, 3, 8, 4, 2]
    sorter.sort_array(array1)
    print("Bubble Sort:", array1)
    sorter.set_strategy(QuickSortStrategy())
    array2 = [5, 3, 8, 4, 2]
    sorter.sort_array(array2)
    print("Quick Sort:", array2)

if __name__ == "__main__":
    main()