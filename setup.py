import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("CMText/version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="CM_text_sdk_python", # Replace with your own username
    version=version['__version__'],
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
