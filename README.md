## User Similarity

In this project I am dealing with the users dataset. I have given a challenge to find the similarities of existing users
based on their interest, assessments or actions.


### Github Link

https://github.com/karthiktsaliki/recommendations

### Libraries used


* pandas: Pandas is a software library written for the Python programming language for data manipulation and analysis.

* sklearn: Machine learning library for the Python programming language. It features for classification and regression.

* scipy: A library mostly used for training svd.

* psycopg2: For connecting to postgresql

### Motivation

User similarity is the first stage in Recommender systems for performing collaborative filtering.


### Approach

At first I transformed the given data into a user by feature matrix then I applied SVD on top of that
and finally I perfomed the similarity check to create user by user similarity matrix. Ingested the data into postgres.
I exposed an API for getting similar users for given users


### Results

Developed a web application which takes the user_id and num_similar_users as the parameters and returns the similar
users as response

### Usage

https://github.com/karthiktsaliki/recommendations/blob/master/usage_guide.md

### Answers

1. Cosine similarity looks at the angle between two vectors. Let's say you have users who have scored photoshop, angular, javascript, react, tensorflow 

 * User 1  10 photoshop, 30 angular, 50 react
 * User 2  10 photoshop,  10 tensorflow, 10 pytorch 
 * User 3  30 photoshop, 50 angular, 70 react

By cosine similarity, user 1 and user 3 are more similar. By euclidean similarity, user 2 is more similar to user 1.

2. Actually I am not getting that high magnitude in similarity it will be really accurate if we have more data and we should be even consider some map reduce techniques in transforming data.

3. We can give recommendations of courses to users. In what ways they are similar. If a new user comes in what courses should I recommend this can all be taken into future enhancements. I would like to collect demographics of users to provide some insights ,   some more information(content) on courses and more information on authors.


### Future enhancements

* We can do some time based feature engineering, add extra course tags into account.

* Do featue transformation on authors. I neglected this but this might add relevance few users might be biased to authors.

* Provide recommendations of courses to users

### Files

* app.py the flask application runs on 5000 port

* driver.py which runs all the steps and saves the similarity data in postgres

* data_ingestion.py for creating and storing data in postgres

* data_transformation.py for transforming the give data to apply cf

* user_similarity.py which does the similarity between users and saves it in the csv

* model.py apply svd on the given data
 
* database.ini database config information

* config.py which parses the config of database.ini and return the params of postgres

### My similar work in recommendations

https://github.com/karthiktsaliki/Hikeathon_Analytics_Vidhya (Secured 17th rank world wide)
https://github.com/karthiktsaliki/IBM_Recommendations

