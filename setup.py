from setuptools import setup, find_packages

setup(
    name="swarmpulse",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.20.0",
        "sqlalchemy>=2.0.0",
        "pandas>=1.5.0",
        "requests>=2.28.0",
        "plotly>=5.13.0"
    ],
    entry_points={
        "console_scripts": [
            "swarmpulse-dash=swarmpulse.app:main",
        ],
    },
)
