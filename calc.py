import streamlit as st
from lens_calc.thickness import calculate_edge_thickness

st.title("👓 コバ厚計算ツール")

# 入力フォーム
sphere = st.number_input("S度数（Sphere）", value=-4.00, step=0.25)
cylinder = st.number_input("C度数（Cylinder）", value=-1.50, step=0.25)
axis = st.slider("軸（Axis）", min_value=0, max_value=180, value=90)
distance = st.slider("中心からの距離（mm）", min_value=0.0, max_value=50.0, value=30.0, step=0.5)
refractive_index = st.selectbox("レンズの屈折率", options=[1.50, 1.60, 1.67, 1.74], index=1)
center_thickness = st.number_input("中心厚（mm）", value=2.0, step=0.1)

# 計算実行
if st.button("計算する"):
    edge = calculate_edge_thickness(sphere, cylinder, axis, distance, refractive_index, center_thickness)

    st.success(f"✅ コバ厚は **{edge} mm** です")


