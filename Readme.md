Quiz App - Django - HTML
=================================================

Quiz app using Django and login with Html.

## Install

```elixir

# Global Installation

sudo apt-get install python-setuptools
sudo apt-get install python-pip

sudo pip install djangorestframework==3.11.1
sudo pip install backcall==0.2.0
sudo pip install decorator==4.4.2
sudo pip install Django==1.11
sudo pip install ipdb==0.13.3
sudo pip install ipython==7.9.0
sudo pip install ipython-genutils==0.2.0
sudo pip install jedi==0.17.2
sudo pip install parso==0.7.1
sudo pip install pexpect==4.8.0
sudo pip install pickleshare==0.7.5
sudo pip install pkg-resources==0.0.0
sudo pip install prompt-toolkit==2.0.10
sudo pip install ptyprocess==0.6.0
sudo pip install Pygments==2.6.1
sudo pip install pytz==2020.1
sudo pip install six==1.15.0
sudo pip install traitlets==4.3.3
sudo pip install wcwidth==0.2.5

```

```elixir

# if using virtual environment python

virtualenv quizenv
source quizenv/bin/activate
pip install -r requir.txt
```

## Run code here
```elixir
git clone https://github.com/manioftony/Quiz-App
cd Quiz-App
python manage.py runserver

http://127.0.0.1:8000/
```


## Get the question and answer using token based authentication  

## culr command

-------------curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"username": "mani", "password": "admin@123"}' http://127.0.0.1:8000/api-token-auth/

result:
    {"token":"e036d94d1a5cc4b3d17a9ef084f8f1a1c7b45f71"}

-------------curl -X GET -i -H "Content-Type: application/json" -H "Authorization: Token e036d94d1a5cc4b3d17a9ef084f8f1a1c7b45f71" http://127.0.0.1:8000/question-answer/

result :

```elixir
{
    'data': [{
            'answer': '4',
            'question': 'what is 2+2?'
        },
        {
            'answer': '2',
            'question': 'what is 4-2?'
        },
        {
            'answer': '38',
            'question': 'what is 19*2?'
        }
    ],
    'status': 200
}
```




## Using python requests

sudo pip install requests
    or 
pip install requests

myurl = 'http://127.0.0.1:8000/api-token-auth/'

auth = {'username': 'mani', 'password': 'admin@123'}

response = requests.post(myurl, auth)

token = response.json()['token']

headers = {'Authorization': 'Token %s' % token}

url = 'http://127.0.0.1:8000/question-answer/'

response = requests.get(url, headers=headers)

print(response.json())


result :

```elixir
{
    'data': [{
            'answer': '4',
            'question': 'what is 2+2?'
        },
        {
            'answer': '2',
            'question': 'what is 4-2?'
        },
        {
            'answer': '38',
            'question': 'what is 19*2?'
        }
    ],
    'status': 200
}

