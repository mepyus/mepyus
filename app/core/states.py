from enum import Enum


class SeedState(str, Enum):
    ISOLATED = "isolated"
    FORMING = "forming"
    REENTERING = "reentering"
    CELL_CANDIDATE = "cell_candidate"
    CELL_BOUND = "cell_bound"


class CellState(str, Enum):
    CANDIDATE = "candidate"
    HELD = "held"
    UNSTABLE = "unstable"
    REENTERING = "reentering"
    DISSOLVED = "dissolved"


class LocalSpaceState(str, Enum):
    FORMING = "forming"
    STABLE_LOCAL = "stable_local"
    SPARSE = "sparse"
    BOUNDARY_HEAVY = "boundary_heavy"
    BRIDGE_EXPOSED = "bridge_exposed"


class BridgeState(str, Enum):
    CANDIDATE = "candidate"
    OBSERVED = "observed"
    HELD = "held"
