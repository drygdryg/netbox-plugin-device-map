from django.conf import settings

from . import config

# Overlay custom settings over default settings
plugin_settings = config.default_settings | settings.PLUGINS_CONFIG[config.name]
plugin_settings['geomap_settings'] = config.default_settings['geomap_settings'] | plugin_settings['geomap_settings']
