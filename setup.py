from setuptools import setup

APP_NAME = "kwm-status-menu"
APP = ['menu_status.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "KWM Status Menu",
        'CFBundleIdentifier': "com.vbrosseau.kwm-status-menu",
        'CFBundleVersion': "0.4.0",
        'CFBundleShortVersionString': "0.4.0",
        'NSHumanReadableCopyright': u"Valentin Brosseau"
    },
    'iconfile': 'app.icns',
    'packages': [],
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
