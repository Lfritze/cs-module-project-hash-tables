# This is a singly linked list

class Node:
  def __init__(self, value):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

# Note insert at head is quicker than insert at tail - dont's have to traverse from head
  def insert_at_head(self, node):
    node.next = self.head
    self.head = node

  def find(self, value):
    current = self.head
    # Traverse List
    while current is not None:
      if current.value == value:
        # Then you found it
        return current
      current = current.next
    return None

  def delete(self, value):
    current = self.head
    if current is None:
      return None
    # To delete the head of list (special case)
    if current.value == value:
      self.head = self.head.next
      return current

    # General cases
    previous = current
    current = current.next

    while current is not None:
      if current.value == value: # Delete it
        previous.next = current.next # cuts out old node 
        return current
      else:
        previous = previous.next
        current = current.next
    return None # if we got nothing then it was found

    
    """
    NOTES

Also the linked list works by way of key value pair
    """