## Usage
1. First add data folder and change the value in constants file
2. Create a database schema and modify the config file.
3. Install dependencies from requirements.txt
4. Run driver file(python driver.py) check the pipeline in log (app.log)
5. After successful ingestion run the app (python app.py) flask application starts


## Signature of API

localhost:5000/get_similar_users?user_handle=1&num_users=10

Response:
{
    'user_handle': int
    'similar_users': list
}

