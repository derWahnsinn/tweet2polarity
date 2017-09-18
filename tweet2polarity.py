#!/usr/bin/python3
##

import tweepy
import json
import time
from textblob import TextBlob
import argparse
import sys



## TWITTER API SECRETS:
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

keyfile = open("api.key","r")
for x in keyfile.readlines():
	if x.startswith("consumer_key ="):
		consumer_key = x.split("=")[1].lstrip(" ").replace("\n","")
	elif x.startswith("consumer_secret ="):
		consumer_secret = x.split("=")[1].lstrip(" ").replace("\n","")
	elif x.startswith("access_token ="):
		access_token = x.split("=")[1].lstrip(" ").replace("\n","")
	elif x.startswith("access_token_secret ="):
		access_token_secret = x.split("=")[1].lstrip(" ").replace("\n","")
	else:
		print("ERROR: can't read api.key file!")
		sys.exit(0)
		
## PARSE STDIN
parser = argparse.ArgumentParser()
parser.add_argument('-t', nargs='+', help='filter hashtags (example: -t dog cat fish)', action='append')
parser.add_argument('-s', help='seconds to calculate the average of the polarity')
args = parser.parse_args()
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
hashtag = args.t[0]
runtime = args.s




## DECLARE COLORS
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	def disable(self):
		self.HEADER = ''
		self.OKBLUE = ''
		self.OKGREEN = ''
		self.WARNING = ''
		self.FAIL = ''
		self.ENDC = ''

ticks = []
scorelist = []
myscore = 0
class StdOutListener(tweepy.StreamListener):
	def on_data(self, data):
		try:
			global scorelist
			decoded = json.loads(data)
			user = str(decoded['user']['screen_name'].encode('ascii', 'ignore'))[:-1][2:]
			mmessage = str(decoded['text'].encode('ascii', 'ignore')).lstrip(" ")[:-1][2:]
			if mmessage.startswith("RT") or mmessage.startswith('RT'):
				pass
			else:
				testimonial = TextBlob(mmessage)
				myticks = str(time.time()).split(".")[0]+":"+str(testimonial.sentiment.polarity)
				if float(testimonial.sentiment.polarity) == float(0.0):
					pass
				else:
					ticks.append(myticks)
				for x in ticks:
					timee = x.split(":")[0]
					score = x.split(":")[1]
					if float(timee) > float(time.time()-int(runtime)):
						pass
					else:
						ticks.remove(x)
						pass
					
				for x in ticks:
					timee = x.split(":")[0]
					score = x.split(":")[1]
					mylen = len(ticks)
					scorelist.append(float(score))
				
				
				mylen = len(ticks)
				myscore = sum(map(float, scorelist))/mylen
				if myscore < float(0.0):
					sys.stdout.write("\033[F")
					sys.stdout.write("\033[K")
					print("Current "+str(runtime)+" seconds score:\t"+bcolors.FAIL+str(myscore)+bcolors.ENDC+"\t"+bcolors.OKBLUE+user+bcolors.ENDC+":\t"+mmessage)
				elif myscore > float(0.0):
					sys.stdout.write("\033[F")
					sys.stdout.write("\033[K")
					print("Current "+str(runtime)+" seconds score:\t"+bcolors.OKGREEN+str(myscore)+bcolors.ENDC+"\t"+bcolors.OKBLUE+user+bcolors.ENDC+":\t"+mmessage)
				else:
					sys.stdout.write("\033[F")
					sys.stdout.write("\033[K")
					print("Current "+str(runtime)+" seconds score:\t"+str(myscore)+"\t"+bcolors.OKBLUE+user+bcolors.ENDC+":\t"+mmessage)
				scorelist = []
				return True
		except Exception as e:
	#		print(e)
			pass

	def on_error(self, status):
		print(status)

if __name__ == '__main__':
	l = StdOutListener()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, l)
	stream.filter(track=hashtag)
