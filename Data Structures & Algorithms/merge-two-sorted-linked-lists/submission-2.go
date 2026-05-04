/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dumb := &ListNode{}
	ptr := dumb
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			ptr.Next = list1
			list1 = list1.Next
		}else{
			ptr.Next = list2
			list2 = list2.Next
		}
		ptr = ptr.Next
	}
	if list1 != nil {
		ptr.Next = list1
	}else if list2 != nil {
		ptr.Next = list2
	}
	return dumb.Next
}
