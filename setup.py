from setuptools import setup

REQUIREMENTS = [
    'django',
    'django-dynamic-rules',
]
TEST_REQUIREMENTS = [
    'mock',
    'lettuce',
    'pyhamcrest',
]

setup(
    name="django-dynamic-manipulation",
    version='0.0.1',
    author="Matthew J Morrison & Aaron Madison",
    author_email="mattjmorrison@mattjmorrison.com",
    description="Record rule based dynamic manipulations.",
    long_description=open('README.txt', 'r').read(),
    url="https://github.com/imtapps/django-dynamic-manipulation",
    packages=("dynamic_manipulation",),
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
