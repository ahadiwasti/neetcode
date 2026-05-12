/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeKLists(lists []*ListNode) *ListNode {
    if len(lists) == 0 {
        return nil
    }
    for len(lists) > 1 {
        var merged []*ListNode
        for i:=0; i<len(lists); i+=2{
            l1 := lists[i]
            var l2 *ListNode
            if i+1 < len(lists){
                l2 = lists[i+1]
            }
            merged = append(merged, mergingLists(l1,l2))
        }
        lists = merged
    }
    return lists[0]
}
 func mergingLists(l1,l2 *ListNode) *ListNode{
    dummy := &ListNode{}
    curr := dummy
    for l1 != nil && l2 != nil {
        if l1.Val <= l2.Val{
            curr.Next = l1
            l1 = l1.Next
        }else{
            curr.Next = l2
            l2 = l2.Next
        }
        curr = curr.Next
    }
    if l1 != nil {
        curr.Next = l1
    }
    if l2 != nil {
        curr.Next = l2
    }
    return dummy.Next
    }
