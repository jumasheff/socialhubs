#!/bin/bash
set -e

. venv/bin/activate
cd apps


# acceptance tests
RUN_TEST_COMMAND="./manage.py harvest acceptance_tests/features --settings=main.settings_test --debug-mode --with-xunit --xunit-file=../testres.xml"
for var in ${@}
do
    RUN_TEST_COMMAND=${RUN_TEST_COMMAND}" -t ${var}"
done
bash -c "${RUN_TEST_COMMAND}"
deactivate