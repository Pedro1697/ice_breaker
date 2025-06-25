from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile
import os 
from agents.lindekind_lookup_agent import lookup as linkedin_lookup_agent

def ice_breaker_with(name:str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    summary_template = """
            given the Linkedin {information} about a person from I want you to create:
            1. A short summary
            2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
                                          input_variables=["information"],
                                          template=summary_template
                                        )
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    chain = summary_prompt_template | llm 
    res = chain.invoke(input={"information":linkedin_data})

    print(res)
if __name__ == '__main__':
    load_dotenv()
    print("Ice Breaker Enter")
    ice_breaker_with(name="Pedro Nicolas Aguilar Gomez")
    

# tempeture is the creativity of the LLM

