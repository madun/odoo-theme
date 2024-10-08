# __manifest__.py
{
    'name': 'Katharos Theme',
    'version': '1.0',
    'summary': 'Clean and modern theme',
    'description': 'Katharos means "clean" in Greece',
    'author': 'Madun',
    'depends': ['web'],
    'data': [
        'views/assets.xml',
        'templates/layout.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': False,
}
