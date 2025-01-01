from setuptools import setup, find_packages

setup(
    name="paper_mill_analysis",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=1.3.0",
        "beautifulsoup4>=4.9.3",
        "requests>=2.26.0",
        "textblob>=0.15.3",
        "urllib3>=1.26.7",
    ],
    python_requires=">=3.8",
)