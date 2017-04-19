# ![alt text](http://i.imgur.com/FwSLsb1.gif "FancyTweeter!")
[![version][release-badge]][RELEASE] [![license][license-badge]][LICENSE]


Pettiness? Fuck yea. Jack Schefer? The love of my life💕💕💕

This application allows a twitter account to respond to any mention with the same exact words but with the closest synonyms for the words in the tweet.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

You will need the [Git CLI](https://git-scm.com/downloads) and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed on your machine. 

You will need to create an application in [Twitter Apps](https://apps.twitter.com)
You will need to create a Thesauras Key account in [Dictionary.com](http://www.dictionaryapi.com)

This project is written in [Python 3.6.0](https://www.python.org/downloads/) so you're probably going to need that.

### Installation

A step by step series of what to do to get FancyTweeter running.

Clone the repository

``` Shell
$ git clone https://github.com/SishaarRao/Tweet-at-Trump.git
```

Go in and edit *secret.py* with your Consumer & Access keys

``` Python
# Go to http://www.dictionaryapi.com and create an account.
# Generate a Thesauras Key and insert it here
THESAURAS_KEY = 'INSERT YOUR THESAURAS KEY HERE'

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
CONSUMER_KEY = 'INSERT YOUR CONSUMER KEY HERE'
CONSUMER_SECRET = 'INSERT YOUR SECRET CONSUMER KEY HERE'

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
ACCESS_KEY = 'INSERT YOUR ACCESS KEY HERE'
ACCESS_SECRET = 'INSERT YOUR SECRET ACCESS KEY HERE'

```

Go in and edit *main.py* with the USERNAME that the account is tweeting from
Similarly, comment out the sishaarSecret import statement and uncomment the secret import statement

``` Python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from sishaarSecret import THESAURAS_KEY, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from secret import THESAURAS_KEY, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
import urllib.request
import re
import lxml.etree as ET
from stop_words import get_stop_words
import tweepy, time, sys

USERNAME = "Sishaar_Rao_API"
...
```

## Running a Test

You can run *main.py* on your local machine.

``` Shell 
$ python3 main.py
```
Note: The account will only automatically tweet while the program is running, so tell your friend to tweet at the account while it's running, and see if the program tweets in response.

## Deployment

FancyTweeter will be deployed through Heroku so that you don't have to run it locally on your system.

Make sure you have heroku and git on your system, and make sure to login to both.

``` Shell
$ heroku --version
$ git --version
$ heroku login
```

Run *setup.sh*

``` Shell
$ bash setup.sh
```

After a few seconds, run this command. If you see 'worker: crashed', refer to [Errors](#errors). If not, then FancyTweeter is up!

``` Shell
$ heroku ps
```

If you decide that you want to turn off the autoreply, simply run *turnOff.sh*

``` Shell
$ bash turnOff.sh
```

If, after doing this you want to turn it back on, simply run *turnOn.sh*

``` Shell
$ bash turnOn.sh
```

## Errors

If you run ``` $ heroku ps ``` and see something along these lines:

``` Shell
=== worker (Free): python main.py (1)
worker.1: crashed 2017/03/25 21:15:25 -0400 (~ 11s ago)
```

Run ``` $ heroku logs ``` and read for errors, which will look something like this:

``` Shell
2017-03-26T01:15:16.554159+00:00 heroku[worker.1]: Starting process with command `python main.py`
2017-03-26T01:15:17.880765+00:00 heroku[worker.1]: State changed from starting to up
2017-03-26T01:15:19.154593+00:00 heroku[worker.1]: Process exited with status 0
2017-03-26T01:15:19.037822+00:00 app[worker.1]: ERROR : connection failed. Check your OAuth keys.n
2017-03-26T01:15:19.168674+00:00 heroku[worker.1]: State changed from up to crashed
2017-03-26T01:15:19.168674+00:00 heroku[worker.1]: State changed from crashed to starting
2017-03-26T01:15:22.902282+00:00 heroku[worker.1]: Starting process with command `python main.py`
2017-03-26T01:15:23.465315+00:00 heroku[worker.1]: State changed from starting to up
2017-03-26T01:15:24.988934+00:00 heroku[worker.1]: Process exited with status 0
2017-03-26T01:15:24.887512+00:00 app[worker.1]: ERROR : connection failed. Check your OAuth keys.
2017-03-26T01:15:25.001256+00:00 heroku[worker.1]: State changed from up to crashed
```

Reading through logs, we can see the message ``` 2017-03-26T01:15:19.037822+00:00 app[worker.1]: ERROR : connection failed. Check your OAuth keys. ``` which means you need to confirm your OAuth keys are correct. 

## Built With

* [Tweepy](http://www.tweepy.org) - Python library for Twitter API
* [Heroku](https://www.heroku.com/) - Deployment of Tweet@Trump
* [Emacs!!](https://www.gnu.org/software/emacs/) - Native Development

## Contributing

Please read [CONTRIBUTING.md](https://github.com/SishaarRao/Tweet-at-Trump/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Sishaar Rao** - *Version 1* - [SishaarRao](https://github.com/SishaarRao)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/SishaarRao/Tweet-at-Trump/blob/master/LICENSE) file for details

## Acknowledgments

I love you Jack.

[LICENSE]: ./LICENSE
[license-badge]: https://img.shields.io/badge/license-MIT-brightgreen.svg
[RELEASE]: https://github.com/SishaarRao/Tweet-at-Trump/releases/tag/v1.0.0
[release-badge]: https://img.shields.io/badge/Version-1.0.0-brightgreen.svg