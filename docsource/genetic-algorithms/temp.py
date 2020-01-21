import os
import compas
from compas.numerical.solvers.ga import ga

def foo(X):
    fit = sum(X)
    return fit

fit_function = foo
fit_type = 'min'
num_var = 10
boundaries = [(0, 1)] * num_var
num_bin_dig  = [8] * num_var
output_path = os.path.join(compas.TEMP, 'ga_out/')

if not os.path.exists(output_path):
    os.makedirs(output_path)

ga = ga(fit_function,
        fit_type,
        num_var,
        boundaries,
        num_gen=100,
        num_pop=100,
        num_elite=40,
        num_bin_dig=num_bin_dig,
        output_path=output_path,
        min_fit=0.01)
