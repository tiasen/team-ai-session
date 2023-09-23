from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

template = """
You are an old man who can tell stories. 
Now I will give you a description in English and ask you to generate a humorous story based on this conversation. 
Keep the story less than 50 words. Just tell me the outcome of the story.
description: {context}
Story:
"""

def generate_story(context: str):
    llm = OpenAI(temperature=0)

    prompt_template = PromptTemplate(input_variables=["context"], template=template)

    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    print("Generating story...")
    story = llm_chain.run(context)
    print("Story: " + story)

    return story


if __name__ == "__main__":
    print(generate_story("woman sitting on the beach with her dog and a cell phone"))