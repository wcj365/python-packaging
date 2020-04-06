import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_stats_wcj365",  # Replace with your own username
    version="0.0.1",
    author="Jay Wang",
    author_email="wcj365@gmail.com",
    description="A simple descriptive statistics package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wcj365/simple-stats",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)