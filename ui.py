import streamlit
from openai import OpenAI

key="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"

def checkAns(q):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=key,
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="deepseek/deepseek-r1-zero:free",
    messages=[
        {
        "role": "user",
        "content": q
        }
    ]
    )
    return completion.choices[0].message.content

streamlit.header("GNA DeepSeek Model")

a=streamlit.text_input("Enter your Question here ")

btn= streamlit.button("Check Answer") 
if btn:
    ans=checkAns(a)   
    streamlit.write(ans)