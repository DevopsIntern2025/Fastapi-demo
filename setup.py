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
    include_package_data=True,
    description="A simple FastAPI app packaged for CI/CD demo",
    author="DevopsIntern2025",
    author_email="babitharani.s@gmail.com",
    entry_points={
        "console_scripts": [
            "fastapi-pr-demo=fastapi_pr_demo.main:app",
        ],
    },
)
