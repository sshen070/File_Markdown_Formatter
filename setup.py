from setuptools import setup, find_packages

setup(
    name="markdown_cleaner",
    version="0.1.0",
    author="Sujith Shen",
    author_email="SujithShen@gmail.com",
    description="A Python utility that cleans poorly structured Markdown strings/files.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sshen070/File_Markdown_Formatter.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "markdown-cleaner=markdown_formatter_sshen070.main:main_str",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
