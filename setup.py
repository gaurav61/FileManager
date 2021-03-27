from setuptools import setup, find_packages
setup(
    name = 'fm',
    version = '1.0',
    scripts = ['./script/fm'],
    author = 'Gaurav Arora',
    description = ('File manager'),
    packages = ['fm'],
    install_requires=[
        'setuptools',
        'PyPDF2 >= 1.26.0',
        'Pillow >= 7.0.0'
    ],
    python_requires='>=3.7'
)