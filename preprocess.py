import os
import cv2
import json, tqdm
from collections import defaultdict
import matplotlib.pyplot as plt


def init_instance_dict(json_file):
    res_dict = defaultdict(list)
    for anno_item in tqdm.tqdm(json_file['annotations'], total=len(json_file['annotations'])):
        img_id = anno_item['image_id']
        res_dict[img_id].append(anno_item)
    return res_dict


class DataLoader(object):
    def __init__(self, json_path='/data/shuai_li/InstanceSegmentation/data/devkit/train_set.json',
                 img_dir='/data/shuai_li/InstanceSegmentation/data/train-image/image'):
        self.json_file = json.load(open(json_path, 'r', encoding='utf-8'))
        self.img_dir = img_dir
        self.instance_dict = init_instance_dict(self.json_file)
        self.category_dict = {i['id']: i for i in self.json_file['categories']}
        self.all_img_paths = {i['id']: os.path.join(self.img_dir,i['file_name']+'.jpg')
                              for i in self.json_file['images']}

    def mask(self,):

    def visualization(self):
        for img_id in tqdm.tqdm(self.all_img_paths.keys(),total=len(self.all_img_paths.keys())):
            img_path = self.all_img_paths[img_id]
            img = cv2.imread(img_path)
            plt.imshow(img[:,:,::-1])
            plt.show()
            print(self.instance_dict[img_id])
            print('*'*100)


if __name__ == '__main__':
    app = DataLoader()
    app.visualization()

