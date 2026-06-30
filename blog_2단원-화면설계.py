import streamlit as st
import random

quiz_bank = {

    # 애자일
    "UI 유형-CLI": "명령어를 텍스트로 입력하여 조작하는 정적인 텍스트 기반 사용자 인터페이스",
    "UI 유형-GUI": "그래픽 환경을 기반으로 마우스나 전자펜 등을 이용하는 그래픽 기반 사용자 인터페이스",
    "UI 유형-NUI": "키보드나 마우스 없이 터치, 음성, 신체 동작 등을 이용하는 직관적 사용자 인터페이스",
    "UI 유형-OUI": "현실의 모든 사물이 입출력 장치가 될 수 있는 유기적 상호작용 기반 사용자 인터페이스",

    # UI 설계 원칙
    "UI 설계 원칙-직관성": "누구나 쉽게 이해하고 사용할 수 있도록 설계하는 원칙",
    "UI 설계 원칙-유효성": "정확하고 완벽하게 사용자의 목표를 달성할 수 있도록 설계하는 원칙",
    "UI 설계 원칙-학습성": "초보자와 숙련자 모두 쉽게 배우고 사용할 수 있도록 설계하는 원칙",
    "UI 설계 원칙-유연성": "사용자의 요구사항을 최대한 수용하고 실수를 방지할 수 있도록 설계하는 원칙",

    # UML 분류
    "UML-구조적 다이어그램": "시스템의 정적인 구조를 표현하는 UML 다이어그램",
    "UML-행위적 다이어그램": "시스템의 동작과 객체 간 상호작용을 표현하는 UML 다이어그램",

    # 구조적 다이어그램
    "구조적 다이어그램-클래스 다이어그램": "클래스의 속성, 연산 및 클래스 간 정적인 관계를 표현하는 다이어그램",
    "구조적 다이어그램-객체 다이어그램": "특정 시점의 객체(인스턴스)와 객체 간 관계를 표현하는 다이어그램",
    "구조적 다이어그램-컴포넌트 다이어그램": "시스템을 구성하는 컴포넌트와 컴포넌트 간 의존 관계를 표현하는 다이어그램",
    "구조적 다이어그램-배치 다이어그램": "물리적 요소의 배치와 컴포넌트 간 종속성을 표현하는 다이어그램",
    "구조적 다이어그램-복합체 구조 다이어그램": "클래스나 컴포넌트의 내부 복합 구조를 표현하는 다이어그램",
    "구조적 다이어그램-패키지 다이어그램": "유스케이스나 클래스 등을 그룹화한 패키지 간 관계를 표현하는 다이어그램",

    # 행위적 다이어그램
    "행위적 다이어그램-유스케이스 다이어그램": "사용자 관점에서 시스템의 기능과 외부 요소를 표현하는 다이어그램",
    "행위적 다이어그램-시퀀스 다이어그램": "객체 간 메시지 흐름을 시간 순서에 따라 표현하는 다이어그램",
    "행위적 다이어그램-커뮤니케이션 다이어그램": "객체 간 메시지와 객체 사이의 연관 관계를 표현하는 다이어그램",
    "행위적 다이어그램-상태 다이어그램": "객체의 상태 변화와 상태에 따른 동작을 표현하는 다이어그램",
    "행위적 다이어그램-활동 다이어그램": "기능 수행 절차와 처리 흐름을 순서대로 표현하는 다이어그램",
    "행위적 다이어그램-타이밍 다이어그램": "객체의 상태 변화와 시간 제약을 표현하는 다이어그램",
}

# ----------------------------
# 최초 실행 시
# ----------------------------
if "questions" not in st.session_state:
    st.session_state.questions = list(quiz_bank.items())
    random.shuffle(st.session_state.questions)

    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.checked = False
    st.session_state.correct = False

st.set_page_config(
    page_title="정보처리기사 퀴즈",
    page_icon="📚",
    layout="centered"
)

st.title("2단원-화면설계")

total = len(st.session_state.questions)
current = st.session_state.index

# ----------------------------
# 모두 끝난 경우
# ----------------------------
if current >= total:

    st.balloons()

    st.success(
        f"🎉 모든 문제를 완료했습니다!\n\n"
        f"점수 : {st.session_state.score} / {total}"
    )

    if st.button("🔄 다시 시작"):

        st.session_state.questions = list(quiz_bank.items())
        random.shuffle(st.session_state.questions)

        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.checked = False
        st.rerun()

    st.stop()

# ----------------------------
# 현재 문제
# ----------------------------

term, description = st.session_state.questions[current]

st.progress((current) / total)

st.write(f"### 문제 {current+1} / {total}")

st.info(description)

# ----------------------------
# 정답 확인
# ----------------------------

if not st.session_state.checked:

    with st.form(key=f"quiz_form_{current}", clear_on_submit=False):

        answer = st.text_input(
            "정답을 입력하세요",
            key=f"answer_{current}",
            placeholder="정답을 입력 후 Enter를 누르세요."
        )

        submitted = st.form_submit_button("정답 확인")

    if submitted:

        st.session_state.checked = True

        correct = term.lower().replace(" ", "")
        user = answer.strip().lower().replace(" ", "")

        if user == correct:
            st.session_state.correct = True
            st.session_state.score += 1
        else:
            st.session_state.correct = False

        st.rerun()

# ----------------------------
# 결과 출력
# ----------------------------

else:

    if st.session_state.correct:

        st.success("정답입니다! 🎉")

    else:

        st.error(f"틀렸습니다.\n\n정답 : {term}")

    st.write(
        f"현재 점수 : **{st.session_state.score} / {current+1}**"
    )

    if st.button("➡ 다음 문제"):

        st.session_state.index += 1
        st.session_state.checked = False
        st.session_state.correct = False

        st.rerun()
