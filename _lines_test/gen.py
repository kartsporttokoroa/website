import math

def elbow_path(x0, y0, turn_x, y1, x1, r):
    """Horizontal from (x0,y0) to (turn_x,y0), rounded corner radius r, then vertical down to y1 at x1."""
    # horizontal segment ends before the corner, arc sweeps, vertical continues
    hx_end = turn_x - r
    vy_start = y0 + r
    return f"M {x0},{y0} L {hx_end},{y0} A {r},{r} 0 0 1 {turn_x},{vy_start} L {turn_x},{y1}"

N = 9
gap = 6
base_r = 40
lines = []
for i in range(N):
    x0 = 0
    y0 = i*gap
    turn_x = 260 + i*gap
    r = base_r + i*gap
    y1 = 340
    lines.append(elbow_path(x0, y0, turn_x, y1, turn_x, r))

svg_paths = "\n".join(f'  <path d="{p}" />' for p in lines)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -10 380 380" fill="none" stroke="currentColor" stroke-width="2.4">
{svg_paths}
</svg>'''
open("elbow.svg","w").write(svg)
print(svg[:200])
