import tensorflow as tf
# from works.utils import load_random_imgs, show_test_samples
from tensorflow.python.keras.models import load_model
from ..PhotoApp import BASE_DIR
import numpy as np

# modelへ保存データを読み込み
model = load_model(BASE_DIR+'../h5/ep_05_ls_-8.4.h5')

def Dogorcat(Img):
    # 評価の実施
    img_data = tf.keras.preprocessing.image.load_img(Img, target_size=(224, 224))
    x_test = np.array([tf.keras.preprocessing.imageimg_to_array(img_data)])
    true_labels = ["None"]
    x_test_preproc = tf.keras.applications.vgg16.preprocess_input(x_test.copy())/255.
    probs = model.predict(x_test_preproc)

    # 学習画像を取り込むジェネレータを作成。それぞれのパラメータを設定'
    img_gen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1/255.,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        preprocessing_function=tf.keras.applications.vgg16.preprocess_input
    )

    return probs[0][0], (100 - probs[0][0])