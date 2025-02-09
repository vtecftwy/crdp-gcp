from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

extensions = [
    Extension('crdp', ['crdp.pyx']),
]

try:
    from Cython.Build import cythonize
    extensions = cythonize(extensions,
                           compiler_directives={
                               'language_level': 3
                           })
except ImportError:
    pass


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="crdp-gcp",
    version="0.0.4",
    author="Ran Bi",
    author_email="biran0079@gmail.com",
    description="A fast Ramer-Douglas-Peucker algorithm implementation. Updated for GCP cloud function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vtecftwy/crdp-gcp",
    keywords="rdp ramer douglas peucker line simplification cython",
    license="MIT",
    packages=(
            find_packages()
    ),
    install_requires=['cython'],
    extras_require=dict(
        dev=[
            'cython',
        ],
    ),

    ext_modules=extensions,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
