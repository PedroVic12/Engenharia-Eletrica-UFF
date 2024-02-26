def main():
    tempo1 = time.time()

    data_visual = DataExploration()
    setup = Setup()
    alg = AlgEvolution(setup)
    alg_NO_repopulation = AlgEvolution(setup)

    # Sem repopulação
    print("\n\nAlg evolutivo Sem repopulação")
    alg_NO_repopulation.setup.num_repopulation = 0
    (
        pop_without_repopulation,
        logbook_without_repopulation,
        best_without_repopulation,
    ) = alg_NO_repopulation.run()
    data_visual.visualize(
        logbook_without_repopulation, pop_without_repopulation, repopulation=False
    )
    data_visual.plot_best_fitness_generation(
        alg_NO_repopulation.getters()["best_fitness_array"], repopulation=False
    )

    # Após a execução do algoritmo sem repopulação
    best_df_without_repopulation, fitness_df_without_repopulation = (
        alg_NO_repopulation.get_population_dataframes()
    )
    best_df_without_repopulation.to_csv(
        "../assets/output/best_individuals_without_repopulation.csv", index=False
    )
    fitness_df_without_repopulation.to_csv(
        "../assets/output/fitness_without_repopulation.csv", index=False
    )

    # Com repopulação
    print("\nAlg evolutivo com repopulação")
    pop_with_repopulation, logbook_with_repopulation, best_with_repopulation = alg.run()
    data_visual.visualize(
        logbook_with_repopulation, pop_with_repopulation, repopulation=True
    )
    data_visual.plot_best_fitness_generation(
        alg.getters()["best_fitness_array"], repopulation=True
    )

    dir = "../assets/output"
    best_df_with_repopulation, fitness_df_with_repopulation = (
        alg.get_population_dataframes()
    )
    best_df_with_repopulation.to_csv(
        "../assets/output/best_individuals_with_repopulation.csv", index=False
    )
    fitness_df_with_repopulation.to_csv(
        "../assets/output/fitness_with_repopulation.csv", index=False
    )

    tempo2 = time.time()
    print(f"Total execution time: {round(tempo2-tempo1,2)} seconds")


if __name__ == "__main__":
    main()
