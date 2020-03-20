import logging

logging.basicConfig(filename='./app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

import constants
from data_transformation import DataTransformation
from model import Model
from data_ingestion import DataIngestion
from similarity_calculation import Similarity


def main():
    try:
        data_transformation = DataTransformation(constants.data_dir)
        logging.info('Data is being processed and getting transformed')
        data_transformation.parse_data()
        user_assessment_scores_tab = data_transformation.transform_user_assessment_scores()
        user_course_views_tab = data_transformation.transform_user_course_views()
        user_interests_tab = data_transformation.transform_user_interests()
        agg_df = data_transformation.aggregate_data(user_course_views_tab, user_interests_tab,
                                                    user_assessment_scores_tab)
        logging.info('Applying SVD')
        model = Model()
        (users, _, _) = model.train(agg_df)
        logging.info('Calculating similarity matrix and saving the csv')
        similarity = Similarity(constants.file_name)
        similarity.create_similarity_matrix(users, agg_df)
        logging.info('Ingesting data into postgres')
        ingestion = DataIngestion()
        ingestion.create_table()
        ingestion.insert_values(constants.file_name)
        logging.info('Process completed')
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()

