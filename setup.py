import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='manager-sdk',
    version='0.0.1',
    author='José Marques',
    author_email='josepmarques@proton.me',
    description='SDK to make python scripts manageable',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jnmarques/python-script-manager',
    project_urls = {
        "Bug Tracker": "https://github.com/jnmarques/python-script-manager/issues"
    },
    license='Apache License 2.0',
    packages=['manager-sdk'],
    install_requires=['psutil'],
)