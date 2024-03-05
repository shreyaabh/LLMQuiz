from langchain.llms import OpenAI
from langchain import PromptTemplate
import openai
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import pandas as pd


def quiz_generator(topic, language):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key='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',
        temperature=0.5,
        max_tokens=4095
    )
    prompt_template = """Role: Act as a particular subject teacher and complete the given task below as shown in example.

        Task: Generate a quiz with 10 questions. The quiz should contain MCQ with 4 options and only one correct answer. 

        Example:
        Query : Generate the quiz on the topic : addition upto 25

        Output Format : 
        Question : What is 12 + 4?
        Category : Math
        Tags: Arithmetic, Addition, Add
        Topic : addition upto 25
        Answer 1 : 16
        Answer 2 : 19
        Answer 3 : 14
        Answer 4 : 18

        Most Important Instructions:
        1. The most important thing is that the Correct answer is always in Answer 1. 
        2. Always maintain the particular topic and output format while generating.
        3. Always generate 10 questions.
        {context} 

        """

    prompt = PromptTemplate(
            input_variables=["context"],
            template=prompt_template,
        )
    chain = LLMChain(llm=llm, prompt= prompt)
    
    query = f"Generate quiz on topic : {topic} in langauge {language}"
    
    quizz = chain.run(query)

    return quizz
    
    
