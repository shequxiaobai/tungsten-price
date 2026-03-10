# 钨钢棒料价格计算器 - 网页版(Mac专用)
import datetime
import streamlit as st
import pandas as pd

# 配置
BASE_DIAMETER = 3.0
MAX_DIAMETER = 34.5
DIAMETER_STEP = 0.5
FIXED_LENGTH = 330
BASE_PRICE_3MM = 148.42

# 生成直径列表
def get_diameters():
    d_list = []
    current = BASE_DIAMETER
    while current <= MAX_DIAMETER + 0.001:
        d_list.append(round(current, 1))
        current += DIAMETER_STEP
    return d_list

# 计算单价基准
def get_price_per_mm3():
    r = 3.0 / 2
    v = 3.1415926535 * r**2 * FIXED_LENGTH
    return BASE_PRICE_3MM / v

# 计算所有价格
def calc_all_prices():
    ppm3 = get_price_per_mm3()
    diameters = get_diameters()
    prices = {}
    for d in diameters:
        r = d / 2
        v = 3.1415926535 * r**2 * FIXED_LENGTH
        prices[d] = round(v * ppm3, 2)
    return prices

# 网页界面
def main():
    st.set_page_config(page_title="钨钢价格", page_icon="📏")
    st.title("📏 钨钢合金棒料价格计算器")

    prices = calc_all_prices()
    today = datetime.date.today()

    with st.sidebar:
        st.header("查价格")
        d = st.selectbox("直径(mm)", get_diameters())
        if st.button("查询"):
            st.success(f"Φ{d}mm × 330mm\n含税价：{prices[d]} 元")

    st.subheader(f"{today} 全部价格表")
    df = pd.DataFrame({
        "直径(mm)": list(prices.keys()),
        "含税价格(元)": list(prices.values())
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

if __name__ == "__main__":
    main()