import streamlit as st
from lens_calc import calculate_edge_thickness
st.header("👓 コバ厚計算ツール")

axis = st.slider("軸角度（°）", 0, 180, 90)
distance = st.number_input("レンズ径（mm）", value=60)
sphere = st.number_input("球面度数（D）", value=-4.0)
cylinder = st.number_input("円柱度数（D）", value=-1.5)
refractive_index = st.number_input("屈折率", value=1.60)
center_thickness = st.number_input("中心厚（mm）", value=20.0)

edge_thickness = calculate_edge_thickness(
    sphere, cylinder, axis, distance, refractive_index, center_thickness
)

# 計算実行
if st.button("計算する"):
    edge = calculate_edge_thickness(sphere, cylinder, axis, distance, refractive_index, center_thickness)
    st.success(f"✅ コバ厚は **{edge} mm** です")

