import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="CodonCoordinates",
    version='0.0.1',
    author="Matthew Wells",
    description="A quick way of looking up SARS-COV2 coordinates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    classifiers=["Programming Language::Python::3"],
    install_requires=['pandas'],
    python_requires=">=3.6",
    entry_points={'console_scripts': ['nucleotide_finder=nucleotide_finder.nucleotide_finder:main']},
    zip_safe=False
)