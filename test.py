import num2kr
import kr2num

try:
	print("Testing Number -> Korean")
	while True:
		num = int(input("Integer: "))
		print(num2kr.num2kr(num))
except KeyboardInterrupt:
	pass

print()

try:
	print("Testing Korean -> Number")
	while True:
	    kr_str = input("Korean: ")
	    print(kr2num.kr2num(kr_str))
except KeyboardInterrupt:
	pass