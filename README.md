## Fetch Rewards Challenge

This project is for the coding project given by Fetch Rewards. The instructions are in this [PDF](./points.pdf) which will show the project objectives. FastAPI is used for the implementation of the project.

# Installation

[Python3](https://www.python.org/downloads/) should be installed to run the code. Also, the following uses the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies needed for this project. I have created a bash script to install the dependencies which can be viewed [here](./downloads.sh) and can be run as shown below in a terminal.

```bash
./downloads.sh
```

One note is that you may need to change the access permissons for the bash files which can be done as follows to make them executable.

```bash
chmod +x downloads.sh
```

# Paths
1. Add transactions for a specific payer and date.
    * http://127.0.0.1:8000/add
2. Spend points using the rules above and return a list of ​{ "payer": <string>, "points": <integer> }​ for each call.
    * http://127.0.0.1:8000/spend
3. Return all payer point balances.
    * http://127.0.0.1:8000/balance

# Testing

For testing purposes there are two ways I will demonstrate. First is using unvicorn (which should be installed if downloads.sh is executed) and curl. In one open terminal run the command that follows.

```bash
uvicorn main:app --reload
```

While keeping that first terminal running another one should be opened to now make the curl calls. There are three different paths the can be called and I will demonstrate each below.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }'
curl -X 'POST' \
  'http://127.0.0.1:8000/spend' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "points": 5000 }'
curl -X 'GET' \
  'http://127.0.0.1:8000/balance' \
  -H 'accept: application/json'
```

The second way to test is by having the first terminal still open with the unvicorn call running and then going to http://127.0.0.1:8000/docs which will provide a user interface to make the post and get calls while allowing one to type in the json needed. Futhermore, there is a testing file called [test_run.sh](./test_run.sh) which has a basic test in it with more examples to look at.
