from PIL import Image
import os

# 이미지가 있는 폴더 경로를 지정합니다.
image_folder = "이미지_폴더_경로"

def convert_png_to_jpg(folder_path):
    # 폴더 내의 모든 파일과 서브폴더를 순회합니다.
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 파일의 확장자를 확인하여 이미지 파일인지 확인합니다.
            if file.lower().endswith(".png"):
                # 이미지 파일인 경우, 파일의 절대 경로를 구합니다.
                image_path = os.path.join(root, file)

                # 이미지를 엽니다.
                image = Image.open(image_path)

                # JPG로 변환하여 저장합니다. 원본 파일 이름 그대로 저장합니다.
                jpg_path = os.path.splitext(image_path)[0] + ".jpg"
                image.convert("RGB").save(jpg_path)

# 함수를 실행하여 PNG 이미지들을 JPG로 변환하여 저장합니다.
convert_png_to_jpg(image_folder)
