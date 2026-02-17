# tests/lab/tools/plotting.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass(frozen=True)
class CsvWaveform:
    time_s: np.ndarray
    volt: np.ndarray


def load_scope_csv(path: str | Path) -> CsvWaveform:
    """
    Load CSV written by labio.sds1104xe.save_waveform_csv().
    Expected header: time_s,volt
    """
    path = Path(path)
    data = np.loadtxt(path, delimiter=",", skiprows=1)
    return CsvWaveform(time_s=data[:, 0], volt=data[:, 1])


def decimate(time_s: np.ndarray, volt: np.ndarray, *, max_points: int = 200_000) -> tuple[np.ndarray, np.ndarray]:
    """
    Downsample uniformly for fast plotting.
    """
    n = len(time_s)
    if n <= max_points:
        return time_s, volt
    step = max(1, n // max_points)
    return time_s[::step], volt[::step]


def plot_waveform_png(
    csv_path: str | Path,
    png_path: str | Path,
    *,
    title: str = "Scope capture",
    max_points: int = 200_000,
) -> Path:
    """
    Convert scope CSV -> PNG plot.
    """
    # Import matplotlib lazily so non-plot users don't pay import cost.
    import matplotlib.pyplot as plt

    csv_path = Path(csv_path)
    png_path = Path(png_path)

    wf = load_scope_csv(csv_path)
    t, v = decimate(wf.time_s, wf.volt, max_points=max_points)

    plt.figure()
    plt.plot(t, v)
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.title(title)
    plt.tight_layout()

    png_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(png_path, dpi=150)
    plt.close()

    return png_path
