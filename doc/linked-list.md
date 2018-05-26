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
