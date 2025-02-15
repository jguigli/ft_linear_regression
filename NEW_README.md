# ft_linear_regression

## Description

`ft_linear_regression` is a Python-based project that implements linear regression using gradient descent. The project is designed to predict car prices based on mileage data. It includes functionalities for training the model, making predictions, evaluating accuracy, and visualizing the results.

## Setup

To set up the project, ensure you have Python installed on your machine. Follow these steps to get started:

**Clone the Repository:**
   ```bash
   git clone https://github.com/jguigli/ft_linear_regression.git
   cd ft_linear_regression
   ```

## Usage

The `Makefile` provides several commands to manage the project lifecycle. Below are the available commands:

### Commands

- **Train the Model:**
  ```bash
  make train
  ```
  This command trains the linear regression model using the data in `data.csv` and saves the parameters to `thetas.csv`.

- **Predict Car Price:**
  ```bash
  make predict
  ```
  This command predicts the price of a car based on user-provided mileage using the trained model.

- **Evaluate Accuracy:**
  ```bash
  make accuracy
  ```
  This command calculates and displays the accuracy metrics of the linear regression model, including Mean Square Error and R2 Score.

- **Visualize Data:**
  ```bash
  make graph
  ```
  This command plots the data and the regression line, providing a visual representation of the model's fit.

## Notes

- Ensure you have the necessary data files in the `data` directory before running the commands.
- The project uses gradient descent to optimize the linear regression model parameters.

## Useful links

[SUJET](https://cdn.intra.42.fr/pdf/pdf/117108/en.subject.pdf)  
[Regression lineaire avec Python](https://moncoachdata.com/blog/regression-lineaire-avec-python/)  
[Descente de gradient](https://www.ibm.com/fr-fr/topics/gradient-descent)  
[Regression lineaire](https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931)  
[Youtube Modele lineaire](https://www.youtube.com/watch?v=wg7-roETbbM)  
[Youtube Modele lineaire](https://www.youtube.com/watch?v=8Y3r7F47Xfo)  
[Normalization](https://www.codecademy.com/article/normalization)  
