import pyblp
import numpy as np
import pandas as pd

pyblp.options.digits = 4
pyblp.options.verbose = False
pyblp.__version__

#%%
product_data = pd.read_csv(pyblp.data.NEVO_PRODUCTS_LOCATION)
product_data.head()
product_data_test = product_data.drop(['city_ids', 'quarter', 'firm_ids', 'brand_ids', 'mushy'], axis=1)

#%%
X1_formulation = pyblp.Formulation('1 + prices')
X2_formulation = pyblp.Formulation('1 + prices + sugar')
product_formulations = (X1_formulation, X2_formulation)
product_formulations

#%%
mc_integration = pyblp.Integration('monte_carlo', size=50, specification_options={'seed': 0})
mc_integration

#%%
mc_problem = pyblp.Problem(product_formulations, product_data, integration=mc_integration)
mc_problem

#%%
bfgs = pyblp.Optimization('bfgs', {'gtol': 1e-4})
bfgs

#%%
agent_data = pd.read_csv(pyblp.data.NEVO_AGENTS_LOCATION)
agent_data_test = agent_data[['market_ids', 'weights', 'income', 'nodes0']]
agent_data.head()

#%%
agent_formulation = pyblp.Formulation('0 + income')
agent_formulation

#%%
nevo_problem = pyblp.Problem(
    product_formulations,
    product_data_test,
    agent_formulation,
    agent_data_test
)
nevo_problem

#%%
product_data_test.to_csv('./product_data.csv')
agent_data_test.to_csv('./agent_data.csv')

#%% Can set parts of this to 0....
initial_sigma = np.diag([0, 1.0, 0])
initial_pi = np.array([[5.4819], [5.8935], [-0.2506]])
tighter_bfgs = pyblp.Optimization('bfgs', {'gtol': 1e-5})
nevo_results = nevo_problem.solve(
    initial_sigma,
    initial_pi,
    optimization=tighter_bfgs,
    method='1s'
)
print(nevo_results)

#%% Can set parts of this to 0....
initial_sigma = np.diag([0, 1.0, 0])
initial_pi = np.array([[1.0], [-20.0], [0.1]])
tighter_bfgs = pyblp.Optimization('bfgs', {'gtol': 1e-5})
nevo_results = nevo_problem.solve(
    initial_sigma,
    initial_pi,
    optimization=tighter_bfgs,
    method='1s'
)
print(nevo_results)


#%%
elasticities = nevo_results.compute_elasticities()
single_market = product_data['market_ids'] == 'C01Q1'
elas_diag = np.diag(elasticities[single_market])

#%%
from matplotlib import pyplot as plt
plt.scatter(product_data.loc[product_data['market_ids'] == 'C01Q1', 'prices'], elas_diag)

#%%
logit_formulation = pyblp.Formulation('1 + prices + sugar')
logit_formulation

product_data_test = product_data[['market_ids', 'shares', 'prices', 'sugar', 'demand_instruments0']]

problem = pyblp.Problem(logit_formulation, product_data)
problem

logit_results = problem.solve()
print(logit_results)

#%%
elasticities = logit_results.compute_elasticities()
single_market = product_data['market_ids'] == 'C01Q1'
elas_diag = np.diag(elasticities[single_market])

#%%
from matplotlib import pyplot as plt
plt.scatter(product_data.loc[product_data['market_ids'] == 'C01Q1', 'prices'], elas_diag)
plt.show()