from setuptools import setup, find_packages
setup(
    name='citybike-Rentsch',
    version='0.0.1',
    author='C. Rentsch',
    author_email='christele.rentsch@gmail.com',
    packages=['citybike'],
  
    url='http://pypi.python.org/pypi/CityBike/',
        
    classifiers=[
        "Programming Language :: Python",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications"
    ],
    install_requires = [
        "numpy",
        "pandas",
        "pyspark",
        "spark >= 2.4"
    ]
)