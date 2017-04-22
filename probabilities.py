from numpy.random import  beta as beta_dist
import numpy as np
N_samp = 100000
clicks_A = 43
views_A = 364
clicks_B = 52
views_B = 323
alpha = 1.0
beta = 1.0
A_samples = beta_dist(clicks_A+alpha, views_A-clicks_A+beta, N_samp)
B_samples = beta_dist(clicks_B+alpha, views_B-clicks_B+beta, N_samp)
print np.mean(A_samples > B_samples)
0.05307
# P(A\B) = P(B\A)*P(A)\(P(B))
