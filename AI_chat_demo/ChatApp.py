import os
import streamlit as st
from volcenginesdkarkruntime import Ark

# 初始化 Ark 客户端
client = Ark(api_key=os.environ.get("ARK_API_KEY"))

st.title("Leon的AI助手")

# 读取文件内容作为 system content
with open("xiaohongshu_prompt.txt", "r", encoding="utf-8") as file:
    system_content = file.read()

# 保存对话历史
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_content}
    ]

# 用户输入
user_input = st.text_input("请输入你的问题：")

if st.button("发送"):
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # 调用大模型接口
        completion = client.chat.completions.create(
            model="ep-20241130154059-sj7ld",
            messages=st.session_state.messages,
        )
        reply = completion.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

    # 显示对话内容
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"**用户：** {message['content']}")
        elif message["role"] == "assistant":
            st.markdown(f"**助手：** {message['content']}")