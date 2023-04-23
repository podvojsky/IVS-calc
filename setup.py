from setuptools import setup

setup(
    name='ivscalc',
    version='1.0.0',
    author='Lukas Podvojsky',
    author_email='lukas.podvojsky@email.com',
    description='My awesome Python GUI application',
    py_modules=['src.calc_view', 'src.colors', 'src.math_lib'],
    entry_points={
        'console_scripts': [
            'ivscalc=src.calc_view:main',
        ],
    },
    data_files=[
        ('share/icons/hicolor/96x96/apps', ['src/icons/ivscalc-96.png']),
        ('share/applications', ['ivscalc.desktop']),
    ],
)
