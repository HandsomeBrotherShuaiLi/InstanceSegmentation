import os


def download_files():
    train_img = 'http://tianchi-public-us-east-download.oss-us-east-1.aliyuncs.com/231787/train-image.zip'
    train_model = 'http://tianchi-public-us-east-download.oss-us-east-1.aliyuncs.com/231787/train-model.zip'
    train_texture = 'http://tianchi-public-us-east-download.oss-us-east-1.aliyuncs.com/231787/train-texture.zip'
    devkit = 'http://tianchi-public-us-east-download.oss-us-east-1.aliyuncs.com/231787/devkit.zip'
    valdata = 'http://tianchi-public-us-east-download.oss-us-east-1.aliyuncs.com/231787/val.zip'
    os.system('wget -P data {}'.format(devkit))
    os.system('wget -P data {}'.format(valdata))
    os.system('wget -P data {}'.format(train_texture))
    os.system('wget -P data {}'.format(train_model))
    os.system('wget -P data {}'.format(train_img))


if __name__ == '__main__':
    download_files()
