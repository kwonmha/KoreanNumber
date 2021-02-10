import num2kr

try:
	while True:
		num = int(input("Interger: "))
		print("mode 0: " + num2kr.num2kr(num, False))
		print("mode 1: " + num2kr.num2kr(num, True))
except KeyboardInterrupt:
	pass
