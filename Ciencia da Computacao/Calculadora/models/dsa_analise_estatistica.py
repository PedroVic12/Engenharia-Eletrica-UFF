class StatisticsCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        # população e amostra
        # distribuição normal
        #medidas de tendencias central
        # valor-p
        # variaça e desvio padrao
        # covariancia e correlação
        # teorema do limite central
        # valor esperado de variaveis aleatorias
        # probabilidade condicional
        # teoream de bayes

    def mean(self):
        mean_x = sum(self.x) / len(self.x)
        mean_y = sum(self.y) / len(self.y)
        return mean_x, mean_y

    def variance(self):
        mean_x, mean_y = self.mean()

        var_x = sum([(xi - mean_x)**2 for xi in self.x]) / len(self.x)
        var_y = sum([(yi - mean_y)**2 for yi in self.y]) / len(self.y)

        return var_x, var_y

    def standard_deviation(self):
        var_x, var_y = self.variance()
        std_dev_x = var_x**0.5
        std_dev_y = var_y**0.5
        return std_dev_x, std_dev_y

    def covariance(self):
        mean_x, mean_y = self.mean()

        covariance_xy = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(self.x, self.y)]) / len(self.x)

        return covariance_xy

    def correlation_coefficient(self):
        covariance_xy = self.covariance()
        std_dev_x, std_dev_y = self.standard_deviation()

        correlation_coeff = covariance_xy / (std_dev_x * std_dev_y) if std_dev_x * std_dev_y != 0 else 0

        return correlation_coeff

    def linear_regression_line(self):
        mean_x, mean_y = self.mean()
        covariance_xy = self.covariance()
        std_dev_x = self.standard_deviation()[0]

        slope = covariance_xy / (std_dev_x**2) if std_dev_x != 0 else 0
        intercept = mean_y - slope * mean_x

        return slope, intercept

    def predict_y_values(self, x_values, slope, intercept):
        predicted_y = [slope * xi + intercept for xi in x_values]
        return predicted_y

    def residual_sum_of_squares(self, y_actual, y_predicted):
        rss = sum([(yi - yp)**2 for yi, yp in zip(y_actual, y_predicted)])
        return rss

    def coefficient_of_determination(self, y_actual, y_predicted):
        mean_y_squared = sum([(yi - mean_y)**2 for yi in y_actual]) / len(y_actual)
        r_squared = 1 - (self.residual_sum_of_squares(y_actual, y_predicted) / mean_y_squared)
        return r_squared

def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 3]

    calculator = StatisticsCalculator(x, y)

    # Calculate and print means
    mean_x, mean_y = calculator.mean()
    print("Mean of x:", mean_x)
    print("Mean of y:", mean_y)

    # Calculate and print variances
    var_x, var_y = calculator.variance()
    print("Variance of x:", var_x)
    print("Variance of y:", var_y)

    # Calculate and print standard deviations
    std_dev_x, std_dev_y = calculator.standard_deviation()
    print("Standard deviation of x:", std_dev_x)
    print("Standard deviation of y:", std_dev_y)

    # Calculate and print covariance
    covariance_xy = calculator.covariance()
    print("Covariance:", covariance_xy)

    # Calculate and print correlation coefficient
    correlation_coeff = calculator.correlation_coefficient()
    print("Correlation coefficient:", correlation_coeff)

    # Calculate and print linear regression line
    slope, intercept = calculator.linear_regression_line()
    print("Linear regression line equation: y =", slope, "x +", intercept)

    # Predict y values for new x values
    

