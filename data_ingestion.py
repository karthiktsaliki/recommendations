import logging

logging.basicConfig(filename='./app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


import psycopg2
import pandas as pd
import constants
from io import StringIO
from config import config



class DataIngestion:
    """
    For creation of tables and inserting values in tables defined
    """
    def __init__(self):
        self.params = config()

    def insert_values(self, file):
        """
        Insert values in PostgreSQL server
        :param file: csv that have to saved
        :return: void
        """
        try:
            user_based_top_similarity_df = pd.read_csv(file)
            connection = psycopg2.connect(**self.params)
            sio = StringIO()
            sio.write(user_based_top_similarity_df.to_csv(index=None, header=None))
            sio.seek(0)

            #  Copy the string buffer to the database, as if it were an actual file
            with connection.cursor() as c:
                c.copy_from(sio, "users", columns=user_based_top_similarity_df.columns, sep=',')
                connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            logging.error('Error in inserting values', error)
            raise error
        finally:
            if connection is not None:
                connection.close()

    def create_table(self):
        """
        create tables in the PostgreSQL database
        :return: void
        """
        user_command = "CREATE TABLE users2 ( user_handle integer PRIMARY KEY , "
        for val in range(1, constants.top_k+1):
            col = 'top_' + str(val)
            user_command = user_command + col + ' integer not null, '
        user_command = user_command[:-2] + ')'
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**self.params)
            cur = conn.cursor()
            # create table
            cur.execute(user_command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            logging.error('Error in creating database', error)
            raise error
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    ingestion = DataIngestion()
    ingestion.create_table()
    ingestion.insert_values('user_top_similarity.csv')
    logging.info('Successfully inserted values in postgres')






