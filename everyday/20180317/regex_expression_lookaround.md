# Python's regex practice.
* Regex practice sote: https://regex101.com/
* Basic function: https://repl.it/@Traveler/Python-String-practice-All
* Regex(中文參照):
    1. http://blog.staynoob.cn/post/2017/01/regular-expression-lookahead-lookbehind/
    2. https://i.linuxtoy.org/docs/guide/ch26s09.html
    3. https://baike.baidu.com/item/%E9%9B%B6%E5%AE%BD%E6%96%AD%E8%A8%80#1
    4. http://hooopo.iteye.com/blog/407062
    5. https://leongfeng.github.io/2017/03/10/regex-java-assertions/

* lookaround/zero-width assersion(零寬斷言)，基本名稱
    1. (?:exp)符合條件，但不創建分組的結果(matches pattern but does not capture the match)
    2. (?=exp)正向先行斷言(lookahead)
    3. (?!exp)負向先行斷言(negative lookahead)
    4. (?<=exp)正回顧後發斷言(lookbehind)
    5. (?<!exp)負回顧後發斷言(negative lookbehind)

* 功能說明
    1. (?:a)(b)\\1符合abb，如果是(a)(b)\\1則符合aba。 <= Java支援
    2. a(?=b), 斷言a後面有b，匹配ab但不匹配aa，回傳a。
    3. a(?!b), 斷言a後面沒有b，匹配aa但不匹配ab，回傳a。
    4. (?<=a)b, 斷言b前面有a，匹配ab但不匹配bb，回傳b。
    5. (?<!a)b, 斷言b前面沒有a，匹配bb但不匹配ab，回傳b。

* Other
    1. 幾種簡單的正規表示式(參照):
        - `[A-Z](?<=B)`, [A-Z]之間只選擇B
        - `[A-Z](?<!B)`, [A-Z]之間只排除B
        - `(?!B)[A-Z]`, [A-Z]之間只排除B
        - `(?!^[a-z]+$)`, 排除纯字母
        - `(?!^[0-9]+$)`, 排除纯數字
        - `^[/\w\.-]+(?<!\.html)$`, 排除以HTML結尾的字串
        - `\b[0-9]\b(?<=[13579])`, 0-9中的奇數
        - `[a-z]+(?=;)`, 分號前所有字母
        - `(?!.*?[lo0])\b[a-z0-9]+\b`, 不包含lo0的字串
        - `\b[a-z]+(?<!z)\b`, 不以z結尾的單詞

    2. 實作問題:
        需求：字母、數字组合，不區分大小寫，不能只有純數字或是純字母，長度6-16個字元。
        - 基本正規表示式：^[a-z0-9]{6,16}$
        - 結果：`(?!^[a-z]+$)(?!^[0-9]+$)^[a-z0-9]{6,16}$`
##
```python
class RegexPractice:
    """
    Regular expression:
    * lookahead
        1. positive
        2. negative
    * lookbehind
        1. positive
        2. negative
    """
    @classmethod
    def reg(cls, pattern = '', text = ''):
        return re.compile(pattern, re.VERBOSE).search(text)
    @classmethod
    def lookahead_positive(cls):
        return cls.reg('g(?=oo)', text = 'google search.')
    @classmethod
    def lookahead_negative(cls):
        return cls.reg('goo(?!ggg)', text = 'google search.')
    @classmethod
    def lookbehind_positive(cls):
        return cls.reg('(?<=g)oo', text = 'google search.')
    @classmethod
    def lookbehind_negative(cls):
        return cls.reg('(?<!g)gle', text = 'google search.')

```