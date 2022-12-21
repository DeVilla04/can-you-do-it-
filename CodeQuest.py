# Welcome to the Lumos Coding Quest
# you have been given a linked list with duplicate values
# upon running this code, you will see a string that has been formed by collecting the data in the nodes of the linked list
# you need to complete the "MyAnswer" function and ensure that it removes the duplicate nodes from the linkedlist
# when you collate the string that this new linked list contains, you will get the link to the whitelist form

# Note:- "list" represents the said linked list

from helper import *


def MyAnswer(self):
    # please put in your answer  here
    current = self.headval
    prev = None
    dupl_dict = {}
    answer = ""
    while current:
        if current.dataval not in dupl_dict:
            answer += current.dataval
            dupl_dict[current.dataval] = None
            prev = current
        else:
            prev.nextval = current.nextval
        current = current.nextval
    print(answer)


MyAnswer(list)
