from training_model import load, estimate_price
import matplotlib.pyplot as plt
import numpy as np

def algorithm_accuracy():
    try:
        data = load("../data/data.csv")
        data_mileage = data['km'].astype('int')
        data_price = data['price'].astype('int')
        mileage = np.array(data_mileage)
        price = np.array(data_price)

        thetas = load("../data/thetas.csv")
        theta0 = float(thetas['theta0'].iloc[0])
        theta1 = float(thetas['theta1'].iloc[0])
        
        m = float(len(mileage))
        predicted_price = estimate_price(theta0, theta1, mileage)

        print("Precision of the algorithm :")

        mean_square_error = (1 / m) * np.sum((predicted_price - price) ** 2)
        root_mean_square_error = np.sqrt(mean_square_error / m)
        sum_square_residuals = np.sum((predicted_price - price) ** 2)
        total_sum_squares = np.sum((price - np.mean(price)) ** 2)
        r2_score = 1 - (sum_square_residuals / total_sum_squares)

        print(f"- Mean Square Error : {mean_square_error:.2f}")
        print(f"- Root Mean Square Error : {root_mean_square_error:.2f}")
        print(f"- R2 Score : {round(100 * r2_score)}%\n")
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return

def main():
    algorithm_accuracy()

if __name__ == "__main__":
    main()