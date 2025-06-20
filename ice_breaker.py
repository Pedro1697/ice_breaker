from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile
if __name__ == '__main__':
    load_dotenv()
    print("Hello LangChain")
    
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

# tempeture is the creativity of the LLM

chain = summary_prompt_template | llm 
linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/pedronaguilar/",mock=True)

res = chain.invoke(input={"information":linkedin_data})

print(res)