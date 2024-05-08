
eval = 0;

// RZ 15mai2011 - Varre todos os elementos do vetor best_run_ever_array
for (k = 0; k < best_run_ever_array_size; k++)
{
    diff = 0;
    for (i = 0; i < num_var; i++)
    {
        // RZ 10mai2011 - Verifica se |diferença| é maior que valor mínimo
        if (fabs(best_run_ever_array[k].x[i] - candidate->x[i]) >= diff_elitism_array)
            diff++;
    }
    // RZ 10mai2011 - Se pelo menos metade das variáveis atende à diferença,
    // incrementa a avaliação do indivíduo candidato ao grupo elite
    if (diff >= num_diff_elitism_array)
    {
        eval++;
    }
}
// indivíduo diferente de todos os indivíduos do array
if (eval == best_run_ever_array_size)
{
    return FALSE;
}
