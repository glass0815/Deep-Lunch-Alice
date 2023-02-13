import numpy as np


def isAnswer(rd_num):
	cnt = 0
	while True:
		input_num = int(input("1~100 숫자 입력 : "))

		if input_num < 1 or input_num > 100:
			print("1~100 숫자만 입력해주세요.")
			continue

		cnt += 1
		if input_num == rd_num:
			print(f"정답입니다! {cnt}회 만에 맞췄어요.")
			break
		elif input_num > rd_num:
			print("Down")
		elif input_num < rd_num:
			print("UP")
		else:
			print("다시 입력해주세요.")
			cnt -= 1
			continue


def run():
	print('>> Up & Down Game Start!')

	rd_num = np.random.randint(1, 100)

	print("컴퓨터가 1~100 중 랜덤 숫자 하나를 정합니다.")
	print("이 숫자를 맞춰주세요.")

	isAnswer(rd_num)


if __name__ == '__main__':
	run()
