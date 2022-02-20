from nbformat import write
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('アプリケーション')

loading_text = st.empty()
bar = st.progress(0)

for i in range(100):
    loading_text.text('Loading...')
    bar.progress(i + 1)
    time.sleep(0.05)

left, right = st.columns(2)
button = left.button('右に文字表示')

if button:
    right.write('ボタンが押されました。')

st.write('よくある質問')
with st.expander('新規登録の方法'):
    st.write('新規登録の回答')
with st.expander('パスワードの消し方'):
    st.write('消し方の回答')


# option = st.text_input('あなたの趣味を教えてください。')
# 'あなたの好きな趣味は', option, 'です'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの好きな趣味は', condition, 'です'


# if st.checkbox('Show Image'):
#     img = Image.open('xviiizz-3b_tjW24pDk-unsplash.jpg')
#     st.image(img, caption='sample', use_column_width=True)
