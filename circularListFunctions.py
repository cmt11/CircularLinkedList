"""
This program implements a "circular" linked list, where the last element's pointer is back to the first element.

Author: Chris Thomas
"""


"""
This function adds a new value before the "current" element of the linked list.
"""
def add(circList, newValue):
    if circList == None: # if the list is empty, create an element that points to itself
        newNode = {"data": newValue}
        newNode["next"] = newNode
        return newNode
    else: # the list is not empty
        newNode = {"data": newValue, "next": circList} # the new element will "point" to the list
        stop = circList
        while circList["next"] is not stop: # loop through the list, up to the element before the current one
            circList = circList["next"]
        circList["next"] = newNode # the end of the list will "point" back to the beginning
        return newNode # return a pointer to the new element, which is now the beginning of the list


"""
This function deletes the "current" element of the linked list.
"""
def delete(circList):
    if circList == None: # if the list is empty, return None
        return None
    else:
        if circList["next"] == circList: # if there is only one element in the list, delete that element by returning None
            return None
        else: # there is more than one element in the list
            stop = circList
            after = circList["next"]
            while circList["next"] is not stop: # loop through the list, up to the element before the current one
                circList = circList["next"]
            circList["next"] = after # "points past" the element being deleted
            return circList["next"] # return a pointer to the new current element of the list
            

"""
This function prints a more visually pleasing representation of the linked list.
"""
def printList(circList):
    if circList == None: # if the list is empty, return an empty pair of square brackets
        print "[]"
    else: # the list is not empty
        string = "["
        stop = circList
        while circList["next"] is not stop: # loop through the list, up to the element before the current one
            string += str(circList["data"]) # adds each element's data to the string
            if circList["next"] is not stop: # if we're not at the "end" of the list, add a comma and a space between elements
                string += ", "
            circList = circList["next"]
        string += str(circList["data"]) # the loop stops one element early - add that element's data to the string
        string += "]"
        print string # print the string to the screen


"""
Returns the "current" element of the linked list.
"""
def current(circList):
    if circList == None: # if the list is empty, return None
        return None
    else: # the list is not empty
        return circList["data"] # return the value of the "current" element


"""
Advances the "current" element of the linked list one forward.
"""
def advance(circList):
    if circList == None: # if the list is empty, return None
        return None
    else:
        if circList["next"] == circList: # if there is only one element in the list, the "current" element can't change
            return circList
        else:
            circList = circList["next"] # advance to the next element of the list
            return circList


"""
Searches the linked list for an element containing value.
"""
def search(circList, value):
    if circList == None: # if the list is empty, return False
        return False
    else:
        if circList["next"] == circList: # if there is only one element in the list
            if circList["data"] == value: # if that element is the one we're looking for, return True
                return True
            else: # the element is not the one we're looking for, return False
                return False
        else: # there is more than one element in the list
            stop = circList
            while circList["next"] is not stop: # loop through the list, up to the element before the current one
                if circList["data"] == value: # if this element is the one we're looking for, return True
                    return True
                circList = circList["next"] # advance to the next element of the list
            if circList["data"] == value: # the loop stops one element early - check to see if it's the one we're looking for
                return True
            else:
                return False


"""
Counts the number of elements in the linked list.
"""
def count(circList):
    if circList == None: # if the list is empty, its length is zero
        return 0
    else:
        if circList["next"] == circList: # if there is only one element in the list, its length it one
            return 1
        else: # there is more than one element in the list
            stop = circList
            counter = 0
            while circList["next"] is not stop: # loop through the list, up to the element before the current one
                counter += 1
                circList = circList["next"]
            return counter + 1 # the loop stops one element early - return one more than the counter's current value
