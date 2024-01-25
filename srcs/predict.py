from training_model import training_model, estimate_price, load

def predict_price():
    try:
        thetas = load("../data/thetas.csv")
        theta0 = float(thetas['theta0'].iloc[0])
        theta1 = float(thetas['theta1'].iloc[0])
        
    except Exception as e:
        print(f"Error handling: {str(e)}")
        print(f"Missing thetas.csv file, value set to 0.")
        theta0 = 0
        theta1 = 0
        
    mileage = input("Enter a mileage to predict the price of a car: ")
    try:
        mileage = int(mileage)
        price = estimate_price(theta0, theta1, mileage)
        print(f"- Price predicted : {int(price)}\n")
    except ValueError:
        print("Incorrect value for mileage. Please enter a valid integer.")

def main():
    predict_price()

if __name__ == "__main__":
    main()