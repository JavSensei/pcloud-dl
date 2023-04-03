from setuptools import setup, find_packages
import os

os.system("pip install git+https://github.com/JavSensei/pycloud")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pcloud-dl",
    version="0.1.2b",
    author="JavierSC",
    description="pcloud downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JavSensei/pcloud-dl",
    packages=find_packages(),
    install_requires=["tqdm"],
    entry_points={'console_scripts': ['pcloud-dl=pcloud_dl.cli:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Utilities'
    ],
    python_requires=">=3.6",
)
