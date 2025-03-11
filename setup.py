from setuptools import setup, find_packages

setup(
    name="Liyev",  
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Okanliyev",
    author_email="Okanliyev@gmail.com",
    description="Bu kitabxana modulu python'a sadə və lazımlı funksiyalar əlave edir. əsas məqsədi iç içə keçmiş çoxlu fnksiyaların qarşısını almaqdı.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Okanliyev/Liyev-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
