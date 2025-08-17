import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def draw_lens_diagram(axis_deg, distance_mm=60, center_thickness=2.0, edge_thickness=5.0):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-70, 70)
    ax.set_ylim(-70, 70)
    ax.axis('off')

    # レンズ外形（円）
    lens_radius = distance_mm / 2
    lens_circle = plt.Circle((0, 0), lens_radius, fill=False, linestyle='--', linewidth=1.5)
    ax.add_artist(lens_circle)

    # レンズ中心
    ax.plot(0, 0, 'ko', label='Lens Center')

    # 軸方向（青）
    axis_rad = np.radians(axis_deg)
    x_axis = lens_radius * np.cos(axis_rad)
    y_axis = lens_radius * np.sin(axis_rad)
    ax.arrow(0, 0, x_axis, y_axis, head_width=3, color='blue', label='Axis Direction')
    ax.text(x_axis * 1.1, y_axis * 1.1, f"Axis {axis_deg}°", color='blue')

    # 厚み方向（赤）＝軸に垂直
    perp_rad = axis_rad + np.pi / 2
    x_thick = lens_radius * np.cos(perp_rad)
    y_thick = lens_radius * np.sin(perp_rad)
    ax.arrow(0, 0, x_thick, y_thick, head_width=3, color='red', label='Max Thickness Direction')
    ax.text(x_thick * 1.1, y_thick * 1.1, "Max Thickness", color='red')

    # 周辺厚の可視化（赤い線）
    edge_x = x_thick
    edge_y = y_thick
    ax.plot([edge_x, edge_x], [edge_y, edge_y + edge_thickness * 5], color='red', linewidth=2)
    ax.text(edge_x, edge_y + edge_thickness * 5 + 2, f"Edge Thickness ≈ {edge_thickness}mm", color='red', ha='center')

    # 中心厚の可視化（黒い線）
    ax.plot([0, 0], [0, center_thickness * 5], color='black', linewidth=2)
    ax.text(0, center_thickness * 5 + 2, f"Center Thickness ≈ {center_thickness}mm", color='black', ha='center')

    st.pyplot(fig)
