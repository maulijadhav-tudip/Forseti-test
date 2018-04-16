"""Creates a Cloud SQL database template for forseti_inventory."""


def GenerateConfig(context):
    """Generate configuration."""

    resources = []

    resources.append({
        'name': context.env['name'],
        'type': 'sqladmin.v1beta4.database',
        'properties': {
            'name': context.env['name'],
            'project': context.env['project'],
            'instance': '$(ref.cloudsql-instance.name)'
        }
    })

    return {'resources': resources}
