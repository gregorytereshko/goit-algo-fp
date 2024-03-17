class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next
  
  def reverse(self):
    prev = None
    current = self.head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev
  
  def insertion_sort(self):
    sorted_list = None
    current = self.head
    while current is not None:
      next_node = current.next
      sorted_list = self.sorted_insert(sorted_list, current)
      current = next_node
    self.head = sorted_list

  def sorted_insert(self, sorted_list, new_node):
    if sorted_list is None or sorted_list.data >= new_node.data:
      new_node.next = sorted_list
      return new_node
    current = sorted_list
    while current.next is not None and current.next.data < new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return sorted_list

def merge_sorted_lists(list1, list2):
  if list1 is None:
    return list2
  if list2 is None:
    return list1

  if list1.data <= list2.data:
    merged_list = list1
    list1 = list1.next
  else:
    merged_list = list2
    list2 = list2.next

  current = merged_list
  while list1 is not None and list2 is not None:
    if list1.data <= list2.data:
      current.next = list1
      list1 = list1.next
    else:
      current.next = list2
      list2 = list2.next
    current = current.next

  if list1 is not None:
    current.next = list1
  elif list2 is not None:
    current.next = list2

  return merged_list
  


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# реверсування однозв'язного списку
llist.reverse()

# Друк зв'язного списку після реверсування
print("Зв'язний список після реверсування:")
llist.print_list()

# Сортування однозв'язного списку вставками
llist.insertion_sort()

# Друк зв'язного списку після сортування
print("Зв'язний список після сортування:")
llist.print_list()

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

merged_list_head = merge_sorted_lists(llist.head, llist2.head)
merged_list = LinkedList()
merged_list.head = merged_list_head
print("Об'єднаний відсортований список:")
merged_list.print_list()
