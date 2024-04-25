import openai
import streamlit as st
import os

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

import openai
import streamlit as st
import os

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("WorkPain Генерация вопросов")
# os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
count = 5
"""Описание проекта и про генерацию вопросов"""
st.subheader('Выберите размер анкеты:')
# st.write('Чем чаще, тем меньше количество вопросов, это позволяет не заскучать при частоте опросов, но Вы всегда можете отменить количество вопросов в анкете.')
option = st.selectbox(
   "Как часто Вы собираетесь проводить этот опрос?",
   ("Каждый месяц", "Каждый квартал", "Каждый год"),
   index=None,
   placeholder="Выберите подходящий вариант из списка...",
)

if option == 'Каждый месяц':
    st.image('week.png')
    count = 5
elif option == 'Каждый квартал':
    st.image('quartal1.png')
    count = 10
elif option == 'Каждый год':
    st.image('year.png')
    count = 15

count = st.text_input('Количество вопросов в анкете', f'{count}')


st.subheader('Какие темы Вы хотите видеть в вопросах:')
questions = st.text_input('Напишите здесь темы', 'Стресс на работе, поддержка...')


if st.button("Сгенерировать вопросы", type="primary", use_container_width=1):
    st.subheader("Ещё в процессе...")









# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": """Я — чат-бот, специально созданный для того, чтобы поговорить о вашей работе и потребностях для последущего своего развития! 
#                                     Как вас зовут?"""}]    

# for msg in st.session_state.messages:
#     if msg["content"] != "Я хочу, чтобы ты выступил в роли эксперта в области CustDev у Hr-ов по сбору обратной связи, с большим опытом и знаниями в сфере интервьюирования. Ты обладаешь глубоким пониманием того, как создавать эффективные стратегии для выявления истинного мнения. Кратко слушая человека и задавая наводящие вопросы, не пиши своё мнение и пиши кратко. Начни общение с того где работает человек, а после с вопроса по частоте проведения обратной связи, а после узнать о проблемах в подходе сбора обратной связи и продолжай задовать вопросы на разные темы сбора обратной связи:":
#         st.chat_message(msg["role"]).write(msg["content"])

# st.session_state.messages.append({"role": "user", "content": "Я хочу, чтобы ты выступил в роли эксперта в области CustDev у Hr-ов по сбору обратной связи, с большим опытом и знаниями в сфере интервьюирования. Ты обладаешь глубоким пониманием того, как создавать эффективные стратегии для выявления истинного мнения. Кратко слушая человека и задавая наводящие вопросы, не пиши своё мнение и пиши кратко. Начни общение с того где работает человек, а после с вопроса по частоте проведения обратной связи, а после узнать о проблемах в подходе сбора обратной связи и продолжай задовать вопросы на разные темы сбора обратной связи:"})


# if prompt := st.chat_input():
#     # if not openai_api_key:
#     #     st.info("Please add your OpenAI API key to continue.")
#     #     st.stop()

#     openai.api_key = os.getenv('OPENAI_API_KEY')
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message
#     st.session_state.messages.append(msg)
#     st.chat_message("assistant").write(msg.content)



# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": """Я — чат-бот, специально созданный для того, чтобы поговорить о вашей работе и потребностях для последущего своего развития! 
#                                     Как вас зовут?"""}]    

# for msg in st.session_state.messages:
#     if msg["content"] != "Я хочу, чтобы ты выступил в роли эксперта в области CustDev у Hr-ов по сбору обратной связи, с большим опытом и знаниями в сфере интервьюирования. Ты обладаешь глубоким пониманием того, как создавать эффективные стратегии для выявления истинного мнения. Кратко слушая человека и задавая наводящие вопросы, не пиши своё мнение и пиши кратко. Начни общение с того где работает человек, а после с вопроса по частоте проведения обратной связи, а после узнать о проблемах в подходе сбора обратной связи и продолжай задовать вопросы на разные темы сбора обратной связи:":
#         st.chat_message(msg["role"]).write(msg["content"])

# st.session_state.messages.append({"role": "user", "content": "Я хочу, чтобы ты выступил в роли эксперта в области CustDev у Hr-ов по сбору обратной связи, с большим опытом и знаниями в сфере интервьюирования. Ты обладаешь глубоким пониманием того, как создавать эффективные стратегии для выявления истинного мнения. Кратко слушая человека и задавая наводящие вопросы, не пиши своё мнение и пиши кратко. Начни общение с того где работает человек, а после с вопроса по частоте проведения обратной связи, а после узнать о проблемах в подходе сбора обратной связи и продолжай задовать вопросы на разные темы сбора обратной связи:"})


# if prompt := st.chat_input():
#     # if not openai_api_key:
#     #     st.info("Please add your OpenAI API key to continue.")
#     #     st.stop()

#     openai.api_key = os.getenv('OPENAI_API_KEY')
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message
#     st.session_state.messages.append(msg)
#     st.chat_message("assistant").write(msg.content)
