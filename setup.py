from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="c17hawke",
    description="A small package for dvc dl with tensorflow pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kantarjack/MLops_project2_tensorflow",
    author_email="kantar.jack@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3" ,
    ]
)