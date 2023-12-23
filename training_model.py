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

def normalize_data(mileage, price):
    mileage_mean, mileage_std = np.mean(mileage), np.std(mileage)
    price_mean, price_std = np.mean(price), np.std(price)

    mileage = (mileage - mileage_mean) / mileage_std
    price = (price - price_mean) / price_std
    return mileage, price

def reajust_coefficient(theta0, theta1, mileage, price):
    theta0 = np.mean(price) - theta1 * np.mean(mileage) * np.std(price) / np.std(mileage)
    theta1 = theta1 * np.std(price) / np.std(mileage)
    return theta0, theta1

def estimate_price(theta0, theta1, mileage):
    return theta0 + theta1 * mileage


def linear_regression(mileage: np.ndarray, price: np.ndarray):
    
    m = len(mileage)
    theta0, theta1 = 0, 0
    learning_rate = 0.01

    for i in range(1000):
        predicted_price = estimate_price(theta0, theta1, mileage)
        # print(f"predicted price : {predicted_price}")
        # print(f"price : {price}")
        diff_price = predicted_price - price
        # print(f"diff price : {diff_price}")
        d_theta0 = (1 / m) * np.sum(diff_price)
        d_theta1 = (1 / m) * np.sum((diff_price) * mileage)

        # print(f"tmptheta0 : {d_theta0}")
        # print(f"tmptheta1 : {d_theta1}")

        theta0 -= learning_rate * d_theta0
        theta1 -= learning_rate * d_theta1
        # print(f"theta0 : {theta0}")
        # print(f"theta1 : {theta1}")

    return theta0, theta1


def training_model():

    try:
        data = load("data.csv")

        data_mileage = data['km'].astype('int')
        data_price = data['price'].astype('int')
        # data_price = 2 * np.random.rand(24, 1)
        # data_mileage = 4 - 3 * data_price + np.random.randn(24, 1)

        # data_mileage = np.array([[2400], [1398], [1505], [1855], [1760], [1148], [1668], [890], [1445], [840],
        #               [820], [630], [740], [975], [670], [760], [482], [930], [609], [656],
        #               [540], [685], [228], [617]])
        # data_price = np.array([[36], [38], [44], [44], [52], [53], [58], [59], [59], [62],
        #               [63], [63], [66], [68], [68], [69], [69], [69], [74], [75],
        #               [79], [79], [79], [82]])

        print(data_mileage)
        print(data_price)
        print()

        mileage = np.array(data_mileage)
        price = np.array(data_price)


        mileage_normalized, price_normalized = normalize_data(mileage, price)

        mileage_normalized = mileage_normalized.reshape((mileage_normalized.shape[0], 1))
        price_normalized = price_normalized.reshape((price_normalized.shape[0], 1))

        mileage = mileage_normalized
        price = price_normalized


        print(mileage)
        print(price)


        # print(mileage_normalized)
        # print(price_normalized)

        theta0, theta1 = linear_regression(mileage, price)
        print(f"Y = {theta1}X + {theta0}")
        theta0, theta1 = reajust_coefficient(theta0, theta1, mileage, price)
        predicted_price = estimate_price(theta0, theta1, mileage)

        # print(f"theta0 : {theta0}")
        # print(f"theta1 : {theta1}")
        print()
        print(f"Y = {theta1}X + {theta0}")
        # print(f"Predicted : {predicted_price}")


        plt.scatter(data_mileage, data_price)
        if theta1 < 0:
            plt.plot([min(mileage), max(mileage)], [max(predicted_price), min(predicted_price)], color='red')
        else:
            plt.plot([min(mileage), max(mileage)], [min(predicted_price), max(predicted_price)], color='red')
        plt.title('Linear regression')
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return



def main():
    training_model()



if __name__ == "__main__":
    main()