#!/bin/bash

python3 manage.py loaddata users/fixtures/users.json
python3 manage.py loaddata courses/fixtures/courses.json
python3 manage.py loaddata courses/fixtures/course_progress.json
python3 manage.py loaddata jobs/fixtures/jobs.json
