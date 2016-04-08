# RedditGildedComments

## Team members:

Joanne Kim

Rebecca Mahany

## Project description:

We plan to analyze the content of Reddit gilded text comments to discover commonalities among gilded content. The three main factors to be analyzed are upvotes/downvotes, length, and language. We will analyze the language using NLTK, and will analyze the data as a whole using pandas and/or NumPy. (We will not be considering image-only comments, and we will not be considering posts themselves.) We plan to take this data from a publicly available compilation of all Reddit comments before July 2015.

Using the results of our analysis, we will identify the criteria that may predict whether a comment will be gilded; we will create graphs that illustrate our findings. We will train and test our program using these criteria. 

We will then monitor rising threads in r/all in real time to attempt to identify comments that will be gilded.

## Project major components:

1. Gather and parse data in a .csv file.

2. Analyze correlation between gilding and upvotes/downvotes,  correlation between gilding and the length of the comment, and correlation between gilding and the language used in the comment. Analyze findings, weigh the above relations in magnitude of their impact to develop a clear trend for gilding. Produce graphs to visualize data.

3. With that information, train and test our program to identify gilded comments based on their up/downvotes, length, and language. 

4. Monitor a select number of threads to predict comments that will be gilded.

## Division of responsibilities:

* Download and parse Reddit comments into a usable form: Joanne

* Analysis of up/downvotes’ effect on gilding: Rebecca

* Analysis of length’s effect on gilding: Joanne

* Analysis of language’s effect on gilding: Rebecca

* Create graphs to visualize findings: Rebecca and Joanne

* Identify criteria that can predict whether a comment is gilded: Joanne

* Train program on training set of comments; same with testing on test set: Rebecca

* For “rising” threads in r/all, identify which comments are most likely to be gilded: Joanne, Rebecca

* Optimization for space/time complexity: Each person is responsible for optimizing code they’ve written

* Write test suite: Each person writes unit tests for the code they’ve written
* 
* Documentation: Each person is responsible for documenting code they've written

## Packages used:

NLTK, pandas, scikit-learn, NumPy

## Timeline:

April 10: Finalize sections of NLTK to be used; research and choose Python packages to visualize and analyze data (Rebecca)

April 10: Data parsed into a usable form (component #1) (Joanne)

April 15: Turn in proposal

April 17: All data analysis sections (component #2) done (Joanne, Rebecca)

April 19: Identified criteria that can predict whether a comment will be gilded (Joanne)

April 21: Training/testing (component #3) complete (Rebecca) 

May 1: Prediction (component #4) complete (Joanne, Rebecca)

May 4: All test suites written; all graphs created; all documentation complete (Joanne, Rebecca)

May 5: All optimization for space/time complexity complete (Joanne, Rebecca)

May 9: Project due

# Documentation

TBD
