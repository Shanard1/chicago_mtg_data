import yaml

config_loc = '/Users/Shane/settings/mtg_pricing.yaml'

config_f = open(config_loc, 'r')

config = yaml.load(config_f)

dev = config['dev']