import json
from pathlib import Path
from labio.sds1104xe import sds1104xe

cfg = json.loads(Path("configs/instruments.json").read_text())
s = sds1104xe(cfg["sds1104xe"], timeout_ms=20000)

print(s.idn())
print(s.get_sast())          # acquisition status
print(s.get_parameter_value("C1", "PKPK"))  # peak-to-peak
print(s.check_error())

s.close()
