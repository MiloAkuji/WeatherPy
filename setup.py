from setuptools import setup, find_packages

setup(
    name='WeatherPy',
    version='1.0.0',
    author='Milo',
    author_email='miloakuji@gmail.com',
    description='A Python module to retrieve and display weather information using the OpenWeatherMap API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MiloAkuji/WeatherPy',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
