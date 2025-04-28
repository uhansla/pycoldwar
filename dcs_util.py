import pandas as pd
from dcs.weapons_data import Weapons
import dcs.planes as planes
import dcs.helicopters as helicopters
from lupa import LuaRuntime
import os
import random
import coldwar_plane_cas as cas
from collections import defaultdict
import pprint


plane_mission_types = {'-sead-', '-patrol-', '-strike-', '-cas-'}
ground_mission_types = {'-supply-', '-assault-'}
heli_mission_types = {'-supply-', '-cas-'}

#### STATIC ####

clsid_to_plane_reference = {}

for plane_name in dir(planes):
    plane_class = getattr(planes, plane_name)
    if isinstance(plane_class, type):
        for attr_name in dir(plane_class):
            if attr_name.startswith("Pylon"):
                pylon = getattr(plane_class, attr_name)
                if isinstance(pylon, type):
                    for weapon_attr in dir(pylon):
                        weapon = getattr(pylon, weapon_attr)
                        if isinstance(weapon, tuple) and len(weapon) == 2:
                            weapon_data = weapon[1]
                            clsid = weapon_data.get("clsid", "").strip()
                            if clsid:
                                reference = f"planes.{plane_name}.{attr_name}.{weapon_attr}"
                                clsid_to_plane_reference[clsid] = reference

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
def find_sample_plane_unit(mission_data, side, unit_type, group_contains = plane_mission_types):
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
                        if ("-cas-" in group_name) or ("-strike-" in group_name) or ("-sead-" in group_name):
                            # Special CAS handling: select one CAS plane type + payload for whole group

                            cas_planes = cas.BLUE
                            if side == "red":
                                cas_planes = cas.RED


                            cas_plane_type = random.choice(cas_planes)
                            cas_plane = random.choice(cas.planes_map[cas_plane_type])
                            # print(cas_plane)
                            selected_type = cas_plane.get("id")
                            selected_fuel = cas_plane.get("fuel")
                            selected_chaff = cas_plane.get("chaff")
                            selected_flare = cas_plane.get("flare")
                            selected_livery_id = cas_plane.get("livery_id")
                            pylons = cas_plane["payload"]["pylons"]

                            clsids = []
                            for pylon in pylons:
                                if pylon is None:
                                    clsids.append("<CLEAN>")
                                else:
                                    clsids.append(pylon[1]["clsid"])

                            for _, unit in group.get("units", {}).items():
                                unit["type"] = selected_type
                                unit["livery_id"] = selected_livery_id
                                # unit["fuel"] = selected_fuel
                                # unit["chaff"] = selected_chaff
                                # unit["flare"] = selected_flare
                                unit["payload"] = {
                                    "pylons": {(i + 1): {"CLSID": clsid} for i, clsid in enumerate(clsids)},
                                    "fuel": selected_fuel,
                                    "chaff": selected_chaff,
                                    "flare": selected_flare,
                                    "gun": 100
                                }
                                unit.pop("pylons", None)
                                mod_count += 1
                        else:
                            # Normal handling for non-CAS groups
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

def extract_ground_templates(mission_data, mission_types=["-supply-", "-assault-"]):
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
def extract_helicopter_templates(mission_data, mission_types=['-supply-', '-cas-']):
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

# Extracts plane loadouts from mission data

def generate_plane_templates_from_mission(mission_data, mission_types=["cas", "sead", "strike"], save_to_file=None):
    plane_templates = {}

    for side in ["blue", "red"]:
        coalition = mission_data.get("coalition", {}).get(side, {})
        countries = coalition.get("country", {})

        for _, country in countries.items():
            groups = country.get("plane", {}).get("group", {})

            for _, group in groups.items():
                group_name = group.get("name", "").lower()

                matched_mission = None
                for mtype in mission_types:
                    if mtype in group_name:
                        matched_mission = mtype
                        break

                if matched_mission:
                    for _, unit in group.get("units", {}).items():
                        if unit.get("skill", "").lower() == "client":
                            continue  # skip client slots

                        unit_type = unit.get("type")
                        if not unit_type:
                            continue

                        # Try finding plane class
                        plane_class = getattr(planes, unit_type, None)
                        if plane_class is None:
                            fixed_unit_type = unit_type.replace("-", "_")
                            plane_class = getattr(planes, fixed_unit_type, None)

                        if plane_class is None:
                            continue  # skip unknown planes

                        # Now extract pylons
                        pylons_data = unit.get("payload", {}).get("pylons", {})
                        pylons_list = []

                        if pylons_data:
                            sample_key = next(iter(pylons_data.keys()))
                            key_is_str = isinstance(sample_key, str)
                            max_pylon = max(int(k) if isinstance(k, str) else k for k in pylons_data.keys())
                        else:
                            key_is_str = True
                            max_pylon = 0

                        for pylon_index in range(1, max_pylon + 1):
                            key = str(pylon_index) if key_is_str else pylon_index
                            pylon_info = pylons_data.get(key)

                            if pylon_info is None:
                                pylons_list.append(None)
                            else:
                                clsid = pylon_info.get("CLSID")
                                if clsid:
                                    # Match inside PylonX only
                                    pylon_attr = f"Pylon{pylon_index}"
                                    pylon_class = getattr(plane_class, pylon_attr, None)

                                    matched_reference = None
                                    if pylon_class and isinstance(pylon_class, type):
                                        for weapon_attr in dir(pylon_class):
                                            weapon = getattr(pylon_class, weapon_attr)
                                            if isinstance(weapon, tuple) and len(weapon) == 2:
                                                weapon_data = weapon[1]
                                                if weapon_data.get("clsid", "").strip() == clsid:
                                                    matched_reference = f"planes.{plane_class.__name__}.{pylon_attr}.{weapon_attr}"
                                                    break

                                    if matched_reference:
                                        pylons_list.append(matched_reference)
                                    else:
                                        pylons_list.append(None)
                                else:
                                    pylons_list.append(None)

                        # Detect optional fields
                        fuel = unit.get("fuel", None)
                        chaff = unit.get("chaff", None)
                        flare = unit.get("flare", None)

                        # Build the template
                        template = {
                            "type": plane_class.__name__,  # Save as class name string
                            "payload": {
                                "pylons": pylons_list
                            }
                        }
                        if fuel:
                            template["fuel"] = fuel
                        if chaff:
                            template["chaff"] = chaff
                        if flare:
                            template["flare"] = flare

                        if unit_type not in plane_templates:
                            plane_templates[unit_type] = []
                        plane_templates[unit_type].append(template)

    # De-duplicate templates
    for unit_type, templates in plane_templates.items():
        unique_templates = []
        seen_signatures = set()

        for template in templates:
            pylons_signature = tuple(template["payload"]["pylons"])
            if pylons_signature not in seen_signatures:
                seen_signatures.add(pylons_signature)
                unique_templates.append(template)

        plane_templates[unit_type] = unique_templates

    # Saving
    if save_to_file:
        save_folder = os.path.dirname(save_to_file)
        if save_folder:
            os.makedirs(save_folder, exist_ok=True)

        with open(save_to_file, "w", encoding="utf-8") as f:
            f.write("import dcs.planes as planes\n\n")
            f.write("planes_map = {\n")
            for unit_type, templates in plane_templates.items():
                f.write(f"    '{unit_type}': [\n")
                for template in templates:
                    f.write("        {\n")
                    f.write(f"            'type': planes.{template['type']},\n")
                    f.write(f"            'id': planes.{template['type']}.id,\n")
                    f.write(f"            'fuel': planes.{template['type']}.fuel_max,\n")
                    f.write(f"            'chaff': planes.{template['type']}.chaff,\n")
                    f.write(f"            'flare': planes.{template['type']}.flare,\n")
                    f.write("            'payload': {\n")
                    f.write("                'pylons': [\n")
                    for pylon in template["payload"]["pylons"]:
                        if pylon is None:
                            f.write("                    None,\n")
                        else:
                            f.write(f"                    {pylon},\n")
                    f.write("                ]\n")
                    f.write("            }\n")
                    f.write("        },\n")
                f.write("    ],\n")
            f.write("}\n")
        print(f"✅ Plane templates saved to {save_to_file}")

    return plane_templates



# Extracts helo loadouts from mission data

def generate_helicopter_templates_from_mission(mission_data, mission_types=["cas", "sead", "strike"], save_to_file=None):
    helicopter_templates = {}

    for side in ["blue", "red"]:
        coalition = mission_data.get("coalition", {}).get(side, {})
        countries = coalition.get("country", {})

        for _, country in countries.items():
            groups = country.get("helicopter", {}).get("group", {})

            for _, group in groups.items():
                group_name = group.get("name", "").lower()

                matched_mission = None
                for mtype in mission_types:
                    if mtype in group_name:
                        matched_mission = mtype
                        break

                if matched_mission:
                    for _, unit in group.get("units", {}).items():
                        if unit.get("skill", "").lower() == "client":
                            continue  # skip client slots

                        unit_type = unit.get("type")
                        if not unit_type:
                            continue

                        # Try finding helicopter class
                        heli_class = getattr(helicopters, unit_type, None)
                        if heli_class is None:
                            fixed_unit_type = unit_type.replace("-", "_")
                            heli_class = getattr(helicopters, fixed_unit_type, None)

                        if heli_class is None:
                            continue  # skip unknown helis

                        # Now extract pylons
                        pylons_data = unit.get("payload", {}).get("pylons", {})
                        pylons_list = []

                        if pylons_data:
                            sample_key = next(iter(pylons_data.keys()))
                            key_is_str = isinstance(sample_key, str)
                            max_pylon = max(int(k) if isinstance(k, str) else k for k in pylons_data.keys())
                        else:
                            key_is_str = True
                            max_pylon = 0

                        for pylon_index in range(1, max_pylon + 1):
                            key = str(pylon_index) if key_is_str else pylon_index
                            pylon_info = pylons_data.get(key)

                            if pylon_info is None:
                                pylons_list.append(None)
                            else:
                                clsid = pylon_info.get("CLSID")
                                if clsid:
                                    # Match inside PylonX only
                                    pylon_attr = f"Pylon{pylon_index}"
                                    pylon_class = getattr(heli_class, pylon_attr, None)

                                    matched_reference = None
                                    if pylon_class and isinstance(pylon_class, type):
                                        for weapon_attr in dir(pylon_class):
                                            weapon = getattr(pylon_class, weapon_attr)
                                            if isinstance(weapon, tuple) and len(weapon) == 2:
                                                weapon_data = weapon[1]
                                                if weapon_data.get("clsid", "").strip() == clsid:
                                                    matched_reference = f"helicopters.{unit_type}.{pylon_attr}.{weapon_attr}"
                                                    break

                                    if matched_reference:
                                        pylons_list.append(matched_reference)
                                    else:
                                        pylons_list.append(None)
                                else:
                                    pylons_list.append(None)

                        # Detect optional fields
                        fuel = unit.get("fuel", None)
                        chaff = unit.get("chaff", None)
                        flare = unit.get("flare", None)

                        # Build the template
                        template = {
                            "type": heli_class,
                            "payload": {
                                "pylons": pylons_list
                            }
                        }
                        if fuel:
                            template["fuel"] = fuel
                        if chaff:
                            template["chaff"] = chaff
                        if flare:
                            template["flare"] = flare

                        if unit_type not in helicopter_templates:
                            helicopter_templates[unit_type] = []
                        helicopter_templates[unit_type].append(template)

    # De-duplicate templates
    for unit_type, templates in helicopter_templates.items():
        unique_templates = []
        seen_signatures = set()

        for template in templates:
            pylons_signature = tuple(template["payload"]["pylons"])
            if pylons_signature not in seen_signatures:
                seen_signatures.add(pylons_signature)
                unique_templates.append(template)

        helicopter_templates[unit_type] = unique_templates

    if save_to_file:
        with open(save_to_file, "w", encoding="utf-8") as f:
            f.write("helicopters = ")
            f.write(pprint.pformat(helicopter_templates, width=140))
        print(f"✅ Helicopter templates saved to {save_to_file}")

    return helicopter_templates

# Extract liveries

def generate_livery_maps_from_mission(mission_data, save_to_folder=None):
    blue_map = {}
    red_map = {}

    for side in ["blue", "red"]:
        coalition = mission_data.get("coalition", {}).get(side, {})
        countries = coalition.get("country", {})

        for _, country in countries.items():
            for category in ["plane", "helicopter"]:
                groups = country.get(category, {}).get("group", {})

                for _, group in groups.items():
                    for _, unit in group.get("units", {}).items():
                        if unit.get("skill", "").lower() == "client":
                            continue  # skip client slots

                        unit_type = unit.get("type")
                        livery_id = unit.get("livery_id")

                        if not unit_type or not livery_id:
                            continue

                        target_map = blue_map if side == "blue" else red_map

                        if unit_type not in target_map:
                            target_map[unit_type] = []

                        if livery_id not in target_map[unit_type]:
                            target_map[unit_type].append(livery_id)

    if save_to_folder:
        os.makedirs(save_to_folder, exist_ok=True)

        blue_file = os.path.join(save_to_folder, "blue_liveries.py")
        red_file = os.path.join(save_to_folder, "red_liveries.py")

        with open(blue_file, "w", encoding="utf-8") as f:
            f.write("blue_liveries = ")
            f.write(pprint.pformat(blue_map, width=140))

        with open(red_file, "w", encoding="utf-8") as f:
            f.write("red_liveries = ")
            f.write(pprint.pformat(red_map, width=140))

        print(f"✅ Blue liveries saved to {blue_file}")
        print(f"✅ Red liveries saved to {red_file}")

    return blue_map, red_map

# Ground Units

def generate_ground_templates_from_mission(mission_data, mission_types=["cas", "strike", "defense"], save_to_file=None):
    ground_templates = {}

    for side in ["blue", "red"]:
        coalition = mission_data.get("coalition", {}).get(side, {})
        countries = coalition.get("country", {})

        for _, country in countries.items():
            groups = country.get("vehicle", {}).get("group", {})

            for _, group in groups.items():
                group_name = group.get("name", "").lower()

                matched_mission = None
                for mtype in mission_types:
                    if mtype in group_name:
                        matched_mission = mtype
                        break

                if matched_mission:
                    unit_list = []
                    for _, unit in sorted(group.get("units", {}).items()):
                        unit_type = unit.get("type")
                        if not unit_type:
                            continue
                        unit_list.append(unit_type)

                    if unit_list:  # only add if non-empty
                        if matched_mission not in ground_templates:
                            ground_templates[matched_mission] = []
                        ground_templates[matched_mission].append(unit_list)

    if save_to_file:
        import os
        import pprint
        os.makedirs(os.path.dirname(save_to_file), exist_ok=True)
        with open(save_to_file, "w", encoding="utf-8") as f:
            f.write("ground_templates = ")
            f.write(pprint.pformat(ground_templates, width=140))
        print(f"✅ Ground templates saved to {save_to_file}")

    return ground_templates
