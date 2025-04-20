from setuptools import setup, find_packages # type: ignore

setup(
    name='engagelibrary',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'pandas'
    ],
)
