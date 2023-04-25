# from setuptools import setup

# setup(
#     name='ivscalc',
#     version='1.0.0',
#     author='xpodvo00-ivs-team',
#     author_email='xpodvo00@stud.fit.vutbr.cz',
#     description='Simple calculator app',
#     py_modules=['calc_view', 'colors', 'math_lib'],
#     entry_points={
#         'console_scripts': [
#             'ivscalc=calc_view:main',
#         ],
#     },
#     data_files=[
#         ('share/icons/hicolor/96x96/apps', ['icons/ivscalc-96.png']),
#         ('share/applications', ['ivscalc.desktop']),
#     ],
# )

from setuptools import setup

setup(
    name='stddev',
    version='1.0.0',
    author='xpodvo00-ivs-team',
    author_email='xpodvo00@stud.fit.vutbr.cz',
    description='Program for calculating a standard deviation',
    py_modules=['stddev', 'math_lib'],
    entry_points={
        'console_scripts': [
            'stddev=stddev:main',
        ],
    },
)
