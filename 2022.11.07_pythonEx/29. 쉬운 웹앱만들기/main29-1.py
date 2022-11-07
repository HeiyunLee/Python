# pip install streamlit -> 빠르고 쉽게 웹앱을 만들기 위한 라이브러리
#                       -> 설치 시 이메일 입력하는 부분이 나타나면 사용하는 이메일을 입력했을 때 업데이트 되는 내용을 이메일로 알려준다.
#                       -> 그런데 나는 설치 시 이메일 입력이 부분이 나타나지 않았음.
# pi install pyupbit -> 가상화폐 데이터를 조회활 수 있는 라이브러리

import streamlit as st

data_list = {5,5,6,6,7}
st.write('''
샘플데이터
''')

st.line_chart(data_list)