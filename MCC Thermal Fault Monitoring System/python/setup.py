from setuptools import setup, find_packages

setup(
    name="MMC-TFDS",         # Package/project name
    version="0.1.0",                  # Version string
    author="UVIC Mining Club",
    description="libary to help control our sensor",
    long_description=open("README.md").read(),  # Often the README
    long_description_content_type="markdown",
    url="https://github.com/Uvic-Mining-Club/UvicMiningTech",  # Optional project URL
    packages=find_packages(),         # Automatically find packages/modules
    install_requires=[                # Dependencies
        "numpy",
        "matplotlib",
        "smbus2"
    ],
    classifiers=[                     # Metadata for PyPI
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",          # Minimum Python version
)