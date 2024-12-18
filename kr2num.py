import math

"""
Developed by Junseong Kim, Atlas Guide
codertimo@goodatlas.com / github.com/codertimo
Korean to number

Forked & Modified by WieeRd

Forked & Modified by kwonmha
: fix bug case - consecutive arabic numbers, ex) 12만2천
"""

numbers = [
    # Digits
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),

    ("일", 1),
    ("이", 2),
    ("삼", 3),
    ("사", 4),
    ("오", 5),
    ("육", 6),
    ("칠", 7),
    ("팔", 8),
    ("구", 9),

    ("하나", 1),
    ("한", 1),
    ("두", 2),
    ("둘", 2),
    ("세", 3),
    ("셋", 3),
    ("네", 4),
    ("넷", 4),
    ("다섯", 5),
    ("여섯", 6),
    ("일곱", 7),
    ("여덟", 8),
    ("여덜", 8),
    ("아홉", 9),

    # Digits + Unit
    ("스물", 20),
    ("서른", 30),
    ("마흔", 40),
    ("쉰",   50),
    ("예순", 60),
    ("일흔", 70),
    ("여든", 80),
    ("아흔", 90),

    # Mini Unit
    ("열", 10),
    ("십", 10),
    ("백", 10**2),
    ("천", 10**3),

    # Unit
    ("만", 10**4),
    ("억", 10**8),
    ("조", 10**12),
    ("경", 10**16),
    ("해", 10**20),
]

float_nums = [
    ("일", 1),
    ("이", 2),
    ("삼", 3),
    ("사", 4),
    ("오", 5),
    ("육", 6),
    ("칠", 7),
    ("팔", 8),
    ("구", 9)
]


def kr2num(kr_str):
    decode_result = []
    result = 0
    temp_result = 0
    index = 0

    float_dividing = kr_str.split("점")
    float_result = ""
    if len(float_dividing) == 2:
        kr_str = float_dividing[0]
        float_num = float_dividing[1]
        for c in float_num:
            for float_num, float_value in float_nums:
                if c == float_num:
                    float_result += str(float_value)
                    break
        if len(float_result) == 0:
            float_result = 0.0
        else:
            float_result = float("0." + float_result)
    else:
        float_result = 0.0

    while index < len(kr_str):
        for number, true_value in numbers:
            if index + len(number) <= len(kr_str):
                # numbers에서 일치하는 글자의 숫자값을 추가한다.
                if kr_str[index:index + len(number)] == number:
                    # 연속으로 숫자가 나오면 이전에 추가된 값을 빼고 
                    # 그 값에서 10을 곱한 뒤 현재 값을 더해서 추가한다.
                    if is_prev_digit and '1' <= number <= '9':
                        prev_value = decode_result.pop()[0]
                        prev_value *= 10
                        prev_value += true_value
                        decode_result.append((prev_value, False))
                    # 기본 로직
                    else:
                        # (숫자, 10의 배수 단위인지)
                        decode_result.append((true_value, math.log10(true_value).is_integer()))
                        is_prev_digit = False
                    
                    #숫자가 연속으로 나올 경우를 대비해 체크
                    if '1' <= number <= '9':
                        is_prev_digit = True

                    if len(number) == 2:
                        index += 1
                    break
        index += 1

    for index, (number, is_natural) in enumerate(decode_result):
        if is_natural:
            # ****억, ****만 같은 단위를 처리
            if math.log10(number) > 3 and (math.log10(number) - 4) % 4 == 0:
                result += temp_result * number
                temp_result = 0

            elif index >= 1:
                # 앞(왼쪽) 자리의 is_natural값이 false
                # '이십억'의 '이십'과 같은 경우를 처리
                if not decode_result[index - 1][1]:
                    temp_result += number * decode_result[index - 1][0]
                
                # 맨 마지막 일의 자리의 1 처리
                else:
                    temp_result += number
            
            # 맨 첫자리가 1일 때
            else:
                temp_result += number

        else:
            # 맨 마지막 일의 자리의 1 제외 다른 숫자들
            if index + 1 == len(decode_result):
                temp_result += number

            # list 다음(뒤)이 만 단위 이상일 때
            elif math.log10(decode_result[index + 1][0]) > 3 and (math.log10(decode_result[index + 1][0]) - 4) % 4 == 0:
                temp_result += number

    result += temp_result

    if float_result != 0.0:
        result += float_result

    return result
