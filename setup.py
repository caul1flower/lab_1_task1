import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skyscrapers-caul1flower",
    version="0.0.1",
    author="Anita Hrodzytska",
    author_email="hrodzytska@ucu.edu.ua",
    description="Task 1, lab 1 (II semester)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caul1flower/lab_1_task1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.5',
)