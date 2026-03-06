import numpy as np
from sklearn.ensemble import IsolationForest

# Normal vitals dataset
normal_data = np.array([
    [72, 98, 36.8, 120, 80, 16],
    [75, 97, 36.7, 118, 78, 15],
    [80, 99, 37.0, 122, 82, 17],
    [70, 98, 36.6, 115, 75, 16],
    [78, 97, 36.9, 121, 79, 18],
])

model = IsolationForest(contamination=0.15)
model.fit(normal_data)


def detect_anomaly(vitals):

    data = np.array([vitals])

    prediction = model.predict(data)
    score = model.decision_function(data)[0]

    if prediction[0] == -1:
        return "HIGH RISK", score
    else:
        return "NORMAL", score