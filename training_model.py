import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load(path: str) -> pd.DataFrame:
    """Read a CSV datasheet and return a DataFrame."""
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return


def estimate_price(theta0, theta1, mileage):
    return theta0 + theta1 * mileage


def linear_regression(mileage: np.ndarray, price: np.ndarray):
    
    m = len(mileage)
    theta0, theta1 = 2, 1
    learning_rate = 0.0001

    for i in range(100):
        predicted_price = estimate_price(theta0, theta1, mileage)
        # print(predicted_price)
        d_theta0 = (1 / m) * np.sum(predicted_price - price)
        d_theta1 = (1 / m) * np.sum((predicted_price - price) * mileage)

        theta0 -= learning_rate * d_theta0
        theta1 -= learning_rate * d_theta1
        print(f"theta0 : {theta0}")
        print(f"theta1 : {theta1}")

    return theta0, theta1


def training_model():

    try:
        data = load("data.csv")

        data_mileage = data['km'].values.astype('int')
        data_price = data['price'].values.astype('int')

        mileage = np.array(data_mileage)
        price = np.array(data_price)


        theta0, theta1 = linear_regression(mileage, price)
        predicted_price = estimate_price(theta0, theta1, mileage)

        print(f"theta0 : {theta0}")
        print(f"theta1 : {theta1}")

        print(data_mileage)
        print(data_price)

        plt.scatter(data_price, data_mileage)
        plt.plot([min(price), max(price)], [min(predicted_price), max(predicted_price)], color='red')
        plt.title('Linear regression')
        plt.xlabel('Price')
        plt.ylabel('Mileage')
        plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return



def main():
    training_model()



if __name__ == "__main__":
    main()