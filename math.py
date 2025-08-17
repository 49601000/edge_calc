import math

def calculate_edge_thickness(sphere, cylinder, axis, distance_mm, refractive_index, center_thickness=2.0):
    # 軸をラジアンに変換
    axis_rad = math.radians(axis)
    
    # 円柱度数の軸方向寄与（近似）
    cyl_contribution = cylinder * math.cos(axis_rad) ** 2
    
    # 実効度数
    effective_power = sphere + cyl_contribution
    
    # 厚み計算（近似式）
    edge_thickness = center_thickness + (effective_power * distance_mm ** 2) / (2000 * refractive_index)
    
    return round(edge_thickness, 2)