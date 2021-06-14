from chapter_02.linked_list import LinkedList


def kth_to_last_runner(ll, k):
    runner = current = ll.head
    for _ in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current



def kth_to_last_recursive(ll, k):
    def Recursion(head, k):
        if head is None:
            return 0,None
        else:
            i,Node=Recursion(head.next, k)
            i+=1
            if i==k:
                return i,head
            else:
                return i, Node     
    
    if ll is None:
        return None
    else:
        head=ll.head
        i, Node=Recursion(head, k)
        return Node





test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 3, 30),
    ((10, 20, 30, 40, 50), 5, 10),
)


Method_cases=[kth_to_last_runner,kth_to_last_recursive]

#Method_cases=[kth_to_last_recursive]

def test_kth_to_last():
    for kth_to_last in Method_cases:
        for linked_list_values, k, expected in test_cases:
            ll = LinkedList(linked_list_values)
            assert kth_to_last(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()
           

