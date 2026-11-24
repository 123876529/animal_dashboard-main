import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh
import random
import time

# 导入拆分出去的组件和配置
from components.render_table import render_html_table
from components.css_style import LIGHT_CSS, DARK_CSS
from config import IUCN_ORDER, COLOR_MAP_DARK, COLOR_MAP_LIGHT

# ================= 页面配置与基础设置 =================
st.set_page_config(page_title="动物百科监控大屏", layout="wide", initial_sidebar_state="expanded")

# 加载基础浅色CSS
st.markdown(LIGHT_CSS, unsafe_allow_html=True)

# ================= 侧边栏控制 =================
st.sidebar.header("⚙️ 监控与显示设置")
realtime_mode = st.sidebar.checkbox("📡 开启实时数据监控", value=False)
if realtime_mode:
    st_autorefresh(interval=2000, key="realtime_refresh")
    st.sidebar.success("实时监控中...")

dark_mode = st.sidebar.checkbox("🌌 炫酷蓝大屏模式", value=False)
if dark_mode:
    st.markdown(DARK_CSS, unsafe_allow_html=True)

auto_carousel = st.sidebar.checkbox("🎞️ 开启详情自动轮播", value=False)

st.sidebar.markdown("---")
st.sidebar.header("数据筛选")

@st.cache_data
def load_data():
    return pd.read_csv("data/animals.csv")

if realtime_mode:
    df = load_data()
    df.loc[df["iucn_level"].isin(["极危", "濒危", "易危"]), "iucn_level"] = df[df["iucn_level"].isin(["极危", "濒危", "易危"])]["iucn_level"].apply(
        lambda x: x if random.random() > 0.1 else random.choice(["极危", "濒危", "易危", "近危"])
    )
else:
    df = load_data()

search_query = st.sidebar.text_input("🔍 搜索动物名称/学名", "")
class_list = ["全部"] + list(df["class_name"].unique())
selected_class = st.sidebar.selectbox("选择纲目", class_list)
iucn_list = ["全部"] + list(df["iucn_level"].unique())
selected_iucn = st.sidebar.selectbox("选择IUCN等级", iucn_list)

filtered_df = df.copy()
if search_query:
    filtered_df = filtered_df[filtered_df["chinese_name"].str.contains(search_query) | filtered_df["scientific_name"].str.contains(search_query, case=False)]
if selected_class != "全部":
    filtered_df = filtered_df[filtered_df["class_name"] == selected_class]
if selected_iucn != "全部":
    filtered_df = filtered_df[filtered_df["iucn_level"] == selected_iucn]

if filtered_df.empty:
    st.warning("没有找到符合条件的动物数据，请调整筛选条件。")
    st.stop()

# ================= 页面主内容 =================
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.title("🐾 动物百科实时监控看板")
st.markdown("探索动物分类、濒危等级与栖息地分布")

threatened_species = len(filtered_df[filtered_df["iucn_level"].isin(["极危", "濒危", "易危"])])
if threatened_species > 50:
    st.error("🚨 **实时预警**：受威胁物种数已超过 50 种，请立即关注！")

st.markdown("### 📊 核心数据概览")
col1, col2, col3, col4 = st.columns(4)

total_species = len(filtered_df)
families = filtered_df["family_name"].nunique()
avg_lifespan = round(filtered_df["lifespan_years"].mean(), 1)

col1.metric("物种总数", f"{total_species} 种")
if threatened_species > 50:
    with col2:
        st.metric("受威胁物种数", f"{threatened_species} 种", delta="超限", delta_color="inverse")
        st.markdown(f"<div class='alert-text'>🚨 达 {threatened_species} 种！</div>", unsafe_allow_html=True)
else:
    col2.metric("受威胁物种数", f"{threatened_species} 种")

col3.metric("科属数量", f"{families} 科")
col4.metric("平均寿命", f"{avg_lifespan} 年")

st.markdown("<br>", unsafe_allow_html=True)

# ================= 图表通用配置 =================
chart_bg = 'rgba(0,0,0,0)'
chart_font_color = '#E2E8F0' if dark_mode else '#2C3E2D'
chart_grid_color = '#1E293B' if dark_mode else '#F0F0F0'

chart_layout = dict(
    plot_bgcolor=chart_bg, paper_bgcolor=chart_bg,
    margin=dict(t=50, b=30, l=20, r=10),
    font=dict(color=chart_font_color),
    title_font=dict(color=chart_font_color),
    legend_font=dict(color=chart_font_color)
)

bar_color_seq = px.colors.sequential.Blues_r if dark_mode else px.colors.sequential.Greens_r
habitat_color_seq = px.colors.sequential.Purples_r if dark_mode else px.colors.qualitative.Set2

# ================= 维度统计区 =================
st.markdown("### 📈 维度统计")
row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    class_counts = filtered_df["class_name"].value_counts().reset_index()
    class_counts.columns = ["纲", "数量"]
    fig_bar = px.bar(class_counts, x="纲", y="数量", title="各纲物种数量对比", color="纲", color_discrete_sequence=bar_color_seq)
    fig_bar.update_layout(**chart_layout)
    fig_bar.update_layout(legend=dict(orientation="v", yanchor="top", y=0.98, xanchor="left", x=1.02, font=dict(size=12)))
    fig_bar.update_xaxes(showgrid=True, gridcolor=chart_grid_color)
    fig_bar.update_yaxes(showgrid=True, gridcolor=chart_grid_color)
    st.plotly_chart(fig_bar, use_container_width=True)

with row2_col2:
    iucn_counts = filtered_df["iucn_level"].value_counts().reindex(IUCN_ORDER).dropna().reset_index()
    iucn_counts.columns = ["等级", "数量"]
    color_map = COLOR_MAP_DARK if dark_mode else COLOR_MAP_LIGHT

    fig_pie = px.pie(iucn_counts, names="等级", values="数量", hole=0.6, title="IUCN 濒危等级占比", color="等级", color_discrete_map=color_map)
    fig_pie.update_layout(**chart_layout)
    fig_pie.update_layout(legend=dict(orientation="v", yanchor="top", y=0.98, xanchor="left", x=1.02, font=dict(size=12)))
    st.plotly_chart(fig_pie, use_container_width=True)

with row2_col3:
    habitat_counts = filtered_df["habitat"].value_counts().reset_index()
    habitat_counts.columns = ["栖息地", "数量"]
    fig_habitat = px.bar(habitat_counts, x="数量", y="栖息地", orientation='h', title="栖息地分布情况", color="栖息地", color_discrete_sequence=habitat_color_seq)
    fig_habitat.update_layout(**chart_layout)
    fig_habitat.update_layout(legend=dict(orientation="v", yanchor="top", y=0.98, xanchor="left", x=1.02, font=dict(size=12)))
    fig_habitat.update_xaxes(showgrid=True, gridcolor=chart_grid_color)
    fig_habitat.update_yaxes(showgrid=True, gridcolor=chart_grid_color)
    st.plotly_chart(fig_habitat, use_container_width=True)

# ================= 趋势分析区 (核心优化) =================
st.markdown("### 📉 数据分析")
row3_col1, row3_col2 = st.columns([7, 3])

with row3_col1:
    st.markdown("#### 体重与寿命关系散点图")
with row3_col2:
    st.markdown("#### 🏆 寿命最长 Top 5")

with row3_col1:
    fig_scatter = px.scatter(filtered_df, x="weight_kg", y="lifespan_years", color="class_name", hover_name="chinese_name",
                             labels={"weight_kg": "体重 (kg)", "lifespan_years": "寿命 (年)", "class_name": "纲"})

    chart_layout_scatter = chart_layout.copy()
    chart_layout_scatter['margin'] = dict(t=10, b=30, l=20, r=10)

    fig_scatter.update_layout(**chart_layout_scatter)
    fig_scatter.update_layout(
        legend=dict(orientation="v", yanchor="top", y=0.98, xanchor="left", x=1.0, font=dict(size=13), itemwidth=30)
    )
    fig_scatter.update_xaxes(showgrid=True, gridcolor=chart_grid_color)
    fig_scatter.update_yaxes(showgrid=True, gridcolor=chart_grid_color)
    st.plotly_chart(fig_scatter, use_container_width=True)

with row3_col2:
    top5 = filtered_df.nlargest(5, "lifespan_years")[["chinese_name", "lifespan_years"]].copy()
    top5.columns = ["动物名称", "寿命 (年)"]
    st.markdown(render_html_table(top5, is_dark=dark_mode), unsafe_allow_html=True)

# ================= 明细数据区 =================
row4_col1, row4_spacer, row4_col2 = st.columns([6, 0.2, 3.8])

with row4_col1:
    st.markdown("### 📋 物种明细")
    detail_df = filtered_df[["chinese_name", "scientific_name", "class_name", "iucn_level", "habitat"]].copy()
    detail_df.columns = ["中文名", "学名", "纲目", "濒危等级", "栖息地"]
    st.markdown(render_html_table(detail_df.head(15), is_dark=dark_mode), unsafe_allow_html=True)
    st.caption("注：仅展示前 15 条数据，可通过侧边栏筛选查看更多。")

with row4_col2:
    st.markdown("### 🔍 物种详情卡")
    animal_names = filtered_df["chinese_name"].tolist()

    if auto_carousel:
        current_index = int(time.time() / 2) % len(animal_names)
        selected_animal = animal_names[current_index]
        st.info(f"🎞️ 自动轮播中：当前展示 **{selected_animal}**")
    else:
        selected_animal = st.selectbox("选择物种", animal_names, label_visibility="collapsed")

    if selected_animal:
        animal_info = filtered_df[filtered_df["chinese_name"] == selected_animal].iloc[0]

        if dark_mode:
            detail_html = f"""
            <div class="detail-card">
                <h3 style="margin-top:0; color:#00E5FF !important;">{animal_info['chinese_name']} <span style="font-size:16px; color:#94A3B8 !important; font-weight:normal;">({animal_info['english_name']})</span></h3>
                <p><strong>学名：</strong> <i style="color:#E2E8F0 !important;">{animal_info['scientific_name']}</i></p>
                <p><strong>分类：</strong> <span style="color:#E2E8F0 !important;">{animal_info['class_name']} > {animal_info['order_name']} > {animal_info['family_name']}</span></p>
                <p><strong>IUCN等级：</strong> <span style="color:#38BDF8 !important; font-weight:bold;">{animal_info['iucn_level']}</span></p>
                <p><strong>分布地区：</strong> <span style="color:#E2E8F0 !important;">{animal_info['region']}</span></p>
                <p><strong>食性：</strong> <span style="color:#E2E8F0 !important;">{animal_info['diet']}</span></p>
                <p><strong>体型：</strong> <span style="color:#E2E8F0 !important;">体长 {animal_info['body_length_m']} 米，体重 {animal_info['weight_kg']} 千克</span></p>
                <p style="margin-bottom:0;"><strong>简介：</strong> <span style="color:#E2E8F0 !important;">{animal_info['description']}</span></p>
            </div>
            """
            st.markdown(detail_html, unsafe_allow_html=True)
        else:
            st.info(f"**{animal_info['chinese_name']}** ({animal_info['english_name']})")
            st.write(f"**学名**：*{animal_info['scientific_name']}*")
            st.write(f"**分类**：{animal_info['class_name']} > {animal_info['order_name']} > {animal_info['family_name']}")
            st.write(f"**IUCN等级**：{animal_info['iucn_level']}")
            st.write(f"**分布地区**：{animal_info['region']}")
            st.write(f"**食性**：{animal_info['diet']}")
            st.write(f"**体型**：体长 {animal_info['body_length_m']} 米，体重 {animal_info['weight_kg']} 千克")
            st.write(f"**简介**：{animal_info['description']}")

st.markdown('</div>', unsafe_allow_html=True)

# ================= 数据导出 =================
st.markdown("---")
st.markdown("### 📥 数据导出")
csv = filtered_df.to_csv(index=False).encode('utf-8-sig')
st.download_button(label="下载当前筛选的动物数据 (CSV)", data=csv, file_name='filtered_animals.csv', mime='text/csv')
