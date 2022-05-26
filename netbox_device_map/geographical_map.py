from dcim.models import Device

from .settings import plugin_settings
from .helpers import get_connected_devices, LatLon


geomap_settings = plugin_settings['geomap_settings']
CPE_DEVICE_ROLE_NAME = plugin_settings['cpe_device_role']


def configure_leaflet_map(map_id: str, devices: dict[Device, LatLon], calculate_connections=True) -> dict:
    """Generate Leaflet map of devices and the connections between them.
    :param map_id: initialize the map on the div with this id
    :param devices: list of target devices to display on the map
    :param calculate_connections: calculate connections between devices
    """
    device_id_to_latlon = {device.id: position for device, position in devices.items()}
    map_config = dict(**geomap_settings, map_id=map_id)
    markers: list[dict] = []
    connections: set[frozenset[LatLon, LatLon]] = set()
    for device, position in devices.items():
        markers.append(dict(
            position=position,
            icon=device.device_role.slug,
            device=dict(
                id=device.id,
                name=device.name,
                url=device.get_absolute_url(),
                role=device.device_role.name
            )
        ))
        if calculate_connections:
            for peer_device_id in get_connected_devices(device).values_list('id', flat=True).order_by():
                if peer_position := device_id_to_latlon.get(peer_device_id):
                    connections.add(frozenset((position, peer_position)))

    map_config.update(markers=markers, connections=[tuple(c) for c in connections])

    return map_config
