# FlexFx Guitar Pedal (Teensy 4.0)

Bring-up repo for a Teensy 4.0 + Teensy Audio Shield (SGTL5000) guitar pedal project.
Goal: verify clean audio passthrough first, then add DSP (bitcrush, etc).

## Repo Layout

- `firmware/teensy/platformio/` – Teensy firmware (PlatformIO)
- `tests/lab/` – Lab automation scripts (Siglent SDG1032X + SDS1104X-E via Ethernet)
- `submods/labio/` – Python instrument control library (git submodule)
- `docs/` – Datasheets and notes

## Prerequisites

### PlatformIO (recommended via pipx)

```bash
pipx install platformio
pio --version
````

### Teensy USB permissions (udev)

If you need Teensy CLI upload support without sudo, add udev rules (example):

```bash
sudo tee /etc/udev/rules.d/49-teensy.rules > /dev/null <<'EOF'
SUBSYSTEM=="usb", ATTR{idVendor}=="16c0", MODE:="0666"
KERNEL=="hidraw*", ATTRS{idVendor}=="16c0", MODE:="0666"
EOF

sudo udevadm control --reload-rules
sudo udevadm trigger
```

## Build + Upload Firmware

```bash
cd firmware/teensy/platformio
pio run
pio run -t upload
pio device monitor
```

## Lab Test (Passthrough)

### Setup

```bash
cd tests/lab
python3 -m venv .venv
source .venv/bin/activate

# install instrument library (editable)
pip install -r ../../submods/labio/requirements.txt
pip install -e ../../submods/labio
```

Create `tests/lab/configs/instruments.json`:

```json
{
  "sds1104xe": "192.168.1.101",
  "sdg1032x": "192.168.1.103",
  "teensy_serial": "/dev/ttyACM0"
}
```

### Run

```bash
python test_passthrough.py
```

## Notes

* Start with small signal levels (e.g. 100–300 mVpp) to avoid clipping the codec input.
* Use LINE IN / LINE OUT pins on the audio shield (not headphone jack) for clean line-level testing.
