import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discord-boost",
    version="1.0.0",
    author="SYCK",
    author_email="oviyangandhi@gmail.com",
    description="A small package for beginner discord.py coders to handle server boosts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SYCKstudios/discordboost",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)