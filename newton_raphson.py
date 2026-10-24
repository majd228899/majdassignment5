# Newton-Raphson for f(x) = 4x^3 - 15x^2 + 17x - 6, x0 = 3
def f(x):
    return 4*x**3 - 15*x**2 + 17*x - 6

def df(x):
    return 12*x**2 - 30*x + 17

def newton_raphson(x0, eps=1e-6, max_iter=50):
    x = x0
    print(f"{'r':>2} {'x_r':>12} {'f(x_r)':>12} {'f_prime(x_r)':>14} {'x_r+1':>12} {'|dx|':>12}")
    for r in range(max_iter):
        fx, dfx = f(x), df(x)
        if dfx == 0:
            raise ZeroDivisionError("f'(x) = 0, Newton-Raphson fails")
        x_new = x - fx / dfx
        print(f"{r:>2} {x:12.6f} {fx:12.6f} {dfx:14.6f} {x_new:12.6f} {abs(x_new - x):12.6f}")
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    raise RuntimeError("Divergent: max iterations reached")

if __name__ == "__main__":
    root = newton_raphson(3.0)
    print(f"Root approximation: x = {root:.6f}")
