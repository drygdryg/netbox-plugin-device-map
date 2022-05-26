from dcim.models import Device
from django.db.models import QuerySet, Q
from ipam.models import VLAN

from .settings import plugin_settings


LOCATION_CF_NAME = plugin_settings['device_geolocation_cf']
LatLon = tuple[float, float]


def get_device_location(device: Device) -> LatLon | None:
    """Extract device geolocation from special custom field"""
    if location_cf := device.custom_field_data.get(LOCATION_CF_NAME):
        return tuple(map(float, location_cf.replace(' ', '').split(',', maxsplit=1)))


def get_connected_devices(device: Device, vlan: VLAN = None) -> QuerySet[Device]:
    """Get list of connected devices to the specified device.
    If the vlan is specified, return only devices connected to the interfaces of the specified device
    containing the specified VLAN"""
    included_interfaces = device.interfaces.all()
    if vlan is not None:
        included_interfaces = included_interfaces.filter(Q(untagged_vlan=vlan) | Q(tagged_vlans=vlan))
    return Device.objects.filter(interfaces___link_peer_id__in=included_interfaces)


def are_devices_connected(device_a: Device, device_b: Device) -> bool:
    """Determines whether devices are connected to each other by a direct connection"""
    return bool(
        Device.objects.filter(interfaces___link_peer_id__in=device_a.interfaces.all(), id=device_b.id).values('pk')
    )
