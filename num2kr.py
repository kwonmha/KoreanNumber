digit_name = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
unit = ['', '십', '백', '천']
unit_10k = ['', '만', '억', '조', '경', '해', '자', '양', '구', '간', '정', '재', '극']

def num2kr(num : int, space=True, mode=0):
	if num>=pow(10000, len(unit_10k)+1):
		return None # way too big

	split_10k = []
	while num!=0:
		num, rem = divmod(num, 10000)
		split_10k.append(str(rem))

	kr_str = []
	for i in range(len(split_10k)):
		if split_10k[i]!='0':
			kr_str.insert(0, split_10k[i] + unit_10k[i])

	glue = ' ' if space else ''
	kr_str = glue.join(kr_str)

	return kr_str