from setuptools import setup, find_packages

setup(
    name='substring_search_ex',
    version='0.1.0',
    description='Experiments for testing substring search algorithms.',

    author='Vladislav Zaripov',
    author_email='Please use vladislavzaripov.vz@gmail.com contact form.',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['attrs==20.2.0',
                      'certifi==2020.6.20',
                      'cycler==0.10.0',
                      'iniconfig==1.0.1',
                      'kiwisolver==1.2.0',
                      'matplotlib==3.3.2',
                      'more-itertools==8.5.0',
                      'numpy==1.19.2',
                      'packaging==20.4',
                      'Pillow==7.2.0',
                      'plotly==4.10.0',
                      'pluggy==0.13.1',
                      'py==1.9.0',
                      'pycodestyle==2.6.0',
                      'pyparsing==2.4.7',
                      'pytest==6.0.2',
                      'python-dateutil==2.8.1',
                      'retrying==1.3.3',
                      'scipy==1.5.2',
                      'six==1.15.0',
                      'toml==0.10.1',
                      'memory-profiler==0.57.0'],

    entry_points={
        'console_scripts': [
            'substring_search_ex = manager',
        ]
    },
)
