# NullPointer should be set to -1 if using array element with index 0

NULLPOINTER = -1

# Declare record type to store data and pointer
class ListNode:
  def __init__(self):
    self.Data = ""
    self.Pointer = NULLPOINTER


def InitialiseList():
  List = [ListNode() for i in range(7)]
  StartPointer = NULLPOINTER # set start pointer
  FreeListPtr = 0    # set starting position of free list
  for Index in range(6): # link all nodes to make free list
    List[Index].Pointer = Index + 1
  List[6].Pointer = NULLPOINTER #last node of free list
  return(List, StartPointer, FreeListPtr)


def InsertNode(List, StartPointer, FreeListPtr,NewItem):

  if FreeListPtr != NULLPOINTER:
    # there is space in the array
    # take node from free list and store data item
    NewNodePtr = FreeListPtr
    List[NewNodePtr].Data = NewItem
    FreeListPtr = List[FreeListPtr].Pointer
    # find insertion point
    PreviousNodePtr = NULLPOINTER
    ThisNodePtr = StartPointer # start at beginning of list
    while ThisNodePtr != NULLPOINTER and List[ThisNodePtr].Data < NewItem:
    # while not end of list
      PreviousNodePtr = ThisNodePtr # remember this node
    # follow the pointer to the next node
      ThisNodePtr = List[ThisNodePtr].Pointer

    if PreviousNodePtr == NULLPOINTER: # insert new node at start of list
      List[NewNodePtr].Pointer = StartPointer
      StartPointer = NewNodePtr
    else: # insert new node between previous node and this node
      List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
      List[PreviousNodePtr].Pointer = NewNodePtr
  else:
    print("no space for more data")
  return(List, StartPointer, FreeListPtr)


def FindNode(List, StartPointer, DataItem): # returns pointer to node
  CurrentNodePtr = StartPointer # start at beginning of list
  while CurrentNodePtr != NULLPOINTER and List[CurrentNodePtr].Data != DataItem:
    # not end of list,item not found
    # follow the pointer to the next node
    CurrentNodePtr = List[CurrentNodePtr].Pointer
  return(CurrentNodePtr) # returns NullPointer if item not found


def DeleteNode(List, StartPointer, FreeListPtr,DataItem):
  ThisNodePtr = StartPointer # start at beginning of list
  while ThisNodePtr != NULLPOINTER and List[ThisNodePtr].Data != DataItem:
    # while not end of list and item not found
    PreviousNodePtr = ThisNodePtr # remember this node
    # follow the pointer to the next node
    ThisNodePtr = List[ThisNodePtr].Pointer
  if ThisNodePtr != NULLPOINTER: # node exists in list
    if ThisNodePtr == StartPointer: # first node to be deleted
      StartPointer = List[StartPointer].Pointer
    else:
      List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer
    List[ThisNodePtr].Pointer = FreeListPtr
    FreeListPtr = ThisNodePtr
  else:
    print("data does not exist in list")
  return(List, StartPointer, FreeListPtr)


def OutputAllNodes(List, StartPointer):
  CurrentNodePtr = StartPointer # start at beginning of list
  if StartPointer == NULLPOINTER:
    print("No data in list")
    print(CurrentNodePtr)
  while CurrentNodePtr != NULLPOINTER: # while not end of list
    print(CurrentNodePtr, "",List[CurrentNodePtr].Data)
     
    # follow the pointer to the next node
    CurrentNodePtr = List[CurrentNodePtr].Pointer



def GetOption():
  print("1: insert a value")
  print("2: delete a value")
  print("3: find a value")
  print("4: output list")
  print("5: end program")
  response = input("Enter your choice: ")
  return(response)

List, StartPointer, FreeListPtr = InitialiseList()
Option = GetOption()
while Option != "5":
  if Option == "1":
    Data = input("Enter the value: ")
    List, StartPointer, FreeListPtr = InsertNode(List, StartPointer, FreeListPtr, Data)
    OutputAllNodes(List, StartPointer)
  elif Option == "2":
    Data = input("Enter the value: ")
    List, StartPointer, FreeListPtr = DeleteNode(List, StartPointer,FreeListPtr,Data)
    OutputAllNodes(List, StartPointer)
  elif Option == "3":
    Data = input("Enter the value: ")
    CurrentNodePtr = FindNode(List, StartPointer,Data)
    if CurrentNodePtr == NULLPOINTER:
      print("data not found")
    print(StartPointer, FreeListPtr)
    for i in range(7) :
      print(i, " ", List[i].Data, " ", List[i].Pointer)
  elif Option == "4":
    OutputAllNodes(List, StartPointer)
  Option = GetOption()

#end