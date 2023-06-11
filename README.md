# Use Playwright For Web Scraping with Python

The task requires developing a frontend-backend solution. The backend developer's role is to create the backend solution and use minimal frontend if necessary. The requirements are as follows:

1. Develop a Python module that utilizes the playwright-browser to scrape company details from G2Crowd, using a provided CSV of G2Crowd URLs (URL shortening service). The output should be structured, such as a JSON or CSV file with fields and values.
2. Additional considerations include:
   1. Making all API calls asynchronous.
   2. Implementing appropriate exception handling throughout the code

# Playwright Setup & Installation

## Virtual Environment & Playwright Installation

Create a dedicated folder for the project called playwrightwebscraping. (This step is not mandatory but is good practice).
Next, using Python’s built-in venv module, let’s create a virtual environment named playwrightplayground and activate it by calling the activate script.

~~~
pyenv install 3.11.4 
pyenv shell 3.11.4
mkvirtualenv playwrightwebscraping
git clone git@github.com:vantares/playwright-python-scraping.git
cd playwright-python-scraping
workon playwrightwebscraping
pip install -r requirements.txt
~~~


Scrapping Content
Pretty dificult page
use firefox to avoid CloudFormation validation
Wait for redirection

~~~
 python scrap_company.py --browser firefox 
~~~