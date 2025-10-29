import math

def value_iteration(states, actions, transitions, rewards, gamma=0.9, theta=1e-6, max_iters=10000):
    """
    Value Iteration para MDP finito.

    states: iterable de estados (hashable)
    actions: iterable de acciones (hashable)
    transitions: función o dict que devuelve lista de (prob, next_state) para (s,a)
                 Puede ser dict con key (s,a) -> [(p, s_next), ...]
    rewards: función o dict que devuelve R(s,a,s_next) o R(s,a)
             Puede ser dict (s,a,s_next)->r o (s,a)->r.
    gamma: factor de descuento (0 <= gamma < 1)
    theta: umbral para detener iteraciones (cuando delta < theta)
    max_iters: límite de iteraciones por seguridad
    """
    # V: valor estimado de cada estado
    V = {s: 0.0 for s in states}

    def get_transitions(s, a):
        # devuelve lista de (p, s_next)
        if isinstance(transitions, dict):
            return transitions.get((s, a), [])
        else:
            return transitions(s, a)

    def get_reward(s, a, s_next):
        if isinstance(rewards, dict):
            # si existe recompensa dependiente de s_next
            r_key = (s, a, s_next)
            if r_key in rewards:
                return rewards[r_key]
            # si hay recompensa dependiente solo de (s,a)
            r_key2 = (s, a)
            return rewards.get(r_key2, 0.0)
        else:
            return rewards(s, a, s_next)

    it = 0
    while True:
        delta = 0.0
        for s in states:
            # calcular acción-valor Q(s,a) para todas las acciones
            q_values = []
            for a in actions:
                q = 0.0
                for (p, s_next) in get_transitions(s, a):
                    r = get_reward(s, a, s_next)
                    q += p * (r + gamma * V[s_next])
                q_values.append(q)
            if not q_values:
                v_new = 0.0
            else:
                v_new = max(q_values)
            delta = max(delta, abs(V[s] - v_new))
            V[s] = v_new
        it += 1
        if delta < theta or it >= max_iters:
            break

    # Extraer política determinista: pi(s) = argmax_a Q(s,a)
    policy = {}
    for s in states:
        best_a = None
        best_q = -math.inf
        for a in actions:
            q = 0.0
            for (p, s_next) in get_transitions(s, a):
                r = get_reward(s, a, s_next)
                q += p * (r + gamma * V[s_next])
            if q > best_q:
                best_q = q
                best_a = a
        policy[s] = best_a

    return V, policy

# -------------------------
# Ejemplo concreto (pequeño MDP)
# -------------------------
# Estados:
states = ['s0', 's1', 's2', 'terminal']

# Acciones (mismas acciones posibles en todos los estados; en 'terminal' no hay transiciones)
actions = ['a0', 'a1']

# Transitions: dict (s,a) -> list of (prob, s_next)
transitions = {
    # desde s0
    ('s0','a0'): [(1.0, 's1')],
    ('s0','a1'): [(1.0, 's2')],
    # desde s1
    ('s1','a0'): [(0.8, 's1'), (0.2, 's2')],
    ('s1','a1'): [(1.0, 'terminal')],
    # desde s2
    ('s2','a0'): [(1.0, 'terminal')],
    ('s2','a1'): [(1.0, 's0')],  # ciclo posible
    # desde terminal: ninguna transición -> vacío (equivalente a permanecer con 0)
    ('terminal','a0'): [],
    ('terminal','a1'): []
}

# Rewards: podemos dar R(s,a,s_next) (aquí como dict)
rewards = {
    ('s0','a0','s1'): 0,
    ('s0','a1','s2'): 0,
    ('s1','a0','s1'): 2,      # recompensa por quedarse en s1 con a0
    ('s1','a0','s2'): -1,
    ('s1','a1','terminal'): 10,
    ('s2','a0','terminal'): 5,
    ('s2','a1','s0'): -2
    # transiciones sin entrada => recompensa 0 por defecto
}

if __name__ == "__main__":
    V_opt, policy_opt = value_iteration(states, actions, transitions, rewards, gamma=0.9, theta=1e-6)
    print("Valores óptimos V*:")
    for s in V_opt:
        print(f"  {s}: {V_opt[s]:.6f}")
    print("\nPolítica óptima (acción por estado):")
    for s in policy_opt:
        print(f"  {s}: {policy_opt[s]}")