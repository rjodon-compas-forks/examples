import os
import compas
from compas_plotters.gaplotter import visualize_evolution
from math import cos
from math import pi

def rastrigin(X):
    a = 10
    fit = a * 2 + sum([(x ** 2 - a * cos(2 * pi * x)) for x in X])
    return fit

def foo(X):
    fit = sum(X)
    # print ('fit', fit, X)
    return fit

fit_function = rastrigin
# fit_function = foo
fit_type = 'min'
num_var = 2
boundaries = [(-5.12, 5.12)] * num_var
# boundaries = [(1, 5)] * num_var

num_bin_dig = [40] * num_var
output_path = os.path.join(compas.TEMP, 'ga_out/')
min_fit = 0.000001  # num_var * boundaries[0][0]

if not os.path.exists(output_path):
    os.makedirs(output_path)

ga_ = ga(fit_function,
            fit_type,
            num_var,
            boundaries,
            num_gen=100,
            num_pop=100,
            num_elite=20,
            num_bin_dig=num_bin_dig,
            output_path=output_path,
            min_fit=min_fit,
            mutation_probability=0.03,
            n_cross=2)

visualize_evolution(ga_.output_path)
