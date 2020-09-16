import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CM_text_sdk_python", # Replace with your own username
    version="1.0.0",
    author="Joris Pennings",
    author_email="joris.pennings@cm.com",
    description="Python SDK for text with CM.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cmdotcom/text-sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
