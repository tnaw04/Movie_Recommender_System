import streamlit as st
import pandas as pd

# Tiêu đề trang web
st.title("Demo Hệ thống Gợi ý Phim")

# Hiển thị text
st.write("Xin chào! Đây là bước khởi đầu cho đồ án Final Project.")

# Thử tạo một nút bấm
if st.button('Bấm vào đây thử xem'):
    st.success('Bạn đã cài đặt Streamlit thành công! Hệ thống sẵn sàng code tiếp.')