import math
import random
from itertools import product

# -------------------------
# Modelo Tiger (pequeño POMDP)
# -------------------------
states = ['TigerLeft', 'TigerRight']       # S
actions = ['OpenLeft', 'OpenRight', 'Listen']  # A
observations = ['HearLeft', 'HearRight']  # O

# Transiciones T(s'|s,a)
# - Listen no cambia estado
# - Open resets: after opening, tiger randomly placed again
def T(s_next, s, a):
    if a == 'Listen':
        return 1.0 if s_next == s else 0.0
    else:  # OpenLeft/OpenRight -> reset uniformly
        return 0.5

# Observaciones Z(o | s', a). Observation depends on true state (s') and is noisy.
# Sensor correct with prob 0.85 (example)
def Z(o, s_prime, a):
    if o == 'HearLeft':
        return 0.85 if s_prime == 'TigerLeft' else 0.15
    else:
        return 0.85 if s_prime == 'TigerRight' else 0.15

# Recompensas R(s,a,s')
# Open correct: +10, Open wrong: -100, Listen: -1 cost
def R(s, a, s_next):
    if a == 'Listen':
        return -1
    if a == 'OpenLeft':
        return 10 if s == 'TigerLeft' else -100
    if a == 'OpenRight':
        return 10 if s == 'TigerRight' else -100
    return 0

gamma = 0.95

# -------------------------
# Value Iteration on underlying MDP (full-state)
# We compute Q(s,a) via Bellman optimality (MDP view)
# -------------------------
def value_iteration_mdp(states, actions, T_func, R_func, gamma=0.95, theta=1e-6):
    V = {s: 0.0 for s in states}
    while True:
        delta = 0.0
        for s in states:
            q_vals = []
            for a in actions:
                q = 0.0
                for s_next in states:
                    p = T_func(s_next, s, a)
                    r = R_func(s, a, s_next)
                    q += p * (r + gamma * V[s_next])
                q_vals.append(q)
            v_new = max(q_vals)
            delta = max(delta, abs(V[s] - v_new))
            V[s] = v_new
        if delta < theta:
            break
    # compute Q(s,a)
    Q = {}
    for s in states:
        for a in actions:
            q = 0.0
            for s_next in states:
                p = T_func(s_next, s, a)
                r = R_func(s, a, s_next)
                q += p * (r + gamma * V[s_next])
            Q[(s,a)] = q
    return V, Q

# -------------------------
# Creencia (belief) y actualización Bayesiana
# -------------------------
def belief_update(belief, a, o, T_func, Z_func):
    new_b = {s: 0.0 for s in states}
    for s_prime in states:
        # prediction: sum_s T(s'|s,a) b(s)
        pred = sum(T_func(s_prime, s, a) * belief[s] for s in states)
        new_b[s_prime] = Z_func(o, s_prime, a) * pred
    # normalize
    total = sum(new_b.values())
    if total == 0:
        # num stable: if impossible observation, return prior prediction normalized
        for s_prime in states:
            new_b[s_prime] = sum(T_func(s_prime, s, a) * belief[s] for s in states)
        total = sum(new_b.values())
    for s in new_b:
        new_b[s] /= total
    return new_b

# -------------------------
# Política QMDP: elegir acción que maximice sum_s b(s) Q(s,a)
# -------------------------
def qmdp_action(belief, Q, actions):
    best_a = None
    best_val = -math.inf
    for a in actions:
        val = sum(belief[s] * Q[(s,a)] for s in states)
        if val > best_val:
            best_val = val
            best_a = a
    return best_a

# -------------------------
# Simulador del POMDP
# -------------------------
def sample_next_state(s, a, T_func):
    r = random.random()
    cum = 0.0
    for s_next in states:
        cum += T_func(s_next, s, a)
        if r <= cum:
            return s_next
    return states[-1]

def sample_observation(s_next, a, Z_func):
    r = random.random()
    cum = 0.0
    for o in observations:
        cum += Z_func(o, s_next, a)
        if r <= cum:
            return o
    return observations[-1]

def simulate_episode(policy_fn, max_steps=20, render=True):
    # initial state random
    s = random.choice(states)
    # initial belief uniform
    belief = {s0: 1.0/len(states) for s0 in states}
    total_reward = 0.0
    for t in range(max_steps):
        a = policy_fn(belief)
        s_next = sample_next_state(s, a, T)
        r = R(s, a, s_next)
        o = sample_observation(s_next, a, Z)
        # update belief
        belief = belief_update(belief, a, o, T, Z)
        s = s_next
        total_reward += (gamma**t) * r
        if render:
            print(f"t={t}: estado={s}, accion={a}, obs={o}, recompensa={r}, belief={belief}")
    return total_reward

# -------------------------
# Ejecutar: calcular QMDP y simular
# -------------------------
if __name__ == "__main__":
    V_mdp, Q_mdp = value_iteration_mdp(states, actions, T, R, gamma=gamma)
    print("V(s) from underlying MDP:", V_mdp)
    print("Q(s,a) from underlying MDP:")
    for (s,a), q in Q_mdp.items():
        print(f"  Q({s},{a}) = {q:.3f}")

    def policy_from_belief(belief):
        return qmdp_action(belief, Q_mdp, actions)

    print("\nSimulación de 3 episodios usando política QMDP:")
    for ep in range(3):
        print(f"\n--- Episodio {ep+1} ---")
        total = simulate_episode(policy_from_belief, max_steps=10, render=True)
        print("Recompensa descontada total:", total)