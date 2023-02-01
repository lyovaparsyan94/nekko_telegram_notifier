import yaml


class ConfigLoader:

    @staticmethod
    def config_loader(config_file):
        with open(config_file) as stream:
            config = yaml.safe_load(stream=stream)
        return config

