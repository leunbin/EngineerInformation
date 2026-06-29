import streamlit as st
import random

quiz_bank = {
    # 여기 기존 quiz_bank 그대로 붙여넣기
     # 애자일
    "애자일(Agile) 방법론": "절차보다 사람 중심으로 변화에 유연하고 신속하게 적응하는 신속 적응형 경량 개발 방법론. 개발 기간이 짧고 폭포수 모델의 반대 개념",

    # 럼바우 데이터 모델링
    "객체 모델링(Object Modeling)": "시스템에서 요구하는 객체와 객체 간 관계를 정의하여 ER 다이어그램을 만드는 모델링. 객체 다이어그램을 활용",
    "동적 모델링(Dynamic Modeling)": "시간의 흐름에 따른 객체 간 제어 흐름과 동작 순서를 표현하는 모델링. 상태 다이어그램을 활용",
    "기능 모델링(Functional Modeling)": "프로세스의 자료 흐름 중심으로 처리 과정을 표현하는 모델링. 자료 흐름도(DFD)를 활용",

    # SOLID
    "SRP(단일 책임 원칙)": "하나의 클래스는 하나의 책임만 가져야 한다는 객체지향 설계 원칙",
    "OCP(개방-폐쇄 원칙)": "확장에는 열려 있고 변경에는 닫혀 있어야 한다는 객체지향 설계 원칙",
    "LSP(리스코프 치환 원칙)": "하위 클래스는 언제나 상위 클래스로 대체할 수 있어야 한다는 객체지향 설계 원칙",
    "ISP(인터페이스 분리 원칙)": "사용하지 않는 인터페이스는 구현하지 않아야 하며 기능별 인터페이스로 분리해야 한다는 원칙",
    "DIP(의존성 역전 원칙)": "구체 클래스가 아닌 추상에 의존하여 결합도를 낮추는 객체지향 설계 원칙",

    # 디자인 패턴 분류
    "생성 패턴": "객체 생성 방식과 캡슐화를 다루는 디자인 패턴",
    "구조 패턴": "클래스와 객체를 조합하여 더 큰 구조를 만드는 디자인 패턴",
    "행위 패턴": "객체 간 상호작용과 역할 분담을 다루는 디자인 패턴",

    # 생성 패턴
    "생성-Builder": "복잡한 객체를 단계적으로 조립하며 생성과 표현을 분리하는 패턴",
    "생성-Prototype": "원형 객체를 복사한 뒤 필요한 부분만 수정하여 사용하는 패턴",
    "생성-Factory Method": "상위 클래스에서 생성 인터페이스를 정의하고 하위 클래스에서 객체를 생성하는 패턴",
    "생성-Abstract Factory": "서로 관련된 객체들의 집합을 생성하는 인터페이스를 제공하는 패턴",
    "생성-Singleton": "클래스의 인스턴스를 하나만 생성하도록 제한하는 패턴",

    # 구조 패턴
    "구조-Bridge": "기능 계층과 구현 계층을 분리하여 연결하는 패턴",
    "구조-Decorator": "기존 객체에 기능을 동적으로 추가하는 패턴으로 상속의 대안",
    "구조-Facade": "복잡한 시스템을 단순한 인터페이스로 제공하는 패턴",
    "구조-Flyweight": "객체를 공유하여 메모리 사용량을 줄이는 경량화 패턴",
    "구조-Proxy": "실제 객체 대신 대리 객체를 두어 접근을 제어하는 패턴",
    "구조-Composite": "객체를 트리 구조로 구성하여 부분과 전체를 동일하게 처리하는 패턴",
    "구조-Adapter": "기존 클래스를 재사용할 수 있도록 인터페이스를 맞춰주는 패턴",

    # 행위 패턴
    "행위-Mediator": "중재자를 통해 객체 간 통신을 수행하여 결합도를 낮추는 패턴",
    "행위-Interpreter": "문법 규칙을 클래스로 구현하여 문장을 해석하는 패턴",
    "행위-Iterator": "컬렉션 내부 구조를 노출하지 않고 순차 접근을 제공하는 패턴",
    "행위-Template Method": "전체 알고리즘은 유지하면서 일부 단계만 하위 클래스에서 변경하는 패턴",
    "행위-Observer": "객체 상태가 변경되면 의존 객체들에게 자동으로 알리는 패턴",
    "행위-State": "객체 상태를 클래스로 분리하여 상태에 따라 행동이 달라지는 패턴",
    "행위-Visitor": "데이터 구조와 처리 기능을 분리하여 새로운 기능을 쉽게 추가하는 패턴",
    "행위-Command": "요청을 객체로 캡슐화하여 실행하는 패턴",
    "행위-Strategy": "알고리즘을 캡슐화하여 필요에 따라 교체할 수 있도록 하는 패턴",
    "행위-Memento": "객체의 이전 상태를 저장하고 복원하는 패턴(Undo)",
    "행위-Chain of Responsibility": "요청을 처리할 객체들을 체인 형태로 연결하여 처리하는 패턴",

    # 요구사항
    "기능 요구사항": "시스템이 제공해야 하는 기능과 서비스에 대한 요구사항",
    "비기능 요구사항": "성능, 보안, 품질 등 시스템 기능 이외의 제약사항에 대한 요구사항"
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

st.title("1단원-요구사항 확인")

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
