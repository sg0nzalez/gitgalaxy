import re
import math
import hashlib
import logging
import time
from typing import Dict, List, Any, TypedDict, Optional, Tuple


class Cartographer:
    """
    Transforms a flat list of files into a deterministic 3D star map 
    following a "Fractal Fibonacci" pattern. 
    
    Groups files into Constellations (folders) and orbits them around the 
    heavy "Sun" (God Object) of each sector while maintaining satellite clearance.
    """
    
    def __init__(self, parent_logger: Optional[logging.Logger] = None):
        # --- TELEMETRY SYNC ---
        if parent_logger:
            self.logger = parent_logger.getChild("cartographer")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("cartographer")
            self.logger.setLevel(logging.INFO)

        # --- SPATIAL CONSTANTS ---
        # Micro Angle: Stars within folders follow the classic Golden Angle
        self.MICRO_GOLDEN_ANGLE = math.pi * (3.0 - math.sqrt(5.0))  # ~2.39996 rad (~137.5 deg)
        
        # Macro Angle: Constellations follow the user-tuned 92.4 degree step
        self.MACRO_GOLDEN_ANGLE = math.radians(92.4) 
        
        # Base expansion multipliers
        self.MICRO_SPACING = 250.0   # Internal planet-to-planet density baseline
        self.MACRO_STEP_FACTOR = 1.5 # Inter-galaxy step multiplier (Center-to-Center)
        self.MAX_TILT_DEG = 15.0     # Max degrees a constellation can tilt from horizontal plane
        self.CORE_EXCLUSION_RADIUS = 600.0 # Clear center zone
        self.JITTER_MAGNITUDE = 100


    def _calculate_orbit_footprint(self, mass: float) -> float:
        """Determines the required tight clearance radius for a star based on mass."""
        visual_radius = 10 + (math.pow(max(mass, 1), 1/3) * 2) 
        clearance = 40 + (math.log2(max(mass, 2)) * 5)
        
        # Removed the p_scalar multiplier. 
        # Micro-placement will now be tight, and macro WebGPU scaling is handled safely in map_galaxy.
        return visual_radius + clearance

    def _hash_jitter(self, seed: str, amplitude: float) -> float:
        """
        Applies a deterministic pseudo-random jitter based on a filename hash.
        Ensures the same codebase generates the exact same geometry every time.
        """
        if not seed:
            return 0.0
        h = int(hashlib.md5(seed.encode('utf-8')).hexdigest()[:8], 16)
        # Map 0-0xffffffff to a normalized range of -1.0 to 1.0
        normalized = (h / 0xffffffff) * 2.0 - 1.0
        return normalized * amplitude


    def map_galaxy(self, stars: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Injects 3D coordinates using a Ray-Casting Dynamic Mask.
        Ensures galaxies wrap around previous turns of the spiral by measuring
        all previously placed obstruction circles.
        """
        if not stars:
            return []

        self.logger.info(f"Cartographer: Executing Ray-Casting Dynamic Mask packing for {len(stars)} bodies...")

        # 1. Sectorization
        sectors: Dict[str, List[Dict[str, Any]]] = {}
        for star in stars:
            path_str = star.get("path", star.get("filename", ""))
            parts = [p for p in path_str.replace("\\", "/").split("/") if p]
            sector_name = parts[0] if len(parts) > 1 else "__monolith__"
            if sector_name not in sectors: sectors[sector_name] = []
            sectors[sector_name].append(star)

        # 2. Hull Calculation (Unmodified - keeps internal spacing pure)
        sector_stats = []
        for name, items in sectors.items():
            items.sort(key=lambda x: self._get_mass(x), reverse=True)
            sun_mass = self._get_mass(items[0])
            sun_foot = self._calculate_orbit_footprint(sun_mass)
            hull_radius = sun_foot + (math.sqrt(len(items)) * self.MICRO_SPACING)
            sector_stats.append({"name": name, "stars": items, "radius": hull_radius})
            
        sector_stats.sort(key=lambda x: x["radius"], reverse=True)

        # 3. DYNAMIC MASK PLACEMENT (The Black Hole Anchor)
        if sector_stats:
            largest_folder_radius = sector_stats[0]["radius"]
            # Target 1/3 of the largest folder's base radius.
            black_hole_footprint = max(500.0, min(3000.0, largest_folder_radius / 3.0))
        else:
            black_hole_footprint = 1500.0
            
        self.logger.info(f"Setting dynamic Black Hole Exclusion Zone to {black_hole_footprint}")
        
        # Start our collision mask with ONLY the Black Hole
        placed_circles = [[0.0, 0.0, black_hole_footprint]] 

        current_angle = 0.0
        prev_radius = black_hole_footprint 
        prev_dist_from_center = 0.0

        for i, sec in enumerate(sector_stats):
            s_name = sec["name"]
            s_stars = sec["stars"]
            
            # *** THE FIX: Scale the folder footprint by 10 ONLY for Macro placement ***
            # This ensures folders clear each other in WebGPU, but leaves planets tightly packed.
            macro_sec_radius = sec["radius"] * 10.0

            if i == 0:
                # FIRST FOLDER: Sits on the edge of the Black Hole
                dist = black_hole_footprint + macro_sec_radius
                sec_x, sec_z = dist, 0.0
                current_angle = 0.0
                prev_dist_from_center = dist
            else:
                # Step A: Determine angular offset based on Hull-to-Hull link
                arc_step = (prev_radius + macro_sec_radius) * self.MACRO_STEP_FACTOR
                delta_theta = arc_step / max(prev_dist_from_center, 1.0)
                current_angle += delta_theta
                
                # Step B: Ray-Cast to determine distance
                cos_th = math.cos(current_angle)
                sin_th = math.sin(current_angle)
                
                max_r_intersect = black_hole_footprint
                
                for px, pz, pr in placed_circles:
                    b = -2 * (px * cos_th + pz * sin_th)
                    c = (px**2 + pz**2) - (pr * self.MACRO_STEP_FACTOR)**2
                    disc = b**2 - 4*c
                    
                    if disc >= 0:
                        r2 = (-b + math.sqrt(disc)) / 2.0
                        if r2 > max_r_intersect:
                            max_r_intersect = r2
                            
                # Lock position at furthest obstruction + its own scaled radius
                dist = max_r_intersect + macro_sec_radius
                sec_x = dist * cos_th
                sec_z = dist * sin_th
                prev_dist_from_center = dist

            # Add this scaled folder to the collision mask
            placed_circles.append([sec_x, sec_z, macro_sec_radius])

            # Macro Jitter & Tilt (Keep 2500.0 for deep 3D space effect)
            sec_y = self._hash_jitter(s_name, 2500.0)
            tilt_mag = math.radians(self._hash_jitter(s_name + "_tilt_mag", self.MAX_TILT_DEG))
            tilt_dir = math.radians((self._hash_jitter(s_name + "_tilt_dir", 0.5) + 0.5) * 360.0)

            # INTERNAL MICRO PLACEMENT (Untouched Original Logic)
            sun_mass = self._get_mass(s_stars[0])
            sun_foot = self._calculate_orbit_footprint(sun_mass)

            for j, star in enumerate(s_stars):
                f_name = star.get("name", star.get("filename", f"star_{j}"))
                if j == 0:
                    lx, ly, lz = 0.0, 0.0, 0.0
                else:
                    p_foot = self._calculate_orbit_footprint(self._get_mass(star))
                    local_r = sun_foot + p_foot + (math.sqrt(j) * self.MICRO_SPACING)
                    local_th = j * self.MICRO_GOLDEN_ANGLE
                    
                    bx, bz = local_r * math.cos(local_th), local_r * math.sin(local_th)
                    rot_x = bx * math.cos(tilt_dir) + bz * math.sin(tilt_dir)
                    rot_z = -bx * math.sin(tilt_dir) + bz * math.cos(tilt_dir)
                    tx, ty, tz = rot_x * math.cos(tilt_mag), rot_x * math.sin(tilt_mag), rot_z
                    lx = tx * math.cos(tilt_dir) - tz * math.sin(tilt_dir)
                    lz = tx * math.sin(tilt_dir) + tz * math.cos(tilt_dir)
                    ly = ty

                jit_x = self._hash_jitter(f_name + "_x", self.JITTER_MAGNITUDE )
                jit_y = self._hash_jitter(f_name + "_y", self.JITTER_MAGNITUDE )
                jit_z = self._hash_jitter(f_name + "_z", self.JITTER_MAGNITUDE * 4)

                star["pos_x"] = round(sec_x + lx + jit_x, 2)
                star["pos_y"] = round(sec_y + ly + jit_y, 2)
                star["pos_z"] = round(sec_z + lz + jit_z, 2)

                if "layout" not in star: star["layout"] = {}
                star["layout"]["x"], star["layout"]["y"], star["layout"]["z"] = star["pos_x"], star["pos_y"], star["pos_z"]

            prev_radius = macro_sec_radius

        return stars

    def _get_mass(self, star: Dict[str, Any]) -> float:
        """Safely extracts mass regardless of which JSON version the pipeline is using."""
        if "forensics" in star:
            return float(star["forensics"].get("structural_mass", 0.0))
        return float(star.get("file_impact", star.get("sum_fxn_impact", 0.0)))