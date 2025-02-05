# From: https://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
# Descriptive image: https://www.geeksforgeeks.org/merge-sort/ 
# Order of ops. 
import time

def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]

for i in range(100000):
    alist.append(i)


start = time.time()
mergeSort(alist)
end = time.time()
print(start)
print("Runtime was: ", (end - start))
# print(alist)

