# Jeremiah Soyebo - 1902930 #

def selection_sort_descend_trace(list):
    for i in range(len(list) - 1):
        k = i
        for j in range(i + 1, len(list)):
            if list[k] < list[j]:
                k = j
        list[i], list[k] = list[k], list[i]
        for x in list:
            print(x, end=' ')
        print()
    return list


if __name__ == "__main__":
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)

