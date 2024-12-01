import os
from volcenginesdkarkruntime import Ark

# 设置API Key
client = Ark(api_key=os.environ.get("055d8443-2a1e-4e9c-b82c-9abc67f6f435"))

print("----- multiple rounds request -----")
completion = client.chat.completions.create(
    model="ep-20241130154059-sj7ld",
    messages = [
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "花椰菜是什么？"},
        {"role": "assistant", "content": "花椰菜又称菜花、花菜，是一种常见的蔬菜。"},
        {"role": "user", "content": "再详细点"},
    ],
) 
print(completion.choices[0].message.content)


