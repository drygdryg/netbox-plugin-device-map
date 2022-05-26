from django import forms

from dcim.models import DeviceRole, Device
from ipam.models import VLANGroup, VLAN
from utilities.forms import BootstrapMixin, DynamicModelChoiceField, DynamicModelMultipleChoiceField


class DeviceMapFilterForm(BootstrapMixin, forms.Form):
    vlan_group = DynamicModelChoiceField(
        queryset=VLANGroup.objects.all(),
        required=False,
        label="VLAN group",
        help_text="VLAN group for VLAN selection"
    )
    vlan = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        label="VLAN",
        help_text="Filter devices by VLAN attached to any device interface",
        query_params={"group_id": "$vlan_group"}
    )
    device_roles = DynamicModelMultipleChoiceField(
        queryset=DeviceRole.objects.all(),
        required=False,
        label="Device roles",
        help_text="Display devices of only the specified device roles"
    )
    calculate_connections = forms.BooleanField(
        required=False,
        label="Calculate connections between devices",
        initial=True
    )


class ConnectedCpeForm(forms.Form):
    vlan = forms.ModelChoiceField(queryset=VLAN.objects.all(), required=False)
