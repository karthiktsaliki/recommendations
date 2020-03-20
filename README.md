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

### My similar work in recommendations

https://github.com/karthiktsaliki/Hikeathon_Analytics_Vidhya (Secured 17th rank world wide)
https://github.com/karthiktsaliki/IBM_Recommendations

