import math
from copy import deepcopy

def policy_evaluation(policy, states, actions, transitions, rewards, gamma=0.9, theta=1e-6, max_iters=10000):
    """
    Evalúa una política determinista (policy: dict estado->accion) iterativamente.
    Devuelve V (dict estado->valor).
    """
    V = {s: 0.0 for s in states}

    def get_transitions(s, a):
        return transitions.get((s, a), [])

    def get_reward(s, a, s_next):
        # prioriza recompensa dependiente de (s,a,s_next) si existe
        r_key = (s, a, s_next)
        if r_key in rewards:
            return rewards[r_key]
        r_key2 = (s, a)
        return rewards.get(r_key2, 0.0)

    it = 0
    while it < max_iters:
        delta = 0.0
        for s in states:
            a = policy.get(s, None)
            if a is None:
                v_new = 0.0
            else:
                q = 0.0
                for (p, s_next) in get_transitions(s, a):
                    r = get_reward(s, a, s_next)
                    q += p * (r + gamma * V[s_next])
                v_new = q
            delta = max(delta, abs(V[s] - v_new))
            V[s] = v_new
        it += 1
        if delta < theta:
            break
    return V

def policy_iteration(states, actions, transitions, rewards, gamma=0.9, theta=1e-6, max_policy_iters=100):
    """
    Policy Iteration: devuelve (V, policy_opt).
    - states: iterable de estados
    - actions: iterable de acciones (acciones disponibles globalmente; si en un estado no hay acciones, policy[s] debe omitirse o ser None)
    - transitions: dict (s,a) -> list of (prob, s_next)
    - rewards: dict (s,a,s_next)->r o (s,a)->r
    """
    # Inicializar política arbitraria (por ejemplo, primera acción para cada estado)
    policy = {}
    for s in states:
        # si no hay transiciones definidas para ningun (s,a), dejamos policy[s]=None
        has_action = any((s,a) in transitions and transitions[(s,a)] for a in actions)
        policy[s] = actions[0] if has_action else None

    def get_transitions(s, a):
        return transitions.get((s, a), [])

    def get_reward(s, a, s_next):
        r_key = (s, a, s_next)
        if r_key in rewards:
            return rewards[r_key]
        r_key2 = (s, a)
        return rewards.get(r_key2, 0.0)

    for pi_iter in range(max_policy_iters):
        # 1) Evaluar la política actual
        V = policy_evaluation(policy, states, actions, transitions, rewards, gamma=gamma, theta=theta)

        # 2) Mejorar la política
        policy_stable = True
        for s in states:
            # si no hay acciones válidas en s, mantener policy[s]=None
            best_a = None
            best_q = -math.inf
            any_action = False
            for a in actions:
                trans = get_transitions(s, a)
                if not trans:
                    continue
                any_action = True
                q = 0.0
                for (p, s_next) in trans:
                    r = get_reward(s, a, s_next)
                    q += p * (r + gamma * V[s_next])
                if q > best_q:
                    best_q = q
                    best_a = a
            if not any_action:
                new_action = None
            else:
                new_action = best_a

            if policy.get(s) != new_action:
                policy_stable = False
                policy[s] = new_action

        if policy_stable:
            break

    # retornar valor y política final
    V_final = policy_evaluation(policy, states, actions, transitions, rewards, gamma=gamma, theta=theta)
    return V_final, policy

# -------------------------
# Ejemplo concreto (muy similar al anterior)
# -------------------------
if __name__ == "__main__":
    states = ['s0', 's1', 's2', 'terminal']
    actions = ['a0', 'a1']

    transitions = {
        ('s0','a0'): [(1.0, 's1')],
        ('s0','a1'): [(1.0, 's2')],
        ('s1','a0'): [(0.8, 's1'), (0.2, 's2')],
        ('s1','a1'): [(1.0, 'terminal')],
        ('s2','a0'): [(1.0, 'terminal')],
        ('s2','a1'): [(1.0, 's0')],
        # terminal no tiene transiciones
        ('terminal','a0'): [],
        ('terminal','a1'): []
    }

    rewards = {
        ('s1','a0','s1'): 2,
        ('s1','a0','s2'): -1,
        ('s1','a1','terminal'): 10,
        ('s2','a0','terminal'): 5,
        ('s2','a1','s0'): -2
    }

    V_opt, policy_opt = policy_iteration(states, actions, transitions, rewards, gamma=0.9, theta=1e-6)
    print("Valores V* obtenidos por Policy Iteration:")
    for s in V_opt:
        print(f"  {s}: {V_opt[s]:.6f}")
    print("\nPolítica óptima encontrada (acción por estado):")
    for s in policy_opt:
        print(f"  {s}: {policy_opt[s]}")