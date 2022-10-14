from ast import If
from platform import node
import re
from clearEmptyString import clearEmptyString

class Person:
  def __init__(self, id: str, name: str, score: int):
    self.id = id
    self.name = name
    self.score = score

class List:
  def __init__(self, data: Person):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    
  def search (self, id) :
    current_node = self.head
    while current_node != None :
      if current_node.data.id == id :
        return current_node
      else :
        current_node = current_node.next

  def add (self, list: List) :
    list.next = self.head
    self.head = list

  def delete (self, id: str) :
    if self.head.data.id == id :
      self.head = self.head.next
      return

    current_node = self.head
    while current_node != None :
      if current_node.next != None:
        print(current_node.next.data.id,id)
        if current_node.next.data.id == id:
          if current_node.next.next != None:
            current_node.next = current_node.next.next
          else:
            current_node.next = None
      print("sss")
      current_node = current_node.next

  def sort (self):
    current_node = self.head
    while current_node != None :
      if current_node.data.score > current_node.next.data.score:
        self.delete(current_node.data.id)
        current_node.next = current_node.next.next
        current_node.next.next = current_node
      else:
        current_node = current_node.next


  def printLists (self):
    current_node = self.head
    while current_node != None :
      print(current_node.data.id, current_node.data.name, current_node.data.score)
      current_node = current_node.next


def createLinkedList(data):
    linkedList = LinkedList()

    for line in data:
      splitted = re.split("\s", line)
      cleanData = clearEmptyString(splitted)
      id = cleanData[0]
      fullname = cleanData[1] + " " + cleanData[2]
      score = int(cleanData[3])
      person = Person(id, fullname, score)
      list = List(person)
      linkedList.add(list)
    
    return linkedList

def merge(lists1: LinkedList, lists2: LinkedList):
  current_node = lists2.head
  
  while current_node != None :
    found = lists1.search(current_node.data.id)
    if found != None :
      found.data.score = found.data.score + current_node.data.score
    else :
      newPerson = Person(current_node.data.id,current_node.data.name,current_node.data.score)
      newList = List(newPerson)
      lists1.add(newList)
  
    current_node = current_node.next

  return lists1

data1 = open("data1.dat","r")
linkedList1 = createLinkedList(data1)
data2 = open("data2.dat","r")
linkedList2 = createLinkedList(data2)

mergedLinkedList = merge(linkedList1, linkedList2)
mergedLinkedList.sort()
mergedLinkedList.printLists()
