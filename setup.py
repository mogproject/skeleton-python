from setuptools import setup, find_packages

setup(
    name='your-project-name',
    version='0.0.1',
    description='description for you project',
    author='your name',
    author_email='your email address',
    url='your url',
    install_requires=[
        # list your dependencies
    ],
    tests_require=[
        # dependencies for unit testing
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    test_suite='tests',
)
