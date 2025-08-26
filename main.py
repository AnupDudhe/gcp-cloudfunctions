from googleapiclient import discovery
from google.auth import default
import datetime

def create_gce_snapshot(request):
    try:
        project = "bubbly-pillar-464015-r0"
        zone = "us-central1-c"
        disk = "webserver"   # ✅ updated disk name

        snapshot_name = f"{disk}-snapshot-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"

        credentials, _ = default()
        service = discovery.build('compute', 'v1', credentials=credentials)

        snapshot_body = {
            "name": snapshot_name,
            "description": "Automated snapshot from Cloud Function"
        }

        response = service.disks().createSnapshot(
            project=project,
            zone=zone,
            disk=disk,
            body=snapshot_body
        ).execute()

        return f"✅ Snapshot started: {snapshot_name}, operation: {response['name']}"

    except Exception as e:
        return f"❌ Error: {str(e)}"

