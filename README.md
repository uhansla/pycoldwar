# PyColdWar

## Overview

**PyColdWar** is a command-line tool that allows you to automatically modify a DCS (Digital Combat Simulator) mission file by applying Cold War-era templates for aircraft, helicopters, and ground units.

The tool extracts sample units from a given Cold War mission and overwrites the types, payloads, and liveries of the units in a target mission, creating a Cold War-style variant.

---

## Features

- 🔄 Automatically replace modern units with Cold War units
- ✈️ Plane, 🚁 Helicopter, 🚛 Ground unit support
- 🎯 Match units based on mission roles (e.g., SEAD, CAS, Strike, Patrol)
- 🛠️ Optional skipping of planes, ground units, or helicopters
- 🗂️ Saves modified mission file to a specified output folder
- ✅ Clean and informative console logging

---

## Requirements

- Python 3.8+
- Pretense Syria Cold War mission file (it uses this mission file to copy the cold war units)
- Access to `.miz` mission files extracted into folder structure (specifically the `mission` file inside)

---

## Usage

Extract the archive:

```bash
unzip pycoldwar_final.zip
```

Then run the script:

```bash
python pycoldwar.py --mm /path/to/modern_mission/mission --cm /path/to/coldwar_mission/mission --op /path/to/output_folder
```

### Command Line Arguments

| Argument              | Short | Description |
|:----------------------|:------|:-------------|
| `--mission_to_modify`  | `--mm` | Path to the mission file you want to modify |
| `--coldwar_mission`    | `--cm` | Path to the Cold War mission to extract samples from |
| `--output_folder`      | `--op` | Path to folder where modified mission will be saved |
| `--skip_planes`        | -      | Skip modifying plane units |
| `--skip_ground`        | -      | Skip modifying ground units |
| `--skip_heli`          | -      | Skip modifying helicopter units |

### Example

```bash
python pycoldwar.py --mm ./modern/mission --cm ./coldwar/mission --op ./output_folder
```

or with short flags:

```bash
python pycoldwar.py --mm ./modern/mission --cm ./coldwar/mission --op ./output_folder
```

Skip helicopters if needed:

```bash
python pycoldwar.py --mm ./modern/mission --cm ./coldwar/mission --op ./output_folder --skip_heli
```

---

## Notes

- The mission files should be extracted `.miz` archives, and you should point to the `mission` file inside.
- This tool **does not repackage `.miz` files**; it modifies and saves the `mission` file only. You can manually zip the mission structure into a `.miz` if needed.
- Make sure you have proper backups of your missions before modifying.

---

## License

MIT License

---

Enjoy converting your DCS missions to Cold War era battles! ✈️🚁🚛