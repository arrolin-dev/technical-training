{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.0.1",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True,
    'license': 'LGPL-3',
}
