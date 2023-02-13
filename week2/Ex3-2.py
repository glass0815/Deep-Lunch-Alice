def run():
	given_str = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
	name_list = given_str.split(",")

	# 1. 김씨와 이씨는 각각 몇 명인가요
	kim_cnt, lee_cnt = 0, 0
	for name in name_list:
		if name[0] == "김": kim_cnt += 1
		if name[0] == "이": lee_cnt += 1
	print(f"김씨는 총 {kim_cnt}명, 이씨는 총 {lee_cnt}명 입니다.")
	print()

	# 2. "이재영"이란 이름이 몇 번 반복되나요
	leejy_cnt = 0
	for name in name_list:
		if name == "이재영": leejy_cnt += 1
	print(f'"이재영"이란 이름은 총 {leejy_cnt}번 반복되었습니다.')
	print()

	# 3. 중복을 제거한 이름을 출력하세요
	result_list = []
	[result_list.append(name) for name in name_list if name not in result_list]
	print(result_list)

	name_set = set(name_list)  # 출력 순서 랜덤
	print(name_set)
	print()

	# 4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
	sort_list = sorted(result_list)
	print(sort_list)

	sort_set = sorted(name_set)
	print(sort_set)


if __name__ == '__main__':
	run()
