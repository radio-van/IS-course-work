import pandas as pd
from tensorflow.keras import models


"""
A demonstration program of multi-agent system.
This part is an agent that uses prepared model to estimate
failure type of provided data.

In real world this could be a program running on separated machine for a better
performance.
"""


MODEL_NAME = 'NN.h5'


def estimate_failure(data: pd.DataFrame) -> int:
    # load pretrained model
    model = models.load_model(MODEL_NAME)

    # make a prediction of new data
    prediction = model.predict(data)

    # return an index of max activated neuron - this is a predicted value
    return prediction.argmax()
