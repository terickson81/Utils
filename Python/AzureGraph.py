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
