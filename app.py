
import streamlit as st
import pandas as pd

st.set_page_config(page_title="힐스 위험성평가 설문", layout="wide")

st.image("logo.png", width=200)
st.title("힐스 위험성평가 설문 시스템 (WORK TALK)")
st.markdown("사진 1장당 질문 4개를 입력해주세요. 여러 장도 업로드 가능합니다.")

uploaded_photos = st.file_uploader("📸 작업 사진을 업로드하세요", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_photos:
    for idx, photo in enumerate(uploaded_photos):
        st.subheader(f"📷 사진 {idx+1}")
        st.image(photo, width=300)
        st.text_input(f"1. 어떤 작업을 하고 있는 건가요? (사진 {idx+1})", key=f"q1_{idx}")
        st.text_input(f"2. 이 작업은 왜 위험하다고 생각하나요? (사진 {idx+1})", key=f"q2_{idx}")
        st.selectbox(f"3. 이 작업은 얼마나 자주 하나요? (사진 {idx+1})",
                     ["연 1-2회", "반기 1-2회", "월 2-3회", "주 1회 이상", "매일"],
                     key=f"q3_{idx}")
        st.selectbox(f"4. 이 작업은 얼마나 위험하다고 생각하나요? (사진 {idx+1})",
                     ["약간의 위험: 일회용 밴드 치료 필요 가능성 있음",
                      "조금 위험: 병원 치료 필요. 1-2일 치료 및 휴식",
                      "위험: 보름 이상의 휴식이 필요한 중상 가능성 있음",
                      "매우 위험: 불가역적 장애 또는 사망 가능성 있음"],
                     key=f"q4_{idx}")

st.success("설문 작성 테스트용 기본 앱입니다.")
