import re
import json
from jsonschema import validate
from yaml import load, SafeLoader
from .settings import CONFIG_PATH, CONFIG_FILE_TYPE, SCHEMA_PATH, VALIDATORS_PATH


def get_config_name(name):
    return re.sub('([a-z])([A-Z])', r'\1_\2', name).lower().split('_', 1)[1]


class AbstractValidator:
    """
    Defines essential validation that must be performed on all configuration files.
    """

    @staticmethod
    def read_config(filename):
        """
        Reads a configuration file parsing the file format defined in settings.py
        :param filename: The filename
        :return: Parsed configuration file
        """
        if CONFIG_FILE_TYPE.upper() == 'YAML':
            with open(CONFIG_PATH + filename + '.yaml') as json_config_file:
                return load(json_config_file.read(), Loader=SafeLoader)

        elif CONFIG_FILE_TYPE.upper() == 'JSON':
            with open(CONFIG_PATH + filename + '.json') as json_config_file:
                return json.loads(json_config_file.read())
        else:
            raise KeyError('Unsupported CONFIG_FILE_TYPE: ' + CONFIG_FILE_TYPE)

    @staticmethod
    def get_schema(filename):
        with open(SCHEMA_PATH + filename + '.json') as json_config_file:
            return json.loads(json_config_file.read())

    @staticmethod
    def get_validation_data(filename):
        with open(VALIDATORS_PATH + filename + '.yaml') as json_config_file:
            return load(json_config_file.read(), Loader=SafeLoader)

    @classmethod
    def setup_class(cls):
        cls.config_name = get_config_name(cls.__name__)
        cls.schema = cls.get_schema(cls.config_name)
        cls.json_config = cls.read_config(cls.config_name)

    def test_schema(self):
        """
        Schema must be defined for each configuration file and stored with the same name as the configuration file.
        """
        assert validate(self.json_config, self.schema) is None
