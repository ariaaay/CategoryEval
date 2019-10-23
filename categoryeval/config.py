from pathlib import Path


class Dirs:
    root = Path(__file__).parent.parent
    src = Path(__file__).parent
    probes = root / 'probes'


class Eval:
    num_opt_init_steps = 0
    num_opt_steps = 5
    xi = 0.01  # 0.01 is better than 0.05
    verbose = False
    eval_thresholds = [[0.9]]