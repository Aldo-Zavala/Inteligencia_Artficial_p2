import math

# --- Definición de funciones de utilidad comunes ---
def u_linear(x):
    return x

def u_log(x, eps=1e-9):
    # dominio x > 0; añadir eps para evitar log(0)
    return math.log(x + eps)

def u_sqrt(x):
    return math.sqrt(x)

def u_quad(x):
    return x**2

def u_exponential(x, a=0.01):
    # utilidad exponencial común para aversión al riesgo (a>0 => aversión)
    return 1 - math.exp(-a * x)

# --- Operaciones sobre loterías ---
def expected_utility(lottery, utility_fn):
    """
    lottery: lista de tuplas (outcome, prob), por ejemplo [(0, 0.5), (100, 0.5)]
    utility_fn: función que toma outcome -> utilidad
    """
    return sum(p * utility_fn(x) for x, p in lottery)

def expectation(lottery):
    return sum(p * x for x, p in lottery)

def certainty_equivalent(lottery, utility_fn, inverse_utility_fn, tol=1e-6, max_iter=100):
    """
    Calcula el equivalente cierto CE resolviendo u(CE) = EU.
    Necesita la inversa de la función de utilidad (o busca numéricamente si no hay inversa simple).
    """
    eu = expected_utility(lottery, utility_fn)
    # si hay inversa analítica proporcionada:
    if inverse_utility_fn is not None:
        return inverse_utility_fn(eu)
    # búsqueda binaria simple en [low, high]
    low, high = -1e6, 1e6
    for _ in range(max_iter):
        mid = (low + high) / 2
        try:
            val = utility_fn(mid)
        except Exception:
            # si utility_fn no admite valores negativos (ej log), ajustar low
            low = max(low, 0)
            mid = (low + high) / 2
            val = utility_fn(mid)
        if abs(val - eu) < tol:
            return mid
        if val < eu:
            low = mid
        else:
            high = mid
    return mid  # aproximación

def risk_premium(lottery, utility_fn, inverse_utility_fn=None):
    e_x = expectation(lottery)
    ce = certainty_equivalent(lottery, utility_fn, inverse_utility_fn)
    return e_x - ce, e_x, ce

# --- Inversas (cuando existen) ---
def inv_u_linear(u):
    return u

def inv_u_log(u):
    # u = log(x) => x = exp(u)
    return math.exp(u)

def inv_u_sqrt(u):
    return u**2

def inv_u_quad(u):
    # u = x^2, para x >= 0:
    return math.sqrt(u)

def inv_u_exponential(u, a=0.01):
    # u = 1 - exp(-a x) => exp(-a x) = 1 - u => x = -ln(1-u)/a
    if u >= 1:
        return float('inf')
    return -math.log(1 - u) / a

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Lotería: 50% 0, 50% 100
    lottery = [(0, 0.5), (100, 0.5)]

    # Calcular EU con distintas utilidades
    for name, u_fn, inv_fn in [
        ("Lineal", u_linear, inv_u_linear),
        ("Log", u_log, inv_u_log),
        ("Sqrt", u_sqrt, inv_u_sqrt),
        ("Cuadrática", u_quad, inv_u_quad),
        ("Exponencial a=0.02", lambda x: u_exponential(x, a=0.02), lambda u: inv_u_exponential(u, a=0.02))
    ]:
        eu = expected_utility(lottery, u_fn)
        rp, e_x, ce = risk_premium(lottery, u_fn, inv_fn)
        print(f"{name}: EU={eu:.6f}, E[X]={e_x:.6f}, CE≈{ce:.6f}, Prima riesgo={rp:.6f}")
