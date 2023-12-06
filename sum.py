import streamlit as st
import openai

def askGPT(prompt, apiKey):
    client = openai.OpenAI(api_key=apiKey)
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}]
    )
    finalResponse = response.choices[0].message.content
    return finalResponse

def main():
    st.set_page_config(page_title="요약 프로그램")

    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    with st.sidebar:
        open_apiKey = st.text_input(label='OPEN API 키', placeholder='enter your api key')

    if open_apiKey:
        st.session_state["OPENAI_API"] = open_apiKey

    st.markdown('---')
    st.header("요약프로그램")
    st.markdown('---')

    text = st.text_area("요약 할 글을 입력하세요")

    if st.button("요약"):
        prompt = f'''
            **Instructions** :
            - You are an expert assistant that summarizes text into **Korean language**.
            - Your task is to summarize the **text** sentences in **Korean language**.
            - Your summaries should include the following :
                - Omit duplicate content, but increase the summary weight of duplicate content.
                - Summarize by emphasizing concepts and arguments rather than case evidence.
                - Summarize in 3 lines.
                - Use the format of a bullet point.
            -text : {text}
        '''
        st.info(askGPT(prompt, st.session_state["OPENAI_API"]))

if __name__ == "__main__":
    main()