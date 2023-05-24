# https://www.codewars.com/kata/5567e7d0adb11174c50000a7/train/python

# This kata is about singly linked list. A linked list is an ordered set of data elements, each containing a link to its successor (and sometimes its predecessor, known as a double linked list). You are you to implement an algorithm to find the kth to last element.

# For example given a linked list of:

# a -> b -> c -> d

# if k is the number one then d should be returned
# if k is the number two then c should be returned
# if k is the number three then b should be returned
# if k is the number four then a should be returned
# if k exceeds the size of the list then None returned
# Special Note --> Node classes contain two fields; data and next. And to access the head of the list, use head. e.g. linked_list.head


def get_length(l):
    count, node = 0, l.head
    while node != None:
        node = node.next
        count += 1
    return count

def search_k_from_end(linked_list, k):
    length = get_length(linked_list)
    count, node = 0, linked_list.head
    while count < length - k:
        node = node.next
        count += 1
    return node.data if k <= length else None