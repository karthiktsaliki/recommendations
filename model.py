import logging

logging.basicConfig(filename='./app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

import scipy


class Model:
    def __init__(self, **params):
        self.params = params

    def train(self, aggregated_df):
        """
        Applying an SVD on the data
        :param aggregated_df:
        :return:
        """
        try:
            return scipy.linalg.svd(aggregated_df)
        except Exception as e:
            logging.error('Error in applying svd', e)
            raise e

