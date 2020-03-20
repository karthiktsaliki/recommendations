import logging

logging.basicConfig(filename='./app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


import pandas as pd
import constants
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm



class Similarity:
    """
        For calculating and saving similarity matrix of users in csv
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def create_similarity_matrix(self, user, aggregated_df):
        """
        Save the similarity matrix in the csv data
        :param user:
        :param aggregated_df:
        :return: void
        """
        try:
            user_matrix = pd.DataFrame(user)
            user_matrix.index = aggregated_df['user_handle']
            user_sim_matrix = cosine_similarity(user_matrix)

            user_sim_matrix = pd.DataFrame(user_sim_matrix, columns=list(aggregated_df['user_handle']))

            user_sim_matrix['user_handle'] = aggregated_df['user_handle']

            user_sim_matrix.index = user_sim_matrix.user_handle.values

            cols_to_sort = user_sim_matrix.user_handle.tolist()

            user_based_top_similarity = []

            for val in tqdm(cols_to_sort):
                user_based_top_similarity.append(user_sim_matrix[val].
                                                 sort_values(ascending=False).index.tolist()[1:constants.top_k + 1])

            top_columns = ['top_' + str(ind) for ind in range(1, constants.top_k + 1)]

            user_sim_matrix.reset_index(inplace=True)
            user_based_top_similarity_df = pd.DataFrame(user_based_top_similarity, columns=top_columns)
            user_based_top_similarity_df['user_handle'] = user_sim_matrix['user_handle']
            user_based_top_similarity_df.to_csv(self.file_name, index=False)

        except Exception as e:
            logging.error('Error in create_similarity_matrix', e)
            raise e


