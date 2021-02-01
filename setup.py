import setuptools


setuptools.setup(
    name="ml_stat_util",
    version='0.0.1',
    author="Mateusz Buda",
    description="Machine Learning Statistical Utils",
    long_description="Machine Learning Statistical Utils",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=['test*']),
    package_dir={"ml_stat_util": "ml_stat_util"},
    include_package_data=True,
    install_requires=[
        "numpy>=1.16.2",
        "scikit-learn>=0.20.3",
    ],
    python_requires='>=3.5',
)
