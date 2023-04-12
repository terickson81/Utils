from azure.identity import DefaultAzureCredential
from azure.mgmt.resourcegraph import ResourceGraphClient
from msrest.authentication import BasicAuthentication

# Set up Azure credentials
credential = DefaultAzureCredential()

# Set up the resource graph client
resource_graph_client = ResourceGraphClient(credential)

# Query the Azure Resource Graph API to get all connected devices in the VNET
query = "where type =~ 'microsoft.network/networkinterfaces' | where properties.ipConfigurations[0].id startswith '/subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.Network/virtualNetworks/<vnet_name>' | extend vmId = tostring(properties.virtualMachine.id) | project id, vmId"
query_response = resource_graph_client.resources(query)

# Extract the IDs of all connected devices from the query response
connected_devices = [resource['id'] for resource in query_response]

# Print the list of connected devices
print(connected_devices)


from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.models import NetworkInterfaceIPConfiguration

# Set up Azure credentials
credential = DefaultAzureCredential()

# Set up the network management client
network_client = NetworkManagementClient(credential, subscription_id)

# Get the list of all network interfaces in the subscription
network_interfaces = network_client.network_interfaces.list_all()

# Filter the list of network interfaces to only include those connected to the VNet
vnet_interfaces = [iface for iface in network_interfaces
                   if any(isinstance(ip_conf.subnet, NetworkInterfaceIPConfiguration)
                          and ip_conf.subnet.id.startswith(f'/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{vnet_name}')
                          for ip_conf in iface.ip_configurations)]

# Extract the IDs of all connected devices from the list of network interfaces
connected_devices = [iface.id for iface in vnet_interfaces]

# Print the list of connected devices
print(connected_devices)
