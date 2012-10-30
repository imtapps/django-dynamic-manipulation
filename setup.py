from distutils.core import setup
from setuptools import find_packages
from dynamic_manipulation import VERSION


setup(
    name="django-dynamic-manipulation",
    version=VERSION,
    author="imtapps",
    author_email="webadmin@imtapps.com",
    description="Record rule based dynamic manipulations.",
    long_description=file('README.txt', 'r').read(),
    url="https://github.com/imtapps/django-dynamic-manipulation",
    packages=find_packages(exclude=["example"]),
    install_requires=file('requirements/dist.txt', 'r').read(),
    zip_safe=False,
    include_package_data=True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ]
)

