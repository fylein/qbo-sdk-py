"""
Project setup file
"""
import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='qbosdk',
    version='0.14.0',
    author='Shwetabh Kumar',
    author_email='shwetabh.kumar@fyle.in',
    description='Python SDK for accessing Quickbooks Online APIs',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['quickbooks-online', 'quickbooks', 'fyle', 'api', 'python', 'sdk'],
    url='https://github.com/fylein/qbo-sdk-py',
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.25.0', 'future==0.18.2'],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
