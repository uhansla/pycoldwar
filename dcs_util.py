import pandas as pd
from dcs.weapons_data import Weapons
from lupa import LuaRuntime
import os
import random
from collections import defaultdict


# --- Step 1: Build CLSID → Weapon Info mapping ---
clsid_to_weapon = {}
for attr in dir(Weapons):
    weapon = getattr(Weapons, attr)
    if isinstance(weapon, dict):
        clsid = weapon.get("clsid", "").strip()
        if clsid:
            clsid_to_weapon[clsid] = {
                "name": weapon.get("name", "Unknown Weapon").strip(),
                "weight": weapon.get("weight", 0)
            }

def load_mission(path):
    lua = LuaRuntime(unpack_returned_tuples=True)

    with open(path, "r", encoding="utf-8") as f:
        lua_code = f.read()
    lua.execute(lua_code)
    mission = lua.globals().mission

    mission_data = lua_table_to_dict(mission)

    return mission_data, lua

def get_planes(mission_data):
    unit_rows = []
    for side in ["blue", "red", "neutral"]:
        countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
        for _, country in countries.items():
            plane = country.get("plane", {})
            groups = plane.get("group", {})
            for _, group in groups.items():
                group_name = group.get("name", "Unknown Group")
                for _, unit in group.get("units", {}).items():
                    unit_name = unit.get("name", "Unknown Unit")
                    unit_type = unit.get("type", "Unknown Type")
                    unit_skill = unit.get("skill", "Unknown Skill")
                    unit_livery = unit.get("livery_id", "Unknown Livery")

                    possible_pylons = [
                        unit.get("payload", {}).get("pylons") if isinstance(unit.get("payload"), dict) else None,
                        unit.get("pylons"),
                        unit.get("task", {}).get("pylons") if isinstance(unit.get("task"), dict) else None,
                        unit.get("additional_task", {}).get("pylons") if isinstance(unit.get("additional_task"), dict) else None
                    ]

                    pylons = next((p for p in possible_pylons if isinstance(p, dict)), {})

                    clsid_list = []
                    weapon_names = []
                    weapon_weights = []

                    for _, pylon in pylons.items():
                        if isinstance(pylon, dict):
                            clsid = pylon.get("CLSID")
                            if clsid:
                                clsid = clsid.strip()
                                clsid_list.append(clsid)
                                weapon = clsid_to_weapon.get(clsid, {})
                                weapon_names.append(weapon.get("name", "Unknown Weapon"))
                                weapon_weights.append(weapon.get("weight", 0))

                    unit_rows.append({
                        "Side": side.capitalize(),
                        "Group Name": group_name,
                        "Unit Name": unit_name,
                        "Unit Type": unit_type,
                        "Skill": unit_skill,
                        "Livery ID": unit_livery,
                        "Weapons CLSID": ", ".join(clsid_list),
                        "Weapon Names": ", ".join(weapon_names),
                        "Total Weapon Weight (kg)": sum(weapon_weights)
                    })

    # Display as DataFrame
    df_units = pd.DataFrame(unit_rows)
    return df_units

def get_helicopters(mission_data):
    unit_rows = []
    for side in ["blue", "red", "neutral"]:
        countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
        for _, country in countries.items():
            helicopter = country.get("helicopter", {})
            groups = helicopter.get("group", {})
            for _, group in groups.items():
                group_name = group.get("name", "Unknown Group")
                for _, unit in group.get("units", {}).items():
                    unit_name = unit.get("name", "Unknown Unit")
                    unit_type = unit.get("type", "Unknown Type")
                    unit_skill = unit.get("skill", "Unknown Skill")
                    unit_livery = unit.get("livery_id", "Unknown Livery")

                    possible_pylons = [
                        unit.get("payload", {}).get("pylons") if isinstance(unit.get("payload"), dict) else None,
                        unit.get("pylons"),
                        unit.get("task", {}).get("pylons") if isinstance(unit.get("task"), dict) else None,
                        unit.get("additional_task", {}).get("pylons") if isinstance(unit.get("additional_task"), dict) else None
                    ]

                    pylons = next((p for p in possible_pylons if isinstance(p, dict)), {})

                    clsid_list = []
                    weapon_names = []
                    weapon_weights = []

                    for _, pylon in pylons.items():
                        if isinstance(pylon, dict):
                            clsid = pylon.get("CLSID")
                            if clsid:
                                clsid = clsid.strip()
                                clsid_list.append(clsid)
                                weapon = clsid_to_weapon.get(clsid, {})
                                weapon_names.append(weapon.get("name", "Unknown Weapon"))
                                weapon_weights.append(weapon.get("weight", 0))

                    unit_rows.append({
                        "Side": side.capitalize(),
                        "Group Name": group_name,
                        "Unit Name": unit_name,
                        "Unit Type": unit_type,
                        "Skill": unit_skill,
                        "Livery ID": unit_livery,
                        "Weapons CLSID": ", ".join(clsid_list),
                        "Weapon Names": ", ".join(weapon_names),
                        "Total Weapon Weight (kg)": sum(weapon_weights)
                    })

    # Display as DataFrame
    df_units = pd.DataFrame(unit_rows)
    return df_units

def get_ground_units(mission_data):
    # --- Step 3: Extract ground unit data ---
    ground_unit_rows = []
    for side in ["blue", "red", "neutral"]:
        countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
        for _, country in countries.items():
            vehicle = country.get("vehicle", {})
            groups = vehicle.get("group", {})
            for _, group in groups.items():
                group_name = group.get("name", "Unknown Group")
                for _, unit in group.get("units", {}).items():
                    unit_name = unit.get("name", "Unknown Unit")
                    unit_type = unit.get("type", "Unknown Type")
                    unit_skill = unit.get("skill", "Unknown Skill")

                    ground_unit_rows.append({
                        "Side": side.capitalize(),
                        "Group Name": group_name,
                        "Unit Name": unit_name,
                        "Unit Type": unit_type,
                        "Skill": unit_skill
                    })

    # Display ground units as DataFrame
    df_ground_units = pd.DataFrame(ground_unit_rows)
    return df_ground_units

# Convert Lua table to Python dict
def lua_table_to_dict(lua_table):
    if hasattr(lua_table, 'items'):
        return {k: lua_table_to_dict(v) for k, v in lua_table.items()}
    else:
        return lua_table

# Convert Python dict back to Lua table
def dict_to_lua_table(py_dict, lua):
    tbl = lua.table()
    for k, v in py_dict.items():
        tbl[k] = dict_to_lua_table(v, lua) if isinstance(v, dict) else v
    return tbl

# Serialize Lua table to string
def serialize_lua_table(d, indent=0):
    lines = ["{"]
    pad = " " * (indent + 4)
    for k, v in d.items():
        if isinstance(k, int):
            k_str = f"[{k}]"
        else:
            k_str = f"[\"{k}\"]"

        if isinstance(v, dict):
            v_str = serialize_lua_table(v, indent + 4)
        elif isinstance(v, str):
            escaped = v.replace("\\", "\\\\").replace("\"", "\\\"")
            v_str = f'"{escaped}"'
        elif isinstance(v, bool):
            v_str = "true" if v else "false"
        elif v is None:
            v_str = "nil"
        else:
            v_str = str(v)

        lines.append(f"{pad}{k_str} = {v_str},")
    lines.append(" " * indent + "}")
    return "\n".join(lines)



# Save modified mission to file
def save_modified_mission(mission_data, output_path):
    lua_script = f"mission = {serialize_lua_table(mission_data)}"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(lua_script)
    print(f"✅ Modified mission written to {output_path}")

# Find sample unit
def find_sample_unit(mission_data, side, unit_type, group_contains = None):
    sample_unit = None
    #for side in ["blue", "red", "neutral"]:
    countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
    for _, country in countries.items():
        groups = country.get("plane", {}).get("group", {})

        for _, group in groups.items():
            group_name = group.get("name", "")
            # print(group_name)
            # print(group_contains in group_name)
            if group_contains is None or group_contains in group_name:
                for _, unit in group.get("units", {}).items():
                    if unit.get("type") == unit_type and unit.get("skill", "").lower() != "client":
                        sample_unit = unit
                        break
                if sample_unit:
                    break
        if sample_unit:
            break
    # if sample_unit:
    #     break

    if not sample_unit:
        raise ValueError(f"No {unit_type} unit with skill != 'Client' found.")

    return sample_unit

# Modify mission using sample maps
def apply_sample_templates(mission_data, blue_map, red_map):
    mod_count = 0
    for side in ["blue", "red"]:
        coalition = mission_data.get("coalition", {}).get(side, {})
        countries = coalition.get("country", {})
        side_map = blue_map if side == "blue" else red_map

        for _, country in countries.items():
            groups = country.get("plane", {}).get("group", {})
            for _, group in groups.items():
                group_name = group.get("name", "").lower()
                for mission_type in side_map:
                    if mission_type in group_name:
                        sample_units = side_map[mission_type]
                        if not sample_units:
                            continue
                        sample = random.choice(sample_units)
                        for _, unit in group.get("units", {}).items():
                            unit["type"] = sample.get("type")
                            unit["livery_id"] = sample.get("livery_id")
                            unit["payload"] = sample.get("payload", {}).copy()
                            unit.pop("pylons", None)
                            mod_count += 1
                        break  # only apply one template per group
    print(f"✅ Modified {mod_count} unit(s) based on sample maps.")

# Extract ground sample templates from mission

def extract_ground_templates(mission_data, mission_types=["supply", "assault"]):
    ground_map = {"blue": {}, "red": {}}
    for side in ["blue", "red"]:
        ground_map[side] = {}
        countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
        for _, country in countries.items():
            vehicle = country.get("vehicle", {})
            groups = vehicle.get("group", {})
            for _, group in groups.items():
                group_name = group.get("name", "").lower()
                for mission_type in mission_types:
                    if mission_type in group_name:
                        sample_units = list(group.get("units", {}).values())
                        if sample_units:
                            ground_map[side].setdefault(mission_type, []).append(sample_units)
    return ground_map

# Replace ground units with matching group size and mission type

def apply_ground_templates(mission_data, ground_map):
    mod_count = 0
    for side in ["blue", "red"]:
        countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
        for _, country in countries.items():
            vehicle = country.get("vehicle", {})
            groups = vehicle.get("group", {})
            for group_key, group in groups.items():
                group_name = group.get("name", "").lower()
                unit_count = len(group.get("units", {}))
                for mission_type, templates in ground_map.get(side, {}).items():
                    if mission_type in group_name:
                        matching_templates = [t for t in templates if len(t) == unit_count]
                        if matching_templates:
                            selected = random.choice(matching_templates)
                        elif templates:
                            selected = random.choice(templates)[:unit_count]  # fallback: crop to size
                        else:
                            continue

                        for unit_key, sample in zip(group.get("units", {}).keys(), selected):
                            group["units"][unit_key]["type"] = sample.get("type")
                            group["units"][unit_key]["skill"] = sample.get("skill")
                            group["units"][unit_key]["name"] = sample.get("name")
                            mod_count += 1
                        break
    print(f"✅ Modified {mod_count} ground unit(s) based on group size and mission type.")

# Extract helicopter templates by mission type
def extract_helicopter_templates(mission_data, mission_types=['supply', 'cas']):
    from collections import defaultdict
    heli_map = {"blue": defaultdict(list), "red": defaultdict(list)}
    for side in ["blue", "red"]:
        countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
        for _, country in countries.items():
            groups = country.get("helicopter", {}).get("group", {})
            for _, group in groups.items():
                group_name = group.get("name", "").lower()
                for mission_type in mission_types:
                    if mission_type in group_name:
                        for _, unit in group.get("units", {}).items():
                            if unit.get("skill", "").lower() != "client":
                                heli_map[side][mission_type].append(unit)
    return heli_map

# Apply helicopter templates to mission
def apply_helicopter_templates(mission_data, heli_map):
    mod_count = 0
    for side in ["blue", "red"]:
        countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
        for _, country in countries.items():
            groups = country.get("helicopter", {}).get("group", {})
            for _, group in groups.items():
                group_name = group.get("name", "").lower()
                for mission_type in heli_map[side]:
                    if mission_type in group_name:
                        sample_units = heli_map[side][mission_type]
                        if not sample_units:
                            continue
                        sample = random.choice(sample_units)
                        for _, unit in group.get("units", {}).items():
                            unit["type"] = sample.get("type")
                            unit["livery_id"] = sample.get("livery_id")
                            unit["payload"] = sample.get("payload", {}).copy()
                            unit.pop("pylons", None)
                            mod_count += 1
                        break
    print(f"✅ Modified {mod_count} helicopter unit(s) based on templates.")

def extract_plane_templates(mission_data, mission_types, side):
    plane_map = defaultdict(list)
    countries = mission_data.get("coalition", {}).get(side, {}).get("country", {})
    for _, country in countries.items():
        groups = country.get("plane", {}).get("group", {})
        for _, group in groups.items():
            group_name = group.get("name", "").lower()
            for mission_type in mission_types:
                if mission_type in group_name:
                    for _, unit in group.get("units", {}).items():
                        if unit.get("skill", "").lower() != "client":
                            plane_map[mission_type].append(unit)
    return plane_map