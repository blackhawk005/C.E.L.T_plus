# SE Project 2

# C.E.L.T: The Sentimental Analyser is now C.E.L.T Pro! 

![C E L T_PLUS](https://github.com/blackhawk005/C.E.L.T_plus/assets/63787850/e35c3410-b85e-4d53-be89-12719e3c756f)

## Watch how our application works: 

[Youtube Video](https://youtu.be/V_F8zJv_IIg) <br>

[![DOI](https://zenodo.org/badge/722772372.svg)](https://zenodo.org/doi/10.5281/zenodo.10208268)

[![Build Status](https://travis-ci.org/karthikmp5/C.E.L.T_pro.svg?branch=master)](https://travis-ci.org/karthikmp5/C.E.L.T_pro)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![codecov](https://codecov.io/gh/usmanwardag/dollar_bot/branch/main/graph/badge.svg?token=PYAWX95R67)](https://codecov.io/gh/usmanwardag/dollar_bot)

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

![Open Issues](https://img.shields.io/github/issues/blackhawk005/C.E.L.T_plus)

![Closed Issues](https://img.shields.io/github/issues-closed/blackhawk005/C.E.L.T_Plus)

![CI/CD](https://img.shields.io/badge/CI/CD-Passing-brightgreen)


## What is C.E.L.T?

Sentiment analysis is one of the fastest growing research areas in computer science, making it challenging to keep track of all the activities in the area. In our project we aim to achieve our goal in accurately predicting a users sentiment by analysing the data provided in any of the four different methods. They are Document Analysis, Text Analysis, Product Analysis, Tweet Analysis, Image Analysis and Audio Analysis. This document provides a major perspective for the users to understand and take up the project as an Open source software and add on multiple features before releasing to the market. Also, the document aids the developers in understanding the code and acts as a reference point for starting the project.

## PROJECT FLOW
1. The landing page on our website provides comprehensive information on various types of analyses, each with its respective link.
2. Once you have identified the specific type of analysis relevant to your needs, you will be directed to a form that accepts input for sentiment analysis.
3. The algorithm performs the analysis once you have provided the input and initiated the analysis. The results are presented in a variety of visual formats, including pie charts and bar graphs.
4. The output is segmented into three distinct categories, namely positive, neutral, and negative sentiments, each represented as a percentage.<br>
You can have a quick glance at some of our features through the gif below. <br>
We invite you to explore our comprehensive feature list by watching the detailed YouTube video we have provided. <br>
![](project_flow.gif)

## CORE FEATURES
Here are our core features:
1. Text analysis (with enhanced accuracy in the latest version): Text analysis module accepts text string as input, analyses it using TextBlob and presents the output as positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.
2. Document analysis: Document analysis module accepts a PDF document as input, analyses it and presents the output as positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.
3. Tweet analysis (new feature): Tweet analysis accepts the link to a tweet as input, analyses it using TextBlob and BeautifulSoup and presents the output as as graph which displays positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.
4. Image analysis(new feature): Image analysis accepts a jpeg/jpg/png format images as input, analyses it using OpenAI, CLIP and torch, and presents the output as as graph which displays positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.
5. Audio analysis: Audio analysis accepts a wave (.wav) format audio file as input, analyses it using speech recognition and SentimentIntensityAnalyzer and presents the output as as graph which displays positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.
6. Product review analysis: This module accepts a product review link as input, analyses it using scrapy and presents the output as as graph which displays positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.
All of the above, now presented in a more user-friendly interface
7. Video analysis: Video analysis accepts a video file as input, analyses it using video sentiment analysis model and presents the output as a graph which displays positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.
8. Blog analysis: Blog analysis accepts a blog link as input, analyses it using scrapy and presents the output as as graph which displays positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.
9. Restaurant review analysis: Restaurant review analysis accepts a restaurant review link as input, analyses it using scrapy and presents the output as as graph which displays positive sentiment percentage, negative sentiment percentage and neutral sentiment percentage.

## How is C.E.L.T Plus different from C.E.L.T? Read all about our feature additions and enhancements!
C.E.L.T Plus has undergone significant improvements that elevate this version to a higher level. Our team has meticulously designed and integrated a multitude of new features, both major and minor, to ensure that users of C.E.L.T Plus are provided with superior performance and functionality.<br>
### Major Enhancements<br>
1. Video Analysis: The first major feature we worked on was to add the Video Analysis. This feature accepts the video file as the input to be analyzed and returns the sentiment of the video after analyzing it. It can be found under the Video header in the UI and can also be accessed by the Video Analysis container in the Home page.
2. Blog Analysis: The second major feature we worked on was to add the Blog Analysis. This feature accepts the blog link as the input to be analyzed and returns the sentiment of the blog after analyzing it. It can be found under the Blog header in the UI and can also be accessed by the Blog Analysis container in the Home page.
3. Restaurant Review Analysis: The third major feature we worked on was to add the Restaurant Review Analysis. This feature accepts the restaurant review link as the input to be analyzed and returns the sentiment of the restaurant review after analyzing it. It can be found under the Restaurant Review header in the UI and can also be accessed by the Restaurant Review Analysis container in the Home page.<br>
### Minor Enhancements<br>
1. The User Interface was improved to make it more user-friendly.
2. The requirements.txt file was modified to download the packages with the versions >= the ones being mentioned to enable forward compatibility. 
3. Documentation was added to the code to make it more readable and understandable.
<br>

## Release Made in this cycle <br>
1. Critical release 1.0 - Initial release of the application with all the major features.
2. Release 2.0 - Included UI for new features and fixed issues with inputs in some of the features<br>
[Read our detailed release notes](https://github.com/blackhawk005/C.E.L.T_plus/releases) <br>
<br>

## Technology Stack
![Python](https://img.shields.io/badge/PYTHON-6DA55F?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/DJANGO-2320232?style=for-the-badge&logo=django)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Scrappy](https://img.shields.io/badge/SCRAPPY-23404d?style=for-the-badge&)
![Vader Analysis Tool](https://img.shields.io/badge/Vader%20Analysis%20Tool%20-%20%23750413?style=for-the-badge)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup%20-%20%235d60f0?style=for-the-badge)
![Textblob](https://img.shields.io/badge/TextBlob%20-%20%23b5af04?style=for-the-badge)

## Dependencies
Our requirements file has all packages that will be required. For details on all packages that were used, we invite you to read [Requirements](requirements.txt)



## Steps for execution
1. Run `pip install -r requirements.txt` followed by `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"`
2. Execute manage.py using the command `python3 manage.py runserver` at `/C.E.L.T_plus/sentimental_analaysis`. This runs the Django server such that we can open the webUI for the project on the browser.
3. Next, open your browser and type in `localhost:8000` in the search bar to open the webUI of the application.
4. You are now fully equipped to analyze sentiment across various data types, including text, documents, reviews, audio, images, and tweets.
5. If you face any issues while executing, refer this [VIDEO TUTORIAL](https://drive.google.com/file/d/17Bf7iwb8wPozZ53BUCVQEszitDcmSbSR/view?usp=share_link) to set the application up. We have also provided our group email address if you need more help towards the end of the file.


## FUTURE SCOPE

Implement user authentication to store history for each user.

Recommendation system based on analysis results.

Live speech to text sentiment analysis.

Extend the analysis to the Facebook and LinkedIn Posts

## Team Members

<table>
  <tr>
    <td align="center"><a href="https://github.com/aj0671"><img src="https://avatars.githubusercontent.com/u/84402767?v=4" width="75px;" alt=""/><br /><sub><b>Atharva Joshi</b></sub></a></td>
    <td align="center"><a href="https://github.com/shubham-wawale/"><img src="https://avatars.githubusercontent.com/u/63787850?s=400&u=c11a5c9bae68a18540bcb487a3769bd2c4b2ba29&v=4" width="75px;" alt=""/><br /><sub><b>Shubham Wawale</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sal0ni"><img src="https://avatars.githubusercontent.com/u/64455311?v=4" width="75px;" alt=""/><br /><sub><b>Sahil Purohit</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Sahil-18"><img src="https://avatars.githubusercontent.com/u/65714335?v=4" width="75px;" alt=""/><br /><sub><b>Shinit Shetty</b></sub></a><br /></td>
  </tr>
</table>

## Troubleshooting and Support
Common issues observed and solutions:<br>
1. requirements.txt failing: this issue should no longer be seen, as we have used ~= to ensure your systems pick up versions compatible with the other packages. However, if you happen to see the issue, modify the requirements.txt file to use a more recent version.
2. module manage.py not found: ensure you are inside the sentimental_analysis directory while attempting to run the module
3. python was not found: we recommend using python3 as some of the modules are available only on Python3. You may either install Python3 or setup a virtual environment(we suggest the latter if you are currently running other applications on python2)
Facing other issues with the application? Mail us - [celtplus63@gmail.com](celtplus63@gmail.com)
