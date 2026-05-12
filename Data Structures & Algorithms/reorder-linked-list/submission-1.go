/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
    fast, slow := head.Next, head
    for fast != nil && fast.Next != nil {
        fast = fast.Next.Next
        slow = slow.Next
    }
    first, second :=head, slow.Next
    slow.Next = nil
    var prev *ListNode
    for second != nil {
        tmp := second.Next
        second.Next = prev
        prev = second
        second = tmp
    }

    second = prev
    for second != nil{
            temp1,temp2 := first.Next, second.Next
            first.Next = second
            second.Next = temp1
            first,second = temp1,temp2

    }
}
