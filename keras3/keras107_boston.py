# trial, epochs 상관 없이 훈련
# trial >= 2 주는 것이 좋음
import numpy as np
import tensorflow as tf
import autokeras as ak
import datetime

from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.models import load_model

str_time = datetime.datetime.now()

epoch = 5
trials = 500

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

model = ak.StructuredDataRegressor(
    max_trials=trials,
    overwrite=True
)

model.fit(
    x_train, y_train,
    epochs = epoch,
)

results = model.evaluate(x_test, y_test)

print('max_trials : {}'.format(trials))
print('epochs : {}'.format(epoch))
print('results : ', results)
print('time : ', datetime.datetime.now() - str_time)

model2 = model.export_model()
try:
    model2.save('c:/data/h5/ak_boston', save_format = tf)
except:
    model2.save('c:/data/h5/ak_boston_err')

models3 = load_model(
    'c:/data/h5/ak_boston'
)

results2 = models3.evaluate(x_test, y_test)

print('models3 : ', results2)

# max_trials : 2
# epochs : 10
# results :  [68.83074188232422, 68.83074188232422]

# max_trials : 5
# epochs : 500
# results :  [12.814866065979004, 12.814866065979004]

# max_trials : 5
# epochs : 1000
# results :  [19.15825653076172, 19.15825653076172]
# time :  0:02:45.477785