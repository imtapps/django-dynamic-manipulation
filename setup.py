from setuptools import setup, find_packages

REQUIREMENTS = open('dependencies.txt', 'r').read().split('\n')
TEST_REQUIREMENTS = open('test_dependencies.txt', 'r').read().split('\n')

setup(
    name="django-dynamic-manipulation",
    version='0.0.2',
    author="Matthew J Morrison & Aaron Madison",
    author_email="mattjmorrison@mattjmorrison.com",
    description="Record rule based dynamic manipulations.",
    long_description=open('README.txt', 'r').read(),
    url="https://github.com/imtapps/django-dynamic-manipulation",
    packages=find_packages(exclude=["example"]),
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    test_suite='runtests.runtests',
    zip_safe=False,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
