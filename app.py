import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'AI assistant interview', layout='centered')
st.title("AI Interview Assistant")
st.caption("Launched by ANUSHA")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title', ['Machine Learning Engineer','Senior Software','DevOPs Engineer','Data Analyst','Other'])
if role == 'Other':
  st.text_input('Enter you Job Title','XXXXXXX')
model = st.selectbox('Model', ['openai/gpt-oss-120b','openai/gpt-oss-20b'])
level = st.selectbox('Difficulty',['Beginner', 'Intermediate', 'Adavanced'])
mode = st.radio('Activity', ['Generate Questions','Generate Code Questions','Evaluate Answers','Improve Answers'])
if mode == 'Generate Questions':
  count = st.slider(1,10,5)
elif mode == 'Generate Code Questions':
  topic = st.selectbox('Topics', ['SQL', 'AIML', 'Python', 'DSA', 'Java', 'c/c++'])
  count = st.slider("Number of Questions",1,10,5)
else:
  questions = st.text_area('Enter Interview Questions here')
  answer = st.text_area('Enter your answer', height =160)
if st.button("Generate AI Response", type = "primary"):
  if mode in ['Evaluate Answers', 'Improve Answers'] and (not question.strip()) or (not answer.strip()):
    st.warning("Please enter a valid Question and Answer")
    st.stop()
  topics = "Topics is"+topic+"difficulty is"+level
  if mode == "Generate  Questions":
    task = "Generate" + str(count)+"Frequently asked Interview Questions 3 theory and 2 Scenario questions.Do not give answer.give hint"
  elif mode == "Generate Code Questions":
    task = "Generate" + str(count)+"Frequently asked coding question on topic"+"and give nints to solve them.Be accurate."
  elif mode == "Evaluate Answer":
    task = "Question:" + "My Answer:"+answer+"Evaluate this answer based on concept,relevance,communication,length of answer.Give each rating out of File in a list"
  elif mode =="Improve Answer":
    task = "Question:"+question+"My answer:"+answer+"Improve the answer based on choices of words"
  background = "Job role:"+role+"Difficulty level" + level
  with st.spinner("Generatating your answer..."):
    try:
      response = client.chat.completions.create(
        model = gen_mode,
        messages = [{"role":"system",
                     "content":"Act as senior interviewer,both HR and Technical export"},
                    {"role":"user",
                     "content":background + task}],
        temperature = 0.7,
        max_tokens = 1800
      )
      output = response.choices[0].message.content
      st.subheader("AI Response")
      st.markdown(output)
      st.download_button("Download Response",output,file_name="Interview_Response.txt",mime = 'text/plain')
      
    except Exception as e:
      st.error("API connection was unsucessaful:",e)
      st.info("Please check your API key and rate limits")
st.caption("Powered by Streamlit.io and GitHub.Using LLM API")
     
  


   
