# KoreanNumber

한글 <-> 숫자 변환 라이브러리

* 기존 [WieeRd의 라이브러리](https://github.com/WieeRd/KoreanNumber)에서 숫자가 연속해서 나오는 경우의 처리를 추가한 버전

## Number -> Korean

```python

from num2kr import num2kr

# num = int(input("Integer: "))
num = 12345678
print(num2kr(num)) # same as num2kr(num, 0)
print(num2kr(num, 1))

# >>> 1234만 5678
# >>> 일천이백삼십사만오천육백칠십팔

```

## Korean -> Number

```python

from kr2num import kr2num

# kr_str = input("Korean: ")
kr_str = "일조삼천육백칠십일억이천구백삼십칠만사천오백십일"
print(kr2num(kr_str))

# >>> 1367129374511

kr_str = "22억1526만오천6백31"
print(kr2num(kr_str))

# >>> 2215265631

```


## Credit

kr2num: forked from https://github.com/codertimo/korean2num  
num2kr: inspired by https://m.blog.naver.com/wideeyed/221771836059

KoreanNumber: forked from https://github.com/WieeRd/KoreanNumber