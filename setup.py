import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybtmsdk",
    version="0.1.9",
    author="ipqhjjybj",
    author_email="250657661@qq.com",
    description="Python3 implementation of the Bytom protocol. Some Code Fork From pybtm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bytom/python-bytomlib",
    #packages=setuptools.find_packages(),
    packages=setuptools.find_packages(exclude=["example"]),  # 包
    install_requires=[
        "ed25519>=1.4",
        "pbkdf2>=1.3",
        "pybase64>=0.5.0",
        "qrcode>=6.1",
        "sha3>=0.2.1",
        "six>=1.12.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)