#tao 1 nut
class Node:
  def __init__(self, value=None, next=None):
    self.value = value 
    self.next = next #tro vao nut tiep theo
#tao day vong lien ket
class CircularLinkedList:
  def __init__(self):
    self.head = None
  #them nut vao cuoi day vong
  def insert(self, value):
    node = Node(value, self.head) #tao 1 nut
    if self.head == None: #nut dau co trong ko ?
      self.head = node
      self.head.next = node 
    else:
      temp = self.head
      while temp.next != self.head: 
        temp = temp.next 
      
      temp.next = node #them 1 nut
  
  def deleteHead(self):
    deleted_node = self.head
    if self.head.next == self.head: 
      self.head = None
    else:
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
      self.head = self.head.next 
      temp.next = self.head 
    del deleted_node

  def delete(self, value):
    if self.head: 
      if self.head.value == value: 
        self.deleteHead()
        return
      else:
        temp = self.head.next 
        prev=self.head
        while temp != self.head:
          if temp.value == value:
            prev.next = temp.next
            del temp
            return
          else:
            prev = temp
            temp = temp.next
    


  def traverse(self):
     if self.head:
      print(self.head.value, end="\t") 
      temp = self.head.next
      while temp != self.head:
        print(temp.value, end="\t")
        temp = temp.next
      print("")
  
  def isLastNode(self):
    if self.head.next == self.head:
      return True
    else:
      return False

def getKthNode(start, m):
    temp = start
    for i in range(1, m+1):
       temp = temp.next
    return temp
def initializeLinkedList(n):
    ll = CircularLinkedList()

    for i in range(1, n+1):
       ll.insert(i)
    return ll
def josephusProblem(n, m):
  ll = initializeLinkedList(n) 
  if ll.head is None: 
    return None
  start = ll.head 
  while not ll.isLastNode():
    m_node = getKthNode(start, m)
    start = m_node.next 
    ll.delete(m_node.value)
  return start.value
n = int(input())
m = int(input())
last_person_alive = josephusProblem(n, m)
print("The position of the person winner is", last_person_alive)