def bubble_sort(items):
    '''Return array of items, bubble sorted in ascending order'''
    for i, num in enumerate(items):
        try:
            if items[i+1] < num:
                items[i] = items[i+1]
                items[i+1] = num
                bubble_sort(items)
        except IndexError:
            pass
    return items

def merge_sort(items):
    '''Return array of items, merge sorted in ascending order'''
    if len(items) >1:
        mid = len(items)//2
        L = items[:mid]
        R = items[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                items[k] = L[i]
                i+=1
            else:
                items[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            items[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            items[k] = R[j]
            j+=1
            k+=1
    return items

def quick_sort(items):
    '''Return array of items, quick sorted in ascending order'''
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quicksort(items[:i])
        second_part = quicksort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
