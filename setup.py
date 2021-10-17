"""UserConf Setup script
"""

import setuptools


if __name__ == "__main__":
    with open("README.md", "r") as f:
        long_desc = f.read()

    setuptools.setup(
        name="userconf",
        version="0.4.0",
        description="Application user settings management library",
        author="Jose A. Jimenez",
        author_email="jajimenezcarm@gmail.com",
        license="MIT",
        long_description=long_desc,
        long_description_content_type="text/markdown",
        url="https://github.com/jajimenez/userconf",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: MIT License"
        ],
        python_requires=">=3.9.0",
        packages=["userconf"],
        package_dir={"userconf": "src/userconf"}
    )
