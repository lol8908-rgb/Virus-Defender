"""
SafeGuard Setup - Installation & EXE Build für Windows
"""

from setuptools import setup, find_packages
from pathlib import Path

readme_file = Path(__file__).parent / "README.md"
readme_content = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="SafeGuard",
    version="1.0.0",
    description="Sicherer Antivirus-Scanner mit Python CLI",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author="lol8908-rgb",
    url="https://github.com/lol8908-rgb/Virus-Defender",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "click==8.1.7",
        "colorama==0.4.6",
        "watchdog==3.0.0",
        "psutil==5.9.8",
        "pycryptodome==3.19.0",
        "pyyaml==6.0.1",
    ],
    extras_require={
        "dev": [
            "pytest==7.4.3",
            "black==23.12.1",
            "pyinstaller>=6.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "safeguard=safeguard.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
