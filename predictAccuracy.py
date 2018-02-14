from predict import predict_Class
import numpy as np
import os

classes = ["iceberg","ship"]

result1 = []
arr = os.listdir("testing_data/iceberg")
for file in arr:
	values = predict_Class("testing_data/iceberg/"+file)
	result1.append(values[0])

y_pred1 = np.argmax(result1,axis=1)
y_true1 = np.zeros(len(y_pred1))

result2 = []
arr = os.listdir("testing_data/ship")
for file in arr:
	values = predict_Class("testing_data/ship/"+file)
	result2.append(values[0])
y_pred2 = np.argmax(result2,axis=1)
y_true2 = np.ones(len(y_pred2))

y_pred = [*y_pred1,*y_pred2]
y_true = [*y_true1,*y_true2]

correct_pred = [ 1 if y_pred[i] == y_true[i] else 0 for i in range(len(y_pred))]
#print(correct_pred)
accuracy = np.mean(correct_pred)
print("Accuracy: {0:>6.1%}".format(accuracy))