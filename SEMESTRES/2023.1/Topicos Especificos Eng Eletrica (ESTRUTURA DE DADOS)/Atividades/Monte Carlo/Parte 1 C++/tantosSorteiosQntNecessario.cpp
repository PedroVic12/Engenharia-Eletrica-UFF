#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <algorithm>
#include <numeric>

// Classe para a Simulação de Monte Carlo
class MonteCarloSimulation
{
private:
    std::vector<double> f;
    std::vector<double> D;
    double beta_threshold;
    int N;
    double sigma;
    double sigma_squared;
    std::vector<double> l_values;
    std::vector<double> s_values;
    std::vector<double> beta_values;

public:
    MonteCarloSimulation(const std::vector<double> &f, const std::vector<double> &D, double beta_threshold)
        : f(f), D(D), beta_threshold(beta_threshold), N(0), sigma(0), sigma_squared(0) {}

    void run()
    {
        double beta = std::numeric_limits<double>::infinity();

        while (beta >= beta_threshold)
        {
            N++;
            std::random_device rd;
            std::mt19937 gen(rd());
            std::discrete_distribution<int> dist(f.begin(), f.end());
            int index = dist(gen);
            double x = index + 1;
            double D_x = D[index];

            sigma += D_x;
            sigma_squared += std::pow(D_x, 2.0);

            double l = sigma / N;
            double variance = (sigma_squared / N) - std::pow(l, 2.0);
            double s = std::sqrt(variance);
            beta = (s / l) / std::sqrt(N);

            l_values.push_back(l);
            s_values.push_back(s);
            beta_values.push_back(beta);
        }
    }

    void plotResults()
    {
        std::cout << "Valor esperado (l): ";
        for (auto l : l_values)
        {
            std::cout << l << " ";
        }
        std::cout << std::endl;

        std::cout << "Desvio padrão (s): ";
        for (auto s : s_values)
        {
            std::cout << s << " ";
        }
        std::cout << std::endl;

        std::cout << "Parâmetro beta (β): ";
        for (auto beta : beta_values)
        {
            std::cout << beta << " ";
        }
        std::cout << std::endl;
    }
};

int main()
{
    // Função de distribuição de probabilidade
    std::vector<double> f = {0.3, 0.5, 0.2};

    // Função de desempenho
    std::vector<double> D = {1.0, 4.0, 9.0};

    // Tolerância beta
    double beta_threshold;
    std::cout << "Digite a tolerância beta: ";
    std::cin >> beta_threshold;

    MonteCarloSimulation simulation(f, D, beta_threshold);
    simulation.run();
    simulation.plotResults();

    return 0;
}
