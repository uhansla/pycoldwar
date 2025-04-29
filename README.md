# PyColdWar

## Overview

**PyColdWar** is a command-line tool that modifies a DCS (Digital Combat Simulator) mission file by applying Cold War-era templates for aircraft, helicopters, and ground units.

The tool uses predefined Cold War unit templates (already built into the project) to overwrite the types, payloads, and liveries of modern units in a target mission — converting it into a Cold War-style mission.

---

## Features

- ✈️ 🚁 🚛 Replace modern units with Cold War equivalents (planes, helicopters, ground units)
- 🎯 Match groups based on mission roles (CAS, Strike, SEAD, Patrol, Supply)
- 🔀 Random selection of loadouts/templates for each group
- 🛠️ Skip modifying planes, ground units, or helicopters individually if needed
- 🗂️ Saves the modified mission file into a specified output folder
- ✅ Clean console logging for all steps

---

## Requirements

- Python 3.8+
- Prebuilt Cold War templates (included in project)
- Access to extracted `.miz` mission folders (specifically the `mission` file)

---

## Usage

Extract the archive:

```bash
unzip pycoldwar_final.zip
```

Then run the script:

```bash
python pycoldwar.py --mm /path/to/modern_mission/mission --op /path/to/output_folder
```

### Command Line Arguments

| Argument                | Short | Description |
|:-------------------------|:------|:------------|
| `--mission_to_modify`     | `--mm` | Path to the mission file you want to modify |
| `--output_folder`         | `--op` | Path to folder where modified mission will be saved |
| `--skip_planes`           |        | Skip modifying planes |
| `--skip_ground`           |        | Skip modifying ground vehicles |
| `--skip_heli`             |        | Skip modifying helicopters |

✅ **Note**:  
The `--cm` (coldwar_mission) argument is no longer required —  
the system uses **built-in loadouts and liveries**.

---

### Examples

Modify everything:

```bash
python pycoldwar.py --mm ./modern/mission --op ./output_folder
```

Skip helicopters:

```bash
python pycoldwar.py --mm ./modern/mission --op ./output_folder --skip_heli
```

Skip planes and ground vehicles (only modify helicopters):

```bash
python pycoldwar.py --mm ./modern/mission --op ./output_folder --skip_planes --skip_ground
```

---

## How to Create or Modify Your Own Loadouts

PyColdWar uses **prebuilt loadout templates** located in the `loadouts` folder.  
You can customize or create new loadouts easily by editing or adding to these Python files.

### Example: Adding a New Aircraft CAS Loadout

Each loadout file (e.g., `plane_cas.py`) defines a `planes_map` dictionary.  
Each aircraft has a structure like:

```python
planes_map = {
    'F_A_18A': [
        {
            "type": planes.F_A_18A,
            "id": planes.F_A_18A.id,
            "fuel": planes.F_A_18A.fuel_max,
            "chaff": planes.F_A_18A.chaff,
            "flare": planes.F_A_18A.flare,
            "payload": {
                "pylons": [
                    planes.F_A_18A.Pylon1.AIM_9P_Sidewinder_IR_AAM,
                    planes.F_A_18A.Pylon2.LAU_117_with_AGM_65K___Maverick,
                    None,
                    ...
                ]
            }
        }
    ]
}
```

**To add a new aircraft template**:
1. Import the plane class from `dcs.planes`.
2. Define its `fuel`, `chaff`, `flare`, and `pylons` according to available weapons.
3. List each pylon's loadout. Use `None` for empty pylons.

**Pylons must match the exact number and order** of the aircraft's available hardpoints.

---

### General Guidelines

- **Type** must point to the correct aircraft class (e.g., `planes.F_5E`).
- **Fuel**, **chaff**, and **flare** should match the plane’s defaults.
- **Payload → Pylons** is an array of weapons, missiles, bombs, pods, etc.
- Use `None` if no weapon is mounted on a pylon.
- Weapon references must match the correct pylon classes.

### Notes

- You can add **multiple loadouts** for the same aircraft.
- You can create variants by copying an existing entry and adjusting pylons.
- Mistakes (e.g., wrong weapon CLSID) might cause mission generation to fail.

---

## Notes

- You must point to the extracted `mission` file inside a decompressed `.miz` folder.
- This tool **does not repackage** `.miz` archives automatically.  
  After modification, manually zip the mission folder if you want to restore it to `.miz`.
- Always keep a backup of your original mission files!

---

## License

MIT License

---

Enjoy converting your DCS missions into Cold War scenarios! ✈️🚁🚛
