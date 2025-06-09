
import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="출선종료 예측 계산기", page_icon="🧮", layout="centered")

st.title("🧮 출선종료 예측 계산기")

st.markdown("이 계산기는 고로 출선작업에서 종료 시점을 예측합니다.")

# 사용자 입력
total_output = st.number_input("총 출선 예상량 (ton)", min_value=0.0, value=300.0, step=10.0)
current_output = st.number_input("현재까지 출선된 양 (ton)", min_value=0.0, value=180.0, step=10.0)
rate = st.number_input("출선 속도 (ton/min)", min_value=0.1, value=10.0, step=0.1)
current_time_str = st.text_input("현재 시간 (HH:MM)", value="09:00")

# 계산
if st.button("출선 종료 시점 예측하기"):
    try:
        remaining = total_output - current_output
        time_needed_min = remaining / rate
        current_time = datetime.strptime(current_time_str, "%H:%M")
        predicted_end = current_time + timedelta(minutes=time_needed_min)
        result_time = predicted_end.strftime("%H:%M")
        st.success(f"✅ 예상 출선 종료 시각: **{result_time}**")
    except Exception as e:
        st.error(f"입력 값 오류: {e}")
