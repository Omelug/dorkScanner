from setuptools import setup, find_packages

setup(
    name='dork_scanner',
    version='0.1',
    packages=find_packages(),
    description='Simple dorkScanner',
    author='Omelug (authoer of fork), madhavmehndiratta (original author)',
    author_email='None',
    url='https://github.com/Omelug/dorkScanner',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='dork',
    install_requires=[
        'input_parser @ git+https://github.com/Omelug/python_mini_modules@master#egg=input_parser'
    ],
)