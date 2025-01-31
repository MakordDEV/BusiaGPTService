from setuptools import setup, find_packages

setup(
    name="busiagptservice",  
    version="0.1.0",           
    author="MakordDEV",        
    author_email="makordikrom@gmail.com",  
    description="A simple Python library to interact with GPTs models",  
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown", 
    url="https://github.com/MakordDEV/BusiaGPTService",  
    packages=find_packages(),  
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    install_requires=[  
        'requests',  
    ],
)
