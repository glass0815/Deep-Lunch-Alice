import argparse
import cv2


def run(args):
	# 이미지 불러오기
	image_path = args.img_path
	image = cv2.imread(image_path)
	# 이미지 사이즈 변환
	resized_image = cv2.resize(image, (500, 500),
	                           interpolation=cv2.INTER_LANCZOS4)

	smile_path = args.smile_path
	smile_ori = cv2.imread(smile_path)
	resized_smile = cv2.resize(smile_ori, (50, 50),
	                           interpolation=cv2.INTER_LANCZOS4)
	# 이미지 그레이 스케일로 변환
	smile_gray_scale = cv2.cvtColor(resized_smile, cv2.COLOR_BGR2GRAY)

	s_h, s_w, s_c = resized_smile.shape
	crop_image = resized_image[200:200 + s_h, 260:260 + s_w]

	# 합성
	'''
		cv2.copyTo(src, mask, sdt=None) -> dst
		src : 입력영상
		mask : 마스크 영상
		dst : 출력 영상
		- 만약 입력영상과 크기 및 타입이 같은 출력영상을 입력으로 지정하면 출력영상을 새로 생성하지 않고 연산을 수행. 그렇지 않으면 출력연산을 새로 생성하여 연산을 수행한 후 반환
		- 입력영상에서 추출한 비행기 마스크를 출력영상으로 합성한다는 의미.
		- 세 영상은 모두 사이즈가 같아야하고, 입력영상과 출력영상은 타입 또한 같아야 한다. mask 영상은 그레이스케일이어야한다.
	'''
	cv2.copyTo(resized_smile, smile_gray_scale, crop_image)
	resized_image[200:200 + s_h, 260:260 + s_w] = crop_image

	# 텍스트 입력
	'''
		opencv의 경우 한글 텍스트 입력이 지원되지 않기 때문에 한글 텍스트 사용시 PIL로 변환하여 사용한다.
	'''
	cv2.putText(resized_image, "Jeon Yuri", (200, 450), cv2.FONT_HERSHEY_SIMPLEX,
	            1, (255, 255, 255), 2)

	# 이미지 출력
	cv2.imshow('my picture', resized_image)
	cv2.waitKey()


if __name__ == "__main__":
	# 커맨드 라인 실행 시, 인자 받아오기
	parser = argparse.ArgumentParser(description='opencv example')
	parser.add_argument('--img_path',
	                    default='./pic/mypicture.jpg',
	                    type=str,
	                    help='image path for test')
	parser.add_argument('--smile_path',
	                    default='./pic/smile.png',
	                    type=str,
	                    help='smile image path for test')
	args = parser.parse_args()
	run(args)
