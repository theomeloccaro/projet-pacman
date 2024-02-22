import configparser

class ConfigLoader:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_value(self, section, key, data_type=str, tuple_delimiter=':', value_delimiter=','):
        """
        Récupérer la valeur d'une clé dans une section.
        :param section: Nom de la section
        :param key: Clé à récupérer
        :param data_type: Type de données attendu (par défaut, str)
        :param tuple_delimiter: Délimiteur pour séparer les tuples (par défaut, ':')
        :param value_delimiter: Délimiteur pour séparer les valeurs dans un tuple (par défaut, ',')
        :return: Valeur de la clé dans la section
        """
        try:
            if data_type == int:
                return self.config.getint(section, key)
            elif data_type == float:
                return self.config.getfloat(section, key)
            elif data_type == bool:
                return self.config.getboolean(section, key)
            elif data_type == tuple:
                tuple_values = self.config.get(section, key).split(tuple_delimiter)
                result = [tuple(map(int, value.split(value_delimiter))) for value in tuple_values]
                return tuple(result)
            else:
                return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {e}")
            return None