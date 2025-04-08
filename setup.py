from setuptools import setup, find_packages

setup(
    name="fastapi_pr_demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "httpx"
    ],
    entry_points={
        "console_scripts": [
            "fastapi-pr-demo=fastapi_pr_demo.main:app",
        ],
    },
)
