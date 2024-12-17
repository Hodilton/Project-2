from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="file_work",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    description="A package for file work functionality",
    author="Ilya Barsukov",
    author_email="your_email@example.com",
    url="https://github.com/your_username/file_work",
)