from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


def predict_pic(pic):
    np.set_printoptions(suppress=True)

    model = load_model('utils/models/keras_model.h5', compile=False)
    class_names = open('utils/models/labels.txt', 'r', encoding='utf-8').readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(pic).convert('RGB')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_list = class_names[index].strip().split(" ")
    class_id = class_list[0]
    class_name = class_list[1]
    confidence_score = prediction[0][index]

    return int(class_id)+1, class_name, confidence_score