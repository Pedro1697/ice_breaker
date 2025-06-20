import os
import requests

from dotenv import load_dotenv

load_dotenv()
def is_structurally_empty(val):
    if val in (None, "", [], 0):
        return True
    if isinstance(val, dict):
        return all(is_structurally_empty(v) for v in val.values())
    return False

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """ scrape information from LinkedIn profiles,
    Manually scrape the information from LinkedIn profile """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey":os.environ["SCRAPIN_API_KEY"], # We have to use the name of the params in this way for th API function 
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params = params,
            timeout=10
        )

    data = response.json().get("person") # We turn the response into a dictionary with .json method 
    # the ["person"] key exists because we use scrapin.io API

    data = {
        k:v
        for k, v in data.items()
        if not is_structurally_empty(v)
        # and k not in {"testScores","recommendations"} if we want to delete an specifict field eg
      
    }
    return data


if __name__ == "__main__":
    print(scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/pedronaguilar/",
        )
    )