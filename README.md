# CP Contest Companion

 This script will help to download all the sample testcases of a contest.(_currently only supports codeforces._) This is a python script so **python needs to be installed** _(Preferebly python3.6)_ in order to install this.

 ## Requirements :

1. beautifulsoup4 (4.9.3)
2. bs4 (0.0.1)
3. certifi (2020.11.8)
4. chardet (3.0.4)
5. idna (2.10)
6. pip (9.0.1)
7. requests (2.25.0)
8. setuptools (28.8.0)
9. soupsieve (2.0.1)
10. urllib3 (1.26.2)

## Installation :

**Note :** <br> &nbsp; You can create a virtual enviroment (_python venv_) if you want to install the dependencies only for this project and don't install the dependencies globally.

To create a python venv enter the command below.

`python -m venv venv`

<br>

**General Steps :**

We have to just install all the dependencies by entering the command below and then we are good to go.
``pip install -r requirements.txt``

## Usage :

 If you have installed the venv then you have to first activate the venv and then run the main.py file.

- To activate the venv ente rthe following command.

**_If you are on Windows_ :**
`venv\Scripts\activate`

**_If you are on Linux_ :**
`source venv/bin/activate`

- Then run the main.py file by 
`python main.py`

- This will ask the contest URL _(eg: https://codeforces.com/contest/1452)_ and the absolute location _(eg: C:\\Users\\test\\Downloads\\cp_companion)_ where you want to store the sample-testcases folder.<br><br> **Note : Don't give the relative path as an input** 
