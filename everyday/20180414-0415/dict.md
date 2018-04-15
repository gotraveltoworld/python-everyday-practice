# Python lists function.

## Content:
1. 字典(dictionary)是一種映射形式的資料結構，
    * dict的index幾乎可以是任何形式的型別，不同於list，必須要是正整數。
    * 一個dict含有索引構成的群集(a collections of indices)，就是keys和values。這種key和value構成的關聯稱為鍵值與值對組(key-value pair)，有時也可以稱為項目(item)。
    * `ditc`這個方法可以建立一個空的dict。
    * 顯示的符號是`{}`(squiggly brackets)，代表空的字典(empty dictionary)。指定特定的鍵與值可以用`[]`(square brackets)指派，例如：`dic['key']  = 'Hi'`。
    * dict是無序的元素組合，運用雜湊表(hashtables)的方式來降低查找元素的時間。
    * dict可用len計算__鍵值__的數量。
    * dict用`in`運算子，可以找出在__鍵值__中有存在的索引。如果要找值，需要使用`dict.values()`進行比對。
2. 字典(dict)可以做為計數器的一個群集。
    * 利用鍵與值對應，可以計算每個每個鍵值出現的次數，例如：計算文本中所有英文字母出現的次數，就可以用26字母當作鍵值，值則是次數，就可以很好的表示各個字母出現的次數。
