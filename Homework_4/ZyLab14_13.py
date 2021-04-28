# Jeremiah Soyebo - 1902930 #

# Global variable
num_calls = 0


def partition(userIDs, i, k):

    pivot = userIDs[k] 
    index = i - 1
    for j in range(i, k):
        if userIDs[j] <= pivot:
            index += 1
            userIDs[index], userIDs[j] = userIDs[j], userIDs[index]
    userIDs[index+1], userIDs[k] = userIDs[k], userIDs[index+1]
    return index+1


def quicksort(userIDs, i, k):
    
    if i < k:
        piv = partition(userIDs, i, k)
        quicksort(userIDs, i, piv-1)
        quicksort(userIDs, piv+1, k)


if __name__ == "__main__":
    
    userIDs = []
    userID = input()
    while userID != "-1":
        userIDs.append(userID)
        userID = input()
# Initial call to quicksort
    quicksort(userIDs, 0, len(userIDs) - 1)
    num_calls = int(2 * len(userIDs) - 1)
# Print number of calls to quicksort
    print(num_calls)

# Print sorted user ids
for userID in userIDs:
    print(userID)
