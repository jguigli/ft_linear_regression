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

def min_max_scaling(data):
    min_vals = np.min(data)
    max_vals = np.max(data)
    scaled_data = (data - min_vals) / (max_vals - min_vals)
    return scaled_data

def adjust_coefficients(theta0_normalized, theta1_normalized, price, mileage):
    theta0 = theta0_normalized * np.max(price)
    theta1 = theta1_normalized * (np.max(price) / np.max(mileage))
    return theta0, theta1

def estimate_price(theta0, theta1, mileage):
    return theta0 + theta1 * mileage

def gradient_descent(mileage: np.ndarray, price: np.ndarray):
    
    m = float(len(mileage))
    theta0, theta1 = 0, 0
    learning_rate = 0.1

    for i in range(1000):
        predicted_price = estimate_price(theta0, theta1, mileage)
        # print(f"predicted price : {predicted_price}")
        # print(f"price : {price}")
        diff_price = predicted_price - price
        # print(f"diff price : {diff_price}")
        d_theta0 = (1 / m) * np.sum(diff_price)
        d_theta1 = (1 / m) * np.sum(diff_price * mileage)

        # print(f"tmptheta0 : {d_theta0}")
        # print(f"tmptheta1 : {d_theta1}")

        theta0 -= learning_rate * d_theta0
        theta1 -= learning_rate * d_theta1
        # print(f"theta0 : {theta0}")
        # print(f"theta1 : {theta1}")


    # MSE pour Mean Square Error (erreur quadratique moyenne)
    mse = np.sum((predicted_price - price)**2)
    # RMSE pour Root Mean Square Error (racine carrée de l'erreur quadratique moyenne)
    # m est le nombre d'échantillons d'apprentissage
    rmse = np.sqrt(mse/m)

    # ssr = sum of square of residuals (somme des carrés des résidus)
    ssr = np.sum((predicted_price - price)**2)
    #  sst = total sum of squares (somme totale des carrés)
    sst = np.sum((price - np.mean(price))**2)
    # Score R2
    r2_score = 1 - (ssr/sst)

    return theta0, theta1


def training_model():

    try:
        data = load("data.csv")

        data_mileage = data['km'].astype('int')
        data_price = data['price'].astype('int')
        # data_price = 2 * np.random.rand(24, 1)
        # data_mileage = 4 - 3 * data_price + np.random.randn(24, 1)


        print(data_mileage)
        print(data_price)
        print()

        mileage = np.array(data_mileage)
        price = np.array(data_price)


        mileage_normalized = min_max_scaling(mileage)
        price_normalized = min_max_scaling(price)

        # mileage_normalized = mileage_normalized.reshape((mileage_normalized.shape[0], 1))
        # price_normalized = price_normalized.reshape((price_normalized.shape[0], 1))

        # mileage = mileage_normalized
        # price = price_normalized

        # print(mileage)
        # print(price)

        # print(mileage_normalized)
        # print(price_normalized)

        theta0, theta1 = gradient_descent(mileage_normalized, price_normalized)
        print(f"Y = {theta1}X + {theta0}")
        theta0, theta1 = adjust_coefficients(theta0, theta1, price, mileage)

        # print(f"theta0 : {theta0}")
        # print(f"theta1 : {theta1}")
        print()
        print(f"Y = {theta1}X + {theta0}")
        # print(f"Predicted : {predicted_price}")

        predicted_price = estimate_price(theta0, theta1, mileage)

        plt.scatter(mileage, price)
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