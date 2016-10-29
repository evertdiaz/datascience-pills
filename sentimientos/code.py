import tweepy
from textblob import TextBlob as tb
# Textblob es para PLN, solo soporte ingles.

consumer_key = 'XXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXX'
acces_token = 'XXXXXXXXXXXXXX'
acces_token_secret = 'XXXXXXXXXXXXXXXXXXX'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

interfaz = tweepy.API(auth)

#Busqueda de tweets
public_tweets = interfaz.search('ISIS')

#Analizar cada tweet encontrado
for tweet in public_tweets:
	print tweet.text
	analisis = tb(tweet.text)
	# Imprimir resultado de polaridad y subjetividad
	print analisis.sentiment
