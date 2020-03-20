import logging

logging.basicConfig(filename='./app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


from configparser import ConfigParser



def config(filename='database.ini', section='postgresql'):
    """
    To return the params in the database
    :param filename: database config
    :param section: postgres section in config
    :return: database params
    """
    try:
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
 
        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
        return db
    except Exception as e:
        logging.error(e)