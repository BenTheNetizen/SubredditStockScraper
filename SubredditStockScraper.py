# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:43:08 2021

@author: BenTheNetizen 
"""

import praw
import nltk
import pandas as pd

df = pd.read_excel('nyse.xlsx')
nyse = df['Name'].values.tolist()

df2 = pd.read_excel('nasdaq.xlsx')
nasdaq = df2['Symbol'].values.tolist()

df3 = pd.read_excel('common_words.xlsx')
english_words = df3['Words'].values.tolist()
english_words = [x.upper() for x in english_words if not isinstance(x, float)]

df4 = pd.read_excel('acronyms.xlsx')
acronyms = df4['Acronyms'].values.tolist()


reddit = praw.Reddit(client_id = 'my_client_ID',
                     client_secret = 'my_client_secret',
                     user_agent='my_user_agent')


def print_comments(num, subreddit):
    num_comments = 0
    curr_comments = 0
    unread_comments = 0
    
    f = open("redditstream.txt", "w+")
    
    print('\n')
    for submission in subreddit.hot(limit=num):
        try:
            f.write("TITLE: " + submission.title)
            print("Submission title: " + submission.title)
        except:
            print("Unable to read title")
        try:
            f.write("TEXT: " + submission.selftext)
        except:
            print("Unable to read submission text")
            
        for comment in submission.comments.list():
            try:
                f.write(comment.body + '\n')
                num_comments += 1
                curr_comments += 1
    
            except:
                unread_comments += 1
                
                
        print("Read comments: " + str(curr_comments))
        curr_comments = 0

    f.close()
    print('\n\n' + 60*'-')
    print("Unread comments: " + str(unread_comments))
    print("Total read comments: " + str(num_comments))
    print("The number next to each stock ticker is the level of interest. The tickers are displayed below in order of high to low interest.\n")
    
    
    
def analyze_comments():
    f = open("redditstream.txt").read()
    
    tokens = nltk.word_tokenize(f)
    
    tokens_l = [w.upper() for w in tokens]
    
    freq = nltk.FreqDist(tokens_l)
    common_words = freq.most_common(100000)
    
    tickers = {}

    for k, v in common_words:
        if (k in nyse or k in nasdaq) and k not in english_words and k not in acronyms:
            tickers[k] = v
    
    print(tickers)
    print(str(len(tickers)) + ' tickers')
    
    
    
    
bool_exit = False

while True:
    if bool_exit:
        break
    user_input = input("What subreddit would you like to analyze for stocks? (Ex: wallstreetbets, investing, stocks, robinhood, pennystocks) ")
    user_input = user_input.lower()
    if user_input == 'exit':
        break
    while True:
        user_num = input("How many submissions do you want to analyze? ")
        if user_num == 'exit':
            bool_exit = True
            break
        try:
            user_num = int(user_num)
            break
        except:
            print("That was not an integer, try again.")
            
    if bool_exit:
        break
    subreddit = reddit.subreddit(user_input)
    try:
        print_comments(user_num, subreddit)
        analyze_comments()
        while True:
            user_again = input("Do you want to analyze another subreddit? (y/n) ")
            user_again = user_again.lower()
            
            if user_again == 'y' or user_again == 'yes':
                break
            elif user_again == 'n' or user_again == 'no' or user_again == 'exit':
                bool_exit = True
                break
            else:
                print("That was not a valid input, try again.")
        
    except:
        print("Invalid subreddit, try again")



