from extras.plugins import PluginConfig


class DeviceMapConfig(PluginConfig):
    name = 'netbox_device_map'
    verbose_name = 'Device map'
    version = '0.1'
    author = 'Victor Golovanenko'
    author_email = 'drygdryg2014@yandex.com'
    base_url = 'device-map'
    default_settings = {
        'device_geolocation_cf': 'geolocation',
        'cpe_device_role': 'CPE',
        'geomap_settings': {
            'attribution': 'Data by &copy; <a href="https://openstreetmap.org">OpenStreetMap</a>',
            'crs': 'EPSG3857',
            'tiles': {
                'url_template': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                'options': {
                    'subdomains': 'abc',
                }
            }
        }
    }


config = DeviceMapConfig
