import logging

logging.basicConfig(filename='./app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

import pandas as pd
import os
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler



class DataTransformation:
    """
        Transforming given data to formulate the problem into collaborative filtering
    """
    def __init__(self, folder):
        self.data_dir = folder
        self.user_interests = pd.DataFrame()
        self.user_assessment_scores = pd.DataFrame()
        self.user_course_views = pd.DataFrame()
        self.min_max = MinMaxScaler()
        self.le = preprocessing.LabelEncoder()

    def parse_data(self):
        """
            Parsing the given data
            :return: None
        """
        try:
            self.user_interests = pd.read_csv(os.path.join(self.data_dir, 'user_interests.csv'))
            self.user_assessment_scores = pd.read_csv(os.path.join(self.data_dir, 'user_assessment_scores.csv'))
            self.user_course_views = pd.read_csv(os.path.join(self.data_dir, 'user_course_views.csv'))
        except Exception as e:
            logging.error(e)

    def transform_user_interests(self):
        """
            Cross tab on user_interests and taking count
            :return: cross tab data
        """
        try:
            user_interests_tab = pd.crosstab(self.user_interests.user_handle, self.user_interests.interest_tag,
                                             dropna=False)
            user_interests_tab.fillna(0, inplace=True)
            user_interests_tab[user_interests_tab > 0] = 1
            user_interests_tab = user_interests_tab.reset_index().rename_axis(None, axis=1)
            return user_interests_tab

        except Exception as e:
            logging.error(e)

    def transform_user_assessment_scores(self):
        """
            Cross tab on user_assessment and taking mean
            :return: cross tab data
        """
        try:
            self.user_assessment_scores['user_assessment_score'] = self.min_max.fit_transform(
                self.user_assessment_scores[['user_assessment_score']])
            user_assessment_scores_tab = self.user_assessment_scores.groupby(
                ['user_handle', 'assessment_tag'])['user_assessment_score'].mean().unstack()
            user_assessment_scores_tab.fillna(0, inplace=True)
            user_assessment_scores_tab = user_assessment_scores_tab.reset_index().rename_axis(None, axis=1)
            user_assessment_scores_tab.head()
            return user_assessment_scores_tab
        except Exception as e:
            logging.error(e)

    def transform_user_course_views(self):
        """
            Cross tab on user_course_views and taking mean
            :return: cross tab data
        """
        try:
            self.user_course_views['course_id'] = self.le.fit_transform(self.user_course_views.course_id)
            user_course_views_tab = self.user_course_views.groupby(['user_handle', 'course_id'])[
                'view_time_seconds'].sum().unstack()
            user_course_views_tab.fillna(0, inplace=True)
            user_course_views_tab = user_course_views_tab.reset_index().rename_axis(None, axis=1)
            user_course_views_tab.head()
            return user_course_views_tab
        except Exception as e:
            logging.error(e)

    def aggregate_data(self, user_course_views_tab, user_interests_tab, user_assessment_scores_tab):
        """
        aggregating cross tab data for users
        :param user_course_views_tab:
        :param user_interests_tab:
        :param user_assessment_scores_tab:
        :return: aggregated data
        """
        try:
            cols_to_scale = list(user_course_views_tab.columns)[1:]
            user_course_views_tab[cols_to_scale] = self.min_max.fit_transform(user_course_views_tab[cols_to_scale])
            aggregated_df = user_interests_tab.copy()
            aggregated_df = aggregated_df.merge(user_course_views_tab, on='user_handle', how='left')
            aggregated_df = aggregated_df.merge(user_assessment_scores_tab, on='user_handle', how='left')

            aggregated_df.fillna(0, inplace=True)
            return aggregated_df
        except Exception as e:
            logging.error(e)




