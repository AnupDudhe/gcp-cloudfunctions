from googleapiclient import discovery
from google.auth import default
import datetime

def create_instance(request):
    try:
        project = "bubbly-pillar-464015-r0"
        zone = "us-central1-c"
        instance_name = f"vm-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"

        machine_type = f"zones/{zone}/machineTypes/e2-micro"

        credentials, _ = default()
        service = discovery.build("compute", "v1", credentials=credentials)

        config = {
            "name": instance_name,
            "machineType": machine_type,
            "sourceMachineImage": f"projects/{project}/global/machineImages/test",
            "networkInterfaces": [
                {
                    "network": "global/networks/default",
                    "accessConfigs": [
                        {"type": "ONE_TO_ONE_NAT", "name": "External NAT"}
                    ],
                }
            ],
        }

        operation = service.instances().insert(
            project=project, zone=zone, body=config).execute()

        return f"✅ Instance creation started: {instance_name}, operation: {operation['name']}"

    except Exception as e:
        return f"❌ Error: {str(e)}"
