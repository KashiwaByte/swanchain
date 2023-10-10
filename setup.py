from setuptools import find_packages, setup
setup(
    name='swanchain',
    packages=find_packages(),
    version='0.1.0',
    description='swanchain first Python library',
    author='KashiwaByte',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)