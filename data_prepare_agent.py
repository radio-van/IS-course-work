import pandas as pd

from sklearn.preprocessing import MinMaxScaler


"""
A demonstration program of multi-agent system.
This an agent which prepares data from sensors to the form of model input.

In real world this could be a program running on separated machine for a better
performance.
"""


def prepare_data(data: dict = None) -> pd.DataFrame:
    for key, value in data.items():
        data[key] = [value]

    df = pd.DataFrame.from_dict(data)

    # drop useless columns
    cleaned_dataset = df.drop([
        'Type',
        '\ufeffUDI',
        'Product ID',
        'Target',
        'Failure Type',  # pretend this is unknown
    ], axis=1)

    # apply scaler
    scaler = MinMaxScaler()
    scaler.fit(cleaned_dataset)
    scaled_dataset = pd.DataFrame(
        data=scaler.transform(cleaned_dataset),
        columns=cleaned_dataset.columns,
        index=cleaned_dataset.index
    )

    # return prepared dataset
    return scaled_dataset
