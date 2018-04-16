"""Creates a Cloud Storage bucket template for Forseti Security."""

def GenerateConfig(context):
    """Generate configuration."""
    resources = []

    resources.append({
        'name': context.env['name'],
        'type': 'storage.v1.bucket',
        'properties': {
            'project': context.env['project'],
            'location': context.properties['location'],
        }
    })

    return {'resources': resources}
