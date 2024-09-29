import cv2
import os
import csv

input_folder = '/Users/gushuai/Desktop/bigdata/opencv/pic'
output_folder = '/Users/gushuai/Desktop/bigdata/opencv'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

file_path = os.path.join(output_folder, 'features.csv')
with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    image_path = os.path.join(input_folder, os.listdir(input_folder)[0])
    '''
    使用orb算法进行特征提取。
    orb算法使用fast方法来提取特征点，再用brief表示提取到的关键点。
    方向方面，通过计算关键点周围区域的灰度梯度，ORB确定关键点的主方向，并将关键点旋转到该方向。
    匹配时，ORB采用一种快速匹配策略，即使用近似最近邻（ANN）算法来加速匹配过程。
    '''
    orb=cv2.ORB_create()
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_COLOR)


            keypoints, descriptors = orb.detectAndCompute(image, None)

            # 将ORB特征转换为一维数组
            feature_vector = descriptors.flatten()
            row = [filename] + feature_vector.tolist()
            csv_writer.writerow(row)


