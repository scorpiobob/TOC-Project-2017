# TOC Project 2017

Template Code for TOC Project 2017

A telegram bot based on a finite state machine

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, 
till to the state6(die)
it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "birth"
		* Reply: "I'm an egg,please give bone or give fish to me"
* state1

	* Input: "give bone"
		* Reply: "I'm a puppy,feed me"
	* Input: "give fish"
		* Reply: "I'm a kitten,let me big"
* state2
	* Input: "feed"
		* Reply: "I'm dog"
* state3
	* Input: "die"
		* Reply: "I'm dead,birth me again"
* state4
	* Input: "big"
		* Reply: "I'm a cat"
* state5
	* Input: "die"
		* Reply: "I'm dead,birth me again"


## Author
[scorpiobob](https://github.com/scorpiobob)
