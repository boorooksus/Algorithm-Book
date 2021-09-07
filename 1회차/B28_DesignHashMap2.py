from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.table[index].value is None:
            # 'self.table[index].value is None' 이 아닌
            # 'self.table[index] is None' 을 사용할 경우
            # 존재하지 않는 인덱스를 조회했을 때, 바로 빈 ListNode를 생성하기 때문
            # 즉, 절대로 True가 되지 않는 버그가 발생
            self.table[index] = ListNode(key, value)
            return

        # 해당 인덱스에 노드가 존재하는 경우
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        # 해당 key에 아무 것도 없는 경우
        if self.table[index].value is None:
            return

        p = self.table[index]
        # case1. 인덱스의 첫 번째 노드 일 때,
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            # self.table[index] = None으로 할당한다면,
            # 조회 함수에서 self.table[index].value is None 비교 할 때
            # 에러 발생
            return
        # case2. 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# leetcode: 706
# 개별 체이닝 방식
