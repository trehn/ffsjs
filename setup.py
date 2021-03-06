from setuptools import setup

setup(
    name="ffsjs",
    version="1.0.0",
    description="bare bones JavaScript package manager for web development",
    author="Torsten Rehn",
    author_email="torsten@rehn.email",
    license="GPLv3",
    url="https://github.com/trehn/ffsjs",
    keywords=[
        "cdn",
        "cdnjs",
        "css",
        "downloader",
        "javascript",
        "manager",
        "minified",
        "mirror",
        "package",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    python_requires='>=3',
    install_requires=["requests"],
    py_modules=["ffsjs"],
    entry_points={'console_scripts': ["ffsjs=ffsjs:main"]},
)
