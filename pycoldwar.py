# pycoldwar.py
import os
import argparse
from dcs_util import (
    load_mission,
    extract_plane_templates,
    extract_ground_templates,
    extract_helicopter_templates,
    apply_sample_templates,
    apply_ground_templates,
    apply_helicopter_templates,
    save_modified_mission
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cold War Mission Converter")

    parser.add_argument("--mission_to_modify", "--mm", type=str, required=True,
                        help="Path to mission to modify (modern mission)")
    parser.add_argument("--coldwar_mission", "--cm", type=str, required=True,
                        help="Path to Cold War mission to extract templates from")
    parser.add_argument("--output_folder", "--op", type=str, required=True,
                        help="Path to output folder to save modified mission")

    parser.add_argument("--skip_planes", action="store_true", help="Skip modifying planes")
    parser.add_argument("--skip_ground", action="store_true", help="Skip modifying ground units")
    parser.add_argument("--skip_heli", action="store_true", help="Skip modifying helicopters")

    args = parser.parse_args()

    mission_to_modify_data, mission_to_modify_lua = load_mission(args.mission_to_modify)
    coldwar_mission_data, _ = load_mission(args.coldwar_mission)

    plane_mission_types = ['-sead-', '-patrol-', '-strike-', '-cas-']
    ground_mission_types = ['-supply-', '-assault-']
    heli_mission_types = ['-supply-', '-cas-']

    if not args.skip_planes:
        print("✈️ Extracting plane templates...")
        blue_map = extract_plane_templates(coldwar_mission_data, plane_mission_types, "blue")
        red_map = extract_plane_templates(coldwar_mission_data, plane_mission_types, "red")
    if not args.skip_ground:
        print("🚛 Extracting ground templates...")
        ground_map = extract_ground_templates(coldwar_mission_data, ground_mission_types)
    if not args.skip_heli:
        print("🚁 Extracting helicopter templates...")
        heli_map = extract_helicopter_templates(coldwar_mission_data, heli_mission_types)

    if not args.skip_planes:
        print("✈️ Applying plane templates...")
        apply_sample_templates(mission_to_modify_data, blue_map, red_map)
    if not args.skip_ground:
        print("🚛 Applying ground templates...")
        apply_ground_templates(mission_to_modify_data, ground_map)
    if not args.skip_heli:
        print("🚁 Applying helicopter templates...")
        apply_helicopter_templates(mission_to_modify_data, heli_map)

    os.makedirs(args.output_folder, exist_ok=True)
    output_mission_path = os.path.join(args.output_folder, "mission")
    save_modified_mission(mission_to_modify_data, output_mission_path)

    print(f"✅ All done! Modified mission saved to {output_mission_path}")