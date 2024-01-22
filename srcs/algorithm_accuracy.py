from training_model import load, estimate_price
import matplotlib.pyplot as plt
import numpy as np

def algorithm_accuracy():
    """DOC HERE"""
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
        # MSE pour Mean Square Error (erreur quadratique moyenne)
        mse = np.sum((predicted_price - price) ** 2)
        print(f"- Mean Square Error : {mse:.2f}")

        # RMSE pour Root Mean Square Error (racine carrée de l'erreur quadratique moyenne)
        rmse = np.sqrt(mse / m)
        print(f"- Root Mean Square Error : {rmse:.2f}")

        # Sum of square of residuals (somme des carrés des résidus)
        ssr = np.sum((predicted_price - price) ** 2)
        # Total sum of squares (somme totale des carrés)
        sst = np.sum((price - np.mean(price)) ** 2)
        # Score R2
        r2_score = 1 - (ssr / sst)
        print(f"- R2 Score : {round(100 * r2_score)}%\n")
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return

def main():
    algorithm_accuracy()

if __name__ == "__main__":
    main()