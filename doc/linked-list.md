# Insert - O(1)
1. 新增一個 node
2. 把新的 node 接上原本的 list
3. 把原本的 list 接到新的 node

```
prev -> next

prev -> next
         /
    cur -

prev   next
  \    /
    cur
```

# Delete - O(n)
1. 找到要刪除的點
2. 把前一個點的 next 指到下一個點

# Reverse - O(n)
## Concept
使用三個指標 prev, current, next
- prev 起始為 null
- current 起始為 head
- next 起始為 head.next

## Detail
1. 每次只做 `cuurent.next = prev`
2. 往前移動三個指標 (注意 next 是 null 時就要停下)
3. loop 直到 current 是 null
4. 最後 prev 會停在新的 Head
