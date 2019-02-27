import os
from setuptools import setup,find_packages
    
setup(
    name='nitro-python',
    version='1.1',
    author='Citrix Netscaler',
    url='https://www.citrix.com/downloads/citrix-adc/sdks/netscaler-sdk-release-110.html',
    packages=[
        'nitro',
        'nitro.exception',
        'nitro.resource',
        'nitro.util',
        'nitro.service',
        'nitro.resource.base',
        'nitro.resource.config',
        'nitro.resource.stat'] + 
        [ os.path.join('nitro.resource.config', mydir) for mydir in find_packages("nitro/resource/config")] +
        [ os.path.join('nitro.resource.stat', mydir) for mydir in find_packages("nitro/resource/stat")],
    classifiers=[
          'Intended Audience :: NS Administrators',
          'Programming Language :: Python',
          'Topic :: Software Development :: API',
    ],
    description='Python SDK for Nitro API',    
    install_requires=[
        "requests >= 2.3.0",
    ]
)
