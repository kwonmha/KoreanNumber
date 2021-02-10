import num2kr

try:
	while True:
		num = int(input("Interger: "))
		print("Soft mode: " + num2kr.num2kr(num, False))
		print("Hard mode: " + num2kr.num2kr(num, True))
except KeyboardInterrupt:
	pass
