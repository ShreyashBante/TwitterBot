import tweepy
import os
from dotenv import load_dotenv
from transformers import LlamaTokenizer, LlamaForCausalLM
import torch
from langchain.llms import CTransformers
import random

load_dotenv()

# Twitter API credentials
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
client = tweepy.Client(
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret,
    access_token=access_token, 
    access_token_secret=access_token_secret
)

def post_tweet(message):
    """
    Post a tweet with the given message.
    """
    try:
        response = client.create_tweet(text=message)
        print(f"Tweet posted successfully: {message}")
        print(f"Tweet ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
  
    model_path = r"E:\Proects\models\llama-2-7b-chat.ggmlv3.q8_0.bin"  # Adjust this path as needed
    
    llm=CTransformers(model='E:\Proects\models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.5,
                              'repetition_penalty': 1.1}  # Helps avoid repetitive text
                              )
    # Generate a tweet using the LLM
    prompts = [
        "Generate a short, engaging tweet about data Engineering",
        "Write a creative tweet about the future of data Engineering",
        "Create an interesting tweet about data pipelines and analytics",
        "Write a tweet about modern data Engineering challenges"
    ]
    
    prompt = random.choice(prompts)
    tweet_content = llm(prompt)

    # Trim the tweet content to fit Twitter's character limit
    max_tweet_length = 280
    if len(tweet_content) > max_tweet_length:
        tweet_content = tweet_content[:max_tweet_length-3] + "..."
    print(tweet_content)

    # Post the generated tweet
    post_tweet(tweet_content)
   
