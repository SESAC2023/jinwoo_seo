from PIL import Image
import os

# 이미지가 있는 폴더 경로를 지정합니다. / ~~unicode 뜨면 \ 말고 /로 변경해야한다.
image_folder = "파일경로" 

# 이미지 사이즈를 지정합니다.
target_size = 1250

def resize_images(folder_path, target_size):
    # 폴더 내의 모든 파일과 서브폴더를 순회합니다.
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 파일의 확장자를 확인하여 이미지 파일인지 확인합니다.
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
                # 이미지 파일인 경우, 파일의 절대 경로를 구합니다.
                image_path = os.path.join(root, file)

                # 이미지를 엽니다.
                image = Image.open(image_path)

                # 이미지의 너비와 높이를 구합니다.
                width, height = image.size

                # 이미지가 이미 지정된 사이즈를 초과하는 경우에만 resize를 수행합니다.
                if width > target_size or height > target_size:
                    # 너비와 높이를 1450으로 조정합니다.
                    if width > height:
                        new_width = target_size
                        new_height = int(target_size * height / width)
                    else:
                        new_height = target_size
                        new_width = int(target_size * width / height)

                    # 이미지를 resize 합니다.
                    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

                    # 원본 파일 이름으로 저장합니다.
                    resized_image.save(image_path)

# 함수를 실행하여 이미지들을 resize합니다.
resize_images(image_folder, target_size)
