from setuptools import find_packages, setup

setup(
    name="mathapi",
    version="0.1.0",
    description="Yet another math api",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=[
        "flask",
        "SQLAlchemy",
        "alembic",
    ],
)
