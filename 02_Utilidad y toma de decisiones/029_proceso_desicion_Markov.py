import math
import random
from copy import deepcopy
from itertools import product

class MDP:
    def __init__(self, states, actions, transitions, rewards, gamma=0.9):
        """
        states: lista/iterable de estados (hashable)
        actions: lista/iterable de acciones
        transitions: dict (s,a) -> list of (prob, s_next)
        rewards: dict (s,a,s_next) -> r  (o (s,a)->r si prefieres)
        gamma: descuento
        """
        self.states = list(states)
        self.actions = list(actions)
        self.transitions = transitions
        self.rewards = rewards
        self.gamma = gamma

    def get_transitions(self, s, a):
        return self.transitions.get((s,a), [])

    def get_reward(self, s, a, s_next):
        r_key = (s,a,s_next)
        if r_key in self.rewards:
            return self.rewards[r_key]
        r_key2 = (s,a)
        return self.rewards.get(r_key2, 0.0)

    def simulate(self, start_state, policy, max_steps=100, render=False):
        """
        Simula una trayectoria siguiendo una política determinista: policy(s) -> a
        Devuelve (trajectory, total_discounted_reward)
        """
        s = start_state
        traj = [s]
        total = 0.0
        discount = 1.0
        for t in range(max_steps):
            a = policy.get(s, None)
            if a is None:
                break
            trans = self.get_transitions(s, a)
            if not trans:
                break
            # elegir siguiente estado según distribución
            r = random.random()
            cum = 0.0
            for (p, s_next) in trans:
                cum += p
                if r <= cum:
                    break
            rew = self.get_reward(s, a, s_next)
            total += discount * rew
            discount *= self.gamma
            s = s_next
            traj.append(s)
            if render:
                print(f"t={t}: s={traj[-2]} a={a} -> s'={s} r={rew}")
        return traj, total

def value_iteration(mdp, theta=1e-6, max_iters=10000):
    V = {s: 0.0 for s in mdp.states}
    it = 0
    while True:
        delta = 0.0
        for s in mdp.states:
            q_values = []
            for a in mdp.actions:
                q = 0.0
                for (p, s_next) in mdp.get_transitions(s, a):
                    r = mdp.get_reward(s, a, s_next)
                    q += p * (r + mdp.gamma * V[s_next])
                q_values.append(q)
            v_new = max(q_values) if q_values else 0.0
            delta = max(delta, abs(V[s] - v_new))
            V[s] = v_new
        it += 1
        if delta < theta or it >= max_iters:
            break
    # extraer politica greedy determinista
    policy = {}
    for s in mdp.states:
        best_a = None
        best_q = -math.inf
        for a in mdp.actions:
            q = 0.0
            for (p, s_next) in mdp.get_transitions(s, a):
                r = mdp.get_reward(s, a, s_next)
                q += p * (r + mdp.gamma * V[s_next])
            if q > best_q:
                best_q = q
                best_a = a
        policy[s] = best_a
    return V, policy

def policy_evaluation(policy, mdp, theta=1e-6, max_iters=10000):
    V = {s: 0.0 for s in mdp.states}
    it = 0
    while True:
        delta = 0.0
        for s in mdp.states:
            a = policy.get(s, None)
            if a is None:
                v_new = 0.0
            else:
                q = 0.0
                for (p, s_next) in mdp.get_transitions(s, a):
                    r = mdp.get_reward(s, a, s_next)
                    q += p * (r + mdp.gamma * V[s_next])
                v_new = q
            delta = max(delta, abs(V[s] - v_new))
            V[s] = v_new
        it += 1
        if delta < theta or it >= max_iters:
            break
    return V

def policy_iteration(mdp, theta=1e-6, max_policy_iters=100):
    # init policy: primera acción válida por estado
    policy = {}
    for s in mdp.states:
        has_action = any(mdp.get_transitions(s,a) for a in mdp.actions)
        policy[s] = mdp.actions[0] if has_action else None

    for i in range(max_policy_iters):
        V = policy_evaluation(policy, mdp, theta=theta)
        policy_stable = True
        for s in mdp.states:
            best_a = None
            best_q = -math.inf
            any_action = False
            for a in mdp.actions:
                trans = mdp.get_transitions(s,a)
                if not trans:
                    continue
                any_action = True
                q = sum(p * (mdp.get_reward(s,a,s_next) + mdp.gamma * V[s_next]) for (p,s_next) in trans)
                if q > best_q:
                    best_q = q
                    best_a = a
            new_action = best_a if any_action else None
            if policy.get(s) != new_action:
                policy_stable = False
                policy[s] = new_action
        if policy_stable:
            break
    V_final = policy_evaluation(policy, mdp, theta=theta)
    return V_final, policy

# ---------------------------
# Ejemplo: GridWorld sencillo (3x1) con terminal a la derecha
# Estados: s0 (inicio), s1, s2 (terminal)
# Acciones: 'right', 'left'
# reward: +1 al llegar a terminal desde s1->s2, 0 en demás
# ---------------------------
if __name__ == "__main__":
    states = ['s0','s1','s2']   # s2 es terminal (sin transiciones)
    actions = ['right','left']
    transitions = {
        ('s0','right'): [(1.0,'s1')],
        ('s0','left'):  [(1.0,'s0')],
        ('s1','right'): [(1.0,'s2')],
        ('s1','left'):  [(1.0,'s0')],
        ('s2','right'): [],  # terminal: ninguna transición
        ('s2','left'):  []
    }
    rewards = {
        ('s1','right','s2'): 1.0
    }
    mdp = MDP(states, actions, transitions, rewards, gamma=0.9)

    print("=== Value Iteration ===")
    V_vi, pi_vi = value_iteration(mdp)
    for s in states:
        print(f"V[{s}] = {V_vi[s]:.4f}, pi[{s}] = {pi_vi[s]}")

    print("\n=== Policy Iteration ===")
    V_pi, pi_pi = policy_iteration(mdp)
    for s in states:
        print(f"V[{s}] = {V_pi[s]:.4f}, pi[{s}] = {pi_pi[s]}")

    # Simular una trayectoria siguiendo la política óptima (Value Iteration)
    traj, total = mdp.simulate('s0', pi_vi, max_steps=10, render=True)
    print("\nTrayectoria simulada:", traj)
    print("Recompensa descontada total aproximada:", total)