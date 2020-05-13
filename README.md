
## Description

* The idea of this was project was to carry out some basic interactions on reddit. Just me generally playing around with selenium, page-object model and I'm not exactly well versed in the python.
* These automated tests are quite brittle therefore, I wouldnt be surprised if this project largely fails all of its tests in the future, however the code is still here to see and the page-object model makes it a bit easier to fix.

## Setup

* Check the requirements.text and install packages
* Using Chrome because although I'm on Mac nobody likes Safari
* The version of Chromedriver I've been using  is included in resources folder
* Made using Pycharm and should conform to pep8 (Except maybe the 79 char width)

## Classes

* Base - All pages inherit Base
* Locators - Contains all locators
* Users - Tiny class just for storing test users
* Pages - Groups methods around the page the operate on
* TestCases - All test cases that run in alphabetical order

## How I found it

* It was quite tricky as the new Reddit website uses lacks any static attributes, as a 
result I have relied heavily on xpath which is probably a bit more heavy as oppose to traversing the DOM. Hopefully 
the tests shouldn't be too brittle
* There are comments through out the code, mostly to explain where I think a better approach could be taken or just 
explaining a particular piece of code.
* There is also some type hinting, but not throughout

 
## Test Cases

* Open the website https://www.reddit.com/
* Search for a subreddit called "gaming"
* Open the sub-reddit
* Print out the top most post's title
* Perform a login
* Downvote the second post if it's upvoted already, upvote otherwise (in case the second post is an advertisement or 
announcement, use the third)
