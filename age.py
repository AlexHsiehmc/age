driving = input('請問你有沒有開過車?')

if driving != '有' and driving != '沒有':
	print('請輸入有或沒有開過車')
	raise SystemExit

age = input('請問你的年齡?')

age = int(age)

if driving == '有':
	if age >= 18:
		print('通過測驗')

	else:
		print('你為什麼能夠開車?')

elif driving == '沒有':
	if age >= 18:
		print('快去考駕照開車')

	else:
		print('等18歲快去考駕照')