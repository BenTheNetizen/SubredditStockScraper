# SubredditStockScraper

# IMPORTANT
To use SubredditStockScraper, you must input your Reddit API client_id, client_secret, and user_agent found on line 26 for this program to work!

# Summary
This program pulls data from Reddit using the Python Reddit API Wrapper and performs natural language processing (PRAW) to find the hottest stocks in discussion. Users chose a subreddit that includes stock discussions and the number of submissions they wish for the program to perform analysis on. SubredditStockScraper will look through the title, body, and comments of posts looking for the presence of stock tickers. Each appearance of a stock ticker increases its level of interest. 

# How it Works
SubredditStockScraper incorporates praw, nltk, and pandas to successfully analyze submissions on Reddit. Nltk is used to perform natural language processing to tokenize posts and create a FreqDist object. Using this object, the program can find the most common appearances on a given subreddit. Lastly, words that are not stock tickers are removed from the results by comparing them to a database of NYSE and NASDAQ stock tickers using a pandas dataframe. These databases are stored in xlsx files and are necessary for the program to run successfully. An issue I ran into was that common English words such as "it," "for," "so," etc. were being displayed as stock tickers, since they in fact are listed tickers. I had to incorporate another database of common acronyms and English words used in everyday speech to further prune the results. 

# Areas for Improvement
SubredditStockScraper has plenty of room for improvement. Currently the output of the program does not effectively capture all of the stock tickers being discussed since it prunes those that are spelled the same as common English words (see above). Furthermore, some tickers are outputted in the results despite not having "true" interest in Reddit submissions, as they were used as their literal meaning rather than their ticker representation. For example, words or acronyms such as "RSI" and "AHH" appear in the output as stock tickers but were not used in that sense in the submissions. 

Furthermore, the issue with the client_id, client_secret, and user_agent needing to be provided by the user is another place for improvement. I plan on implementing a fix for this soon.
