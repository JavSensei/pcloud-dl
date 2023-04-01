from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pcloud-dl",
    version="0.1.0",
    author="JavierSC",
    description="pcloud downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JavSensei/pcloud-dl",
    packages=["<nombre_del_paquete>"],
    install_requires=["git+https://github.com/JavSensei/pycloud","tqdm"],
    entry_points={'console_scripts': ['pcloud-dl=pcloud_dl.cli:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Utilities'
    ],
    python_requires=">=3.6",
)
