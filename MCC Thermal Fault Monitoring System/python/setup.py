from setuptools import setup, find_packages

def load_requirements(filename):
    with open(filename) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

setup(
    name="MMC-TFDS",
    version="0.1.0",
    author="UVIC Mining Club",
    description="Library to help control our sensor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Uvic-Mining-Club/UvicMiningTech",
    packages=find_packages(),
    install_requires=load_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)
