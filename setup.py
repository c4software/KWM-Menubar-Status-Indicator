from setuptools import setup

APP_NAME = "kwm-status-menu"
APP_VERSION = "0.5.0"
APP = ['menu_status.py']
DATA_FILES = ["icons/bsp.png", "icons/float.png", "icons/monocle.png"]
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "KWM Status Menu",
        'CFBundleIdentifier': "com.vbrosseau.kwm-status-menu",
        'CFBundleVersion': APP_VERSION,
        'CFBundleShortVersionString': APP_VERSION,
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
