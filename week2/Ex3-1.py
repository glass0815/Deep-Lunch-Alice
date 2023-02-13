def run():
	given_list = [-1, 1, 3, -2, 2]

	# 리스트 컴프리헨션(List Comprension) : 직관적, 간결, 속도 향상
	answer_list = [elm for elm in given_list if elm < 0]
	# listA.extend(listB) : listA와 listB를 병합. 뒤에 그대로 붙여준다.
	# + 를 사용해도 같은 기능을 하는데, 이 경우 새로운 리스트를 반환한다. (주소값이 다름)
	answer_list.extend([elm for elm in given_list if elm > 0])
	# 0에 대한 기준은 주어지지않아서 고려하지않음

	return answer_list


'''
	'__name__이라는 변수의 값이 __main__이라면 아래의 코드를 실행하라.'
 			=> 이 모듈을 직접 실행시켰을 때만 아래의 코드를 실행하라.
			=> import 되었을 경우는 실행 x.
   			=> 모듈화 시킬 때 사용하기 좋음.
'''
if __name__ == '__main__':
	answer = run()
	print(answer)
