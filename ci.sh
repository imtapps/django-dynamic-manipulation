#!/bin/bash

# verify user provided a name for the virtualenv
if [ -z "$1" ]; then
    echo "usage: $0 virtual_env_name"
    exit
fi
VIRTUALENV_NAME=$1

virtualenv $VIRTUALENV_NAME
. $VIRTUALENV_NAME/bin/activate

find . -name "*.pyc" -delete

rm -rf jenkins_reports
mkdir jenkins_reports
pip install -r requirements/ci.txt
python example/manage.py test --with-xunit --xunit-file=jenkins_reports/nosetests.xml --with-xcover --cover-package=dynamic_manipulation --xcoverage-file=jenkins_reports/coverage.xml
TEST_EXIT=$?
python example/manage.py harvest -a sample -S --verbosity=3 --with-xunit --xunit-file=jenkins_reports/lettuce.xml
LETTUCE_EXIT=$?
pep8 dynamic_manipulation > jenkins_reports/pep8.report
PEP8_EXIT=$?
pyflakes dynamic_manipulation > jenkins_reports/pyflakes.report
PYFLAKES_EXIT=$?
let JENKINS_EXIT="$TEST_EXIT + $LETTUCE_EXIT + $PEP8_EXIT + $PYFLAKES_EXIT"

if [ $JENKINS_EXIT -gt 2 ]; then
    echo "Test exit status:" $TEST_EXIT
    echo "Lettuce exit status:" $LETTUCE_EXIT
    echo "PEP8 exit status:" $PEP8_EXIT
    echo "Pyflakes exit status:" $PYFLAKES_EXIT
    echo "Exiting Build with status:" $EXIT
    exit $JENKINS_EXIT
fi
