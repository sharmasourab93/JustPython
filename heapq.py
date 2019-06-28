"""
Python: heapq
"""
import heapq


if __name__ == '__main__':
    li = [5, 7, 9, 1, 3]

    heapq.heapify(li)
    print("The create heap is: ", list(li))

    heapq.heappush(li, 4)
    print("The modified heap after push is :", list(li))
    print("the popped and smallest element is:", heapq.heappop(li))
    print("The 3 smallest elements in the heap", heapq.nsmallest(3, li))
    print("The 4 smallest elements in the heap", heapq.nlargest(3, li))