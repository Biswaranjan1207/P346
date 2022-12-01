import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

##################################DIRECT MONTE CARLO ESTIMATION################################################
def monte_carlo_proba(sim, samples, condition=True, pt=False):
    if condition:
        print(sim," Monte Carlo Simulations of size", samples)
    samples = int(samples)
    sim = int(sim)
    
    prob = []
    for i in range(sim):
        mu_1, sigma_1 = 0, 0.01
        mu_2, sigma_2 = 0, 0.03
        #creating an array containing random variables of a Gaussian distribution
        L = np.random.normal(mu_1, sigma_1, samples)
        V = np.random.normal(mu_2, sigma_2, samples)
        #defining the integrand(current here)
        I = (50 * (0.6 - V)**2)/(0.1 + L)
        #checking for the conditions
        true_condition = np.where(I >= 275)#returns the indices of the array where the condition is true
        num_true = true_condition[0].shape[0]
        proba = num_true / samples#probability of the true condition
        prob.append(proba)
    mean_proba = np.mean(prob)#calculating mean probability
    std_proba = np.std(prob)#calculating standard deviation in mean probability
    
    if condition:
        print("Probability Mean:",round(mean_proba,5))
        print("Probability Standard deviation:",round(std_proba,5))
    return prob

prob = monte_carlo_proba(10, 10000, pt=False)

samples = [10**3, 10**4, 10**5, 10**6]
rep = 25

total_prob = []
for i, num_sample in enumerate(samples):
    prob = monte_carlo_proba(rep, num_sample, condition=False)
    total_prob.append(prob)
#converting to array
y_axis = np.asarray(total_prob)
x_axis = np.asarray(samples)
#ploting for visulaizing convergence
for x, y in zip(x_axis, y_axis):
    plt.scatter([x] * len(y), y, s=12)
plt.xscale('log')
plt.title("Direct Monte-Carlo Estimation")
plt.ylabel("Probability Estimate")
plt.xlabel('Number of Samples')
plt.grid(True)
plt.show()

##########################################IMPORTANCE SAMPLING#################################################
def importance_sampling(sim, samples, condition=True, pt=False):
    if condition:
        print("\n",sim,"Importance Sampling Simulations of size", samples)
    sim = int(sim)
    samples = int(samples)
    
    prob = []
    for i in range(sim):
        #initializing some values for given functions
        mu_1, sigma_1 = 0, 0.01
        mu_2, sigma_2 = 0, 0.03
        #initializing values for a proposal distribution
        mu_1_n, sigma_1_n = 0, 0.02
        mu_2_n, sigma_2_n = 0, 0.06
        #creating an array containing random variables of a Gaussian distribution
        L = np.random.normal(mu_1_n, sigma_1_n, samples)
        V = np.random.normal(mu_2_n, sigma_2_n, samples)
        # setup pdfs as normalized random variables for the two normal (Gaussian) distributions
        old_pdf_1 = norm(mu_1, sigma_1)
        new_pdf_1 = norm(mu_1_n, sigma_1_n)
        old_pdf_2 = norm(mu_2, sigma_2)
        new_pdf_2 = norm(mu_2_n, sigma_2_n)
        
        # calculate current
        I = (50 * (0.6 - V)**2)/(0.1 + L)
        
        #defining true condition
        true_condition = np.where(I >= 275)

        # calculate weight functions
        num = old_pdf_1.pdf(L) * old_pdf_2.pdf(V)
        denum = new_pdf_1.pdf(L) * new_pdf_2.pdf(V)
        weights = num / denum #w(x)=p(x)/q(x)

        # select weights for nonzero true condition
        weights = weights[true_condition]

        # compute unbiased proba
        proba = np.sum(weights) / samples
        prob.append(proba)
    #calculate required results
    mean_proba = np.mean(prob)
    std_proba = np.std(prob)
    if condition:
        print("Probability Mean:",round(mean_proba,5))
        print("Probability Standard deviation:",round(std_proba,5))
    return prob
prob = importance_sampling(10, 10000, pt=False)

samples = [10**3, 10**4, 10**5, 10**6]
rep = 25

total_prob = []
for i, num_sample in enumerate(samples):
    prob = importance_sampling(rep, num_sample, condition=False)
    total_prob.append(prob)
#saving as array to plot
y_axis = np.asarray(total_prob)
x_axis = np.asarray(samples)
#ploting the convergence of the results
for x, y in zip(x_axis, y_axis):
    plt.scatter([x] * len(y), y, s=12)
plt.xscale('log')
plt.title("Importance Sampling")
plt.ylabel("Probability Estimate")
plt.xlabel('Number of Samples')
plt.grid(True)
plt.show()

##COMMENTS
##Used NumPy for random variables as I needed random variables from a distribution with given mean and variance...
##I am getting different mean probabilities when I run it multiple times as it is a sampling method...
##This should be because of the use of different random variables for different iterations that are produced by the function...
##However the mean probability outputs are enclosed in a range for all the iterations(when run multiple times) and are equal upto precision 10**-3...
##The standard deviation for IS is much less than that of MC...