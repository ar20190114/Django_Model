import tensorflow as tf
# from works.utils import load_random_imgs, show_test_samples
from tensorflow.python.keras.models import load_model
# from ..PhotoApp import BASE_DIR
import numpy as np
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, CSVLogger
import os
import json
import pickle
from datetime import datetime
import math


#①既存モデルの改良
# `include_top=False`として既存モデルの出力層を消す。
vgg16 = VGG16(include_top=False, input_shape=(224, 224, 3))
# モデルを編集する。
model = Sequential(vgg16.layers)
    # 全19層のうち15層目までは再学習しないようにパラメータを固定する。
for layer in model.layers[:15]:
    layer.trainable = False
    # 出力層の部分を追加
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.load_weights('../h5/ep_05_ls_-8.4.h5')


def Dogorcat(Img):
    # 評価の実施
    img_data = tf.keras.preprocessing.image.load_img(Img, target_size=(224, 224))
    x_test = np.array([tf.keras.preprocessing.image.img_to_array(img_data)])
    true_labels = ["None"]
    x_test_preproc = tf.keras.applications.vgg16.preprocess_input(x_test.copy())/255.
    probs = model.predict(x_test_preproc)

    # 学習画像を取り込むジェネレータを作成。それぞれのパラメータを設定
    img_gen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1/255.,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        preprocessing_function=tf.keras.applications.vgg16.preprocess_input
    )

    return probs[0][0], (100 - probs[0][0])

# print(Dogorcat('../media/00000900_026.jpg'))