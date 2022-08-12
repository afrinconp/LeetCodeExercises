"""2) Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://leetcode.com/problems/add-two-numbers/
"""
class ListNode:
       def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
l1=ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
l2=ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))
result=ListNode(0)
result_tail=result
extra=0
while l1 or l2 or extra!=0:
  if l1 ==None:
    valor1=0
  else: 
    valor1=l1.val
  if l2 ==None:
    valor2=0
  else: 
    valor2=l2.val
  valor,residuo=divmod(valor1+valor2+extra,10)
  result_tail.next=ListNode(residuo)
  result_tail=result_tail.next
  extra=valor
  if l1 !=None:
    l1=l1.next
  if l2 !=None:
    l2=l2.next
result.next
