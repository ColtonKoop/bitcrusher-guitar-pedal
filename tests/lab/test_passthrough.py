import json
import time
from pathlib import Path
from datetime import datetime

from labio.sdg1032x import sdg1032x
from labio.sds1104xe import sds1104xe, Coupling, ChannelUnit

from tools.plotting import plot_waveform_png

CONFIG_PATH = Path(__file__).parent / "configs" / "instruments.json"
RESULTS_DIR = Path(__file__).parent / "results"


def load_cfg():
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Missing {CONFIG_PATH}. Create it from your example JSON."
        )
    return json.loads(CONFIG_PATH.read_text())


def configure_generator(gen: sdg1032x, *, ch="C1", freq_hz=440, vpp=1, offset=0.0):
    # Siglent SDG uses BSWV for basic waveform configuration.
    # Example: C1:BSWV WVTP,SINE,FRQ,440,AMP,1,OFST,0
    gen.set_comm_header("OFF")
    gen.set_basic_wave(f"WVTP,SINE,FRQ,{freq_hz},AMP,{vpp},OFST,{offset}", channel=ch)
    gen.set_output(True, channel=ch)


def configure_scope(scope: sds1104xe, *, ch=1):
    scope.clear_measurements()

    # Show channel, set coupling, scaling, timebase, trigger
    scope.set_trace(ch, True)
    scope.set_coupling(ch, Coupling.DC_1M)  # or AC_1M; DC is fine for 0 offset tests
    scope.set_unit(ch, ChannelUnit.V)

    scope.set_vdiv(ch, 0.100)   # 100 mV/div (adjust as needed)
    scope.set_offset(ch, 0.0)

    scope.set_time_div(1e-3)   # 1 ms/div for ~1kHz
    scope.set_trigger_source(f"C{ch}")
    scope.set_trigger_mode("EDGE")
    scope.set_trigger_slope("POS")
    scope.set_trigger_level(0.0)

    # Autoset can work too, but manual is repeatable:
    # scope.autoset(wait=True)


def measure(scope: sds1104xe, *, ch=1):
    """
    Use the SDS "parameter value" measurement interface:
      <source>:PAVA? <parameter>
    """
    src = f"C{ch}"
    freq = scope.get_parameter_value(src, "FREQ")
    vpp = scope.get_parameter_value(src, "PKPK")
    vrms = scope.get_parameter_value(src, "RMS")
    return {"freq": freq, "vpp": vpp, "vrms": vrms}


def main():
    cfg = load_cfg()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    sdg_ip = cfg["sdg1032x"]
    sds_ip = cfg["sds1104xe"]

    # Starter stimulus (safe)
    freq_hz = 420
    vpp = 1.0
    offset = 0.0

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_json = RESULTS_DIR / f"passthrough_{stamp}.json"
    out_csv = RESULTS_DIR / f"scope_ch1_{stamp}.csv"

    results = {
        "timestamp": stamp,
        "sdg_ip": sdg_ip,
        "sds_ip": sds_ip,
        "stimulus": {"freq_hz": freq_hz, "vpp": vpp, "offset": offset},
        "idn": {},
        "measurements": {},
        "waveform_csv": str(out_csv),
    }

    with sdg1032x(sdg_ip) as gen, sds1104xe(sds_ip) as scope:
        results["idn"]["sdg1032x"] = gen.idn()
        results["idn"]["sds1104xe"] = scope.idn()

        configure_generator(gen, ch="C1", freq_hz=freq_hz, vpp=vpp, offset=offset)
        configure_scope(scope, ch=1)

        # let codec + scope settle
        time.sleep(0.5)

        results["measurements"]["ch1"] = measure(scope, ch=1)

        # Optional: capture waveform to CSV
        meta = scope.save_waveform_csv(str(out_csv), trace="C1", section="DAT2")
        results["measurements"]["waveform_meta"] = meta

        # Plot waveform
        out_png = RESULTS_DIR / f"scope_ch1_{stamp}.png"
        plot_waveform_png(out_csv, out_png, title="Passthrough test - CH1")
        results["waveform_png"] = str(out_png)

    out_json.write_text(json.dumps(results, indent=2))
    print(f"Wrote: {out_json}")
    print(json.dumps(results["measurements"], indent=2))


if __name__ == "__main__":
    main()
