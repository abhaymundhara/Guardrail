from setuptools import setup, find_packages

setup(
    name="guardrail-sdk",
    version="0.1.0",
    description="Enterprise AI Firewall SDK for LLM safety",
    author="Guardrail Team",
    packages=find_packages(),
    install_requires=[
        "httpx>=0.24.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.22.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)
