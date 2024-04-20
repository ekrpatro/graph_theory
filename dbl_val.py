class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse(head):
    prev=None
    while head:
        cur=head
        head=head.next
        cur.next=prev
        prev=cur
    return prev
    

def doubleLinkedListNumber(head):    
   # reverse the list
    
    head=reverse(head)
    # multiply each node by 2    
    carry=0
    current=head
    while current:
        print(" Cur.val = ",current.val)
        current.val = current.val * 2 + carry
        carry = current.val // 10
        current.val %= 10
        prev=current
        current = current.next
    newnode=None
    # if carry exit create a node
    if carry ==1:
        newnode=ListNode(carry)
    prev.next=newnode

    # reverse the list
    
    head=reverse(head) 
    
    return head

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 2 -> 3
head = ListNode(9)
head.next = ListNode(0)
head.next.next = ListNode(0)
head.next.next.next = ListNode(0)

print("Original Linked List:")
printLinkedList(head)

# Double the number represented by the linked list
new_head = doubleLinkedListNumber(head)

print("\nLinked List after Doubling the Number:")
printLinkedList(new_head)
