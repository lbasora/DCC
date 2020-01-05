from setuptools import setup, find_packages

setup(
    name="dcc",
    version="0.1",
    author="Sohil Atul Shah and Vladlen Koltun",
    url="https://github.com/lbasora/DCC/",
    description="Deep Continuous Clustering",
    license="MIT",
    packages=find_packages(),
    install_requires=["torch", "tensorboardX", "tensorboard-logger"],
    python_requires=">=3.6",
)
