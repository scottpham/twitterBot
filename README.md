BotMaker
==========

In March, a medium-sized earthquake hit the Los Angeles area.  It's not particularly uncommon, but there had been an earthquake-drought of sorts, so it warranted a write-up. The very first publication to break that story was the Los Angeles Times, [thanks to a news-writing bot written bot](http://www.slate.com/blogs/future_tense/2014/03/17/quakebot_los_angeles_times_robot_journalist_writes_article_on_la_earthquake.html) written by Ken Schwencke, a journalist and programmer for the paper.

We're guessing that in the near future, a lot more stories will be broken by bots. It's likely that the writers of those bots won't be journalists and they won't work for traditional news publications.  But it doesn't have to be that way.

Anxiety
========
There's a lot of anxiety about bots in journalism. Journalists worry that bots might take their jobs one day. They think bots are antithetical to responsible journalism. But we think bots should be about fun and exploration. Maybe someday the best bots will free the rest of us to focus on the stories that matter — the stories that use our full human faculties and require insight and judgment. 

Bots in Seconds
===============
The goal of BotMaker is to make writing and deploying Twitter bots dead simple. Its target audience is journalists who might be interested in automation, but don't have the time or skills to build one from scratch.

If you can use a Google spreadsheet, you can use BotMaker and roll your own Twitter bot.

Use Cases
============
The public service use cases are easy to imagine: bots that tweet out crimes, environmental data, earthquakes.  Some of these exist right now.  But the very best use cases are the ones we or you haven't even thought of yet! If making a bot is easy and quick, then ideas can come to you on the fly. Do you have unused data sets waiting for a story? Maybe a bot can get that out.  Are you scraping a site to gather statistics? Make use of those individual data points and feed them to your bot!

How to Use
==========
BotMaker is a work in progress, but you should be able to get a version running on your system with a little work.

1. Make a Twitter account
	- We used [this primer from Source](https://source.opennews.org/en-US/articles/botmaking-primer/) for guidance. You'll need to register for an API key and copy your four authentication keys.

2. Plug in your key values on tweet.py
	- Using a code editor, you need to write your own values for:
		- API_KEY  
		- API_SECRET  
		- ACCESS_TOKEN  
		- ACCESS_TOKEN_SECRET  

3. Load up a google spreadsheet
	- Change your sharing settings so that the doc is "Public on the Web."
	- You also need to "publish" your doc by hitting the "Publish to the Web" button under the "File" menu
  	-  Get your "key" from your spreadhseet's URL. That's the number between the '=' and the '#' in this example: https://docs.google.com/spreadsheet/ccc?key=0AhjKa3sJb0yXdGpEVWJNUkZaUlRDRVZkQnlqbkZzdWc#gid=0

4. Clone a copy of the app in your desktop and run it using Python in your terminal
  	- BotMaker is dependent on Python and the Twython library, [available here](https://github.com/ryanmcgrath/twython).

To Do
=======
BotMaker is a working prototype but our team has a little more work to do:

What we need to get to a decent version 1.0:
- Clean up front end code
- Parse input strings more cleanly with proper regex
  - Generate proper arrays for backend ajax call
- Rethink fake templating handlebars {{ }}--maybe variables are just words with different styling/coloring?
- Redo CSS using boostrap customization best practices
- Rethink how spreadsheet gets passed to backend--how can we deal with live data, i.e. a google sheet that changes?
- Allow for more variation in tweet formation: i.e. tweets that contain different #s of text and variables
- Allow user to input own twitter API Keys directly in the front-end
- Hook up to heroku or something so user doesn't have to run python script in terminal

Cool Future Features:
- Build some kind of web scraping into the front end
- Allow for conditional tweets (i.e. tweet only when certain values meet a condtion, or tweet different tweets for different values)
- Let bot respond to mentions
- Let bot search twitter for keywords and tweet at those accounts
- deploy to Heroku
- user inserts own Twitter account credentials and include instructions on how to obtain
- connect to kimonolabs or other UI-based web scraping (optional Google spreadsheets proxy)


About
======
BotMaker was created as part of the [Reynolds Journalism Institute Social Journalism Hackathon](http://www.rjionline.org/hackathon). The team includes:  
  - [Scott Pham](https://twitter.com/scottpham)  
  - [Amy Lee](https://www.linkedin.com/in/amylibra)  
  - [Maggie Shine](https://twitter.com/magksh)
