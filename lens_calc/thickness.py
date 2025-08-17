import math
#計算ロジック


def calculate_edge_thickness(sphere, cylinder, axis, distance_mm, refractive_index, center_thickness=2.0):
    axis_rad = math.radians(axis)
    cyl_contribution = cylinder * math.cos(axis_rad) ** 2
    effective_power = sphere + cyl_contribution
    edge_thickness = center_thickness + (effective_power * distance_mm ** 2) / (2000 * refractive_index)
    return round(edge_thickness, 2)
