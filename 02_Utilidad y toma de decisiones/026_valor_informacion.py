# Modelo (mismos números que arriba)
P_disease = {True: 0.1, False: 0.9}
P_test_given_d = {
    True:  {'Pos': 0.9, 'Neg': 0.1},
    False: {'Pos': 0.2, 'Neg': 0.8}
}
U = {
    ('Treat', True):   80,
    ('Treat', False): -10,
    ('NoTreat', True): -200,
    ('NoTreat', False): 0
}

disease_vals = [True, False]
test_vals = ['Pos', 'Neg']
action_vals = ['Treat', 'NoTreat']

def joint_prob_d_and_test(d, t):
    return P_disease[d] * P_test_given_d[d][t]

def marginal_prob_test(t):
    return sum(joint_prob_d_and_test(d, t) for d in disease_vals)

def posterior_d_given_test(d, t):
    p_joint = joint_prob_d_and_test(d, t)
    p_t = marginal_prob_test(t)
    return p_joint / p_t if p_t > 0 else 0.0

# EU without info: pick best action given prior
def eu_action_without_info(action):
    return sum(P_disease[d] * U[(action, d)] for d in disease_vals)

EU_Treat = eu_action_without_info('Treat')
EU_NoTreat = eu_action_without_info('NoTreat')
EU_no_info = max(EU_Treat, EU_NoTreat)
best_action_no_info = 'Treat' if EU_Treat >= EU_NoTreat else 'NoTreat'

# EU with perfect information
EU_perfect = sum(P_disease[d] * max(U[('Treat', d)], U[('NoTreat', d)]) for d in disease_vals)

# EU with sample (test) — compute optimal policy conditioned on test results
def expected_utility_policy(policy):
    eu = 0.0
    for t in test_vals:
        p_t = marginal_prob_test(t)
        if p_t == 0:
            continue
        action = policy[t]
        eu_cond = sum(posterior_d_given_test(d, t) * U[(action, d)] for d in disease_vals)
        eu += p_t * eu_cond
    return eu

# enumerate deterministic policies mapping test->action
from itertools import product
best_policy = None
best_eu_with_test = -float('inf')
for actions in product(action_vals, repeat=len(test_vals)):
    policy = dict(zip(test_vals, actions))
    eu = expected_utility_policy(policy)
    if eu > best_eu_with_test:
        best_eu_with_test = eu
        best_policy = policy

EU_with_test = best_eu_with_test
EVPI = EU_perfect - EU_no_info
EVSI = EU_with_test - EU_no_info

print("Mejor acción sin info:", best_action_no_info, "EU_no_info =", EU_no_info)
print("EU with perfect info =", EU_perfect, "-> EVPI =", EVPI)
print("Mejor política con test:", best_policy, "EU_with_test =", EU_with_test, "-> EVSI =", EVSI)
