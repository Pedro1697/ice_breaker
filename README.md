# Ice Breaker

## Overview
The purpose of this project is to start in the generative AI with an ice breaker using LangChain to search a person and return the profile picture  with a summary and two interesting facts about them, this information is obtained and extracted of the LinkedIn of the person searched all of this through an UI. 

![image](https://github.com/user-attachments/assets/562c223f-5128-4e4b-83cb-57f54909b8b5)

## Environment Variables
> SCRAPIN_API_KEY \
> GOOGLE_API_KEY \
> TAVILY_API_KEY \

To run this project, you will need to add the following environment variables to your .evn file

## Usage
Clone the project
```
git@github.com:Pedro1697/ice_breaker.git
```
Go to te project directory
```
cd ice_breaker
```
Install dependecies
```
pipenv install
```
Start the flask server
```
pipenv run app.py
```

## Project Structure
* agents 
* templates
* third_parties
* tool
* Pipfile
* Pipfile.lock
* app.py
* ice_breaker.py
* output_parser.py

## Tecchnologies Used
* Python
* LangChain
* Js
* Html
* Flask


## License 
This project is licensed under the MIT License. See the LICENSE file for details.
## Credits 
https://github.com/emarco177
