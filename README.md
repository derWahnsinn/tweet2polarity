# tweet2polarity

collect tweets of a selected timeframe and calculate the average polarity of the tweets


## Getting Started

```
usage: tweet2polarity.py [-h] [-t T [T ...]] [-s S]

optional arguments:
  -h, --help    show this help message and exit
  -t T [T ...]  filter hashtags (example: -t dog cat fish)
  -s S          seconds to calculate the average of the polarity
```


### Prerequisites

install dependencies:

```
pip install tweepy textblob
```

### Installing

```
git clone https://github.com/derWahnsinn/tweet2polarity.git
cd tweet2polarity/
```

edit the api.key file with you twitter credentials

example api.key file:
```
consumer_key = klajsdlfija890sd8u9fa0djlo
consumer_secret = djfhnkajshdudifhklwern989jomiy9x8c
access_token = 1929828347-1930sfxj88d0ajdijr00239as
access_token_secret = c8xilxmlijaosd9u0x98jos
```

now run tweet2polarity with your desired #hashtags and timeframe like:

```
python tweet2polarity.py -t dog cat fish -s 60
```

will give something like:

![alt text](http://www.true-binary.com/wp-content/uploads/2017/09/tweet2polarity.png)


0 1 0
0 0 1
1 1 1