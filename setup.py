from setuptools import setup, find_packages

#* Empaquetamos nuestra aplicación

setup(
    name="my_fastapi_app",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn"
    ],
    entry_points={
        "console_scripts": [
            "my_fastapi_app_run=my_fastapi_app.app:run_server"
        ]
    }
)
