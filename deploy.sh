#!/usr/bin/env bash
# .secrets를 staging area에 추가

pipenv lock --requirements > requirements.txt
git add -A
git add -f .secrets/

# eb deploy실행
eb deploy --profile Fc-8th-eb --staged

# .secrets와 requirements를 staging area에서 제거
git reset HEAD .secrets/ requirements.txt
git reset