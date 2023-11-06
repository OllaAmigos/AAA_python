[Постановка задачи тут](https://github.com/siauPatrick/mai-python/blob/master/03-instrumenty-testirovaniya-v-python/issues.md)


### *Issue 1* (doctest) -- [тут](./issue1/morse.py)
  
  Doctest flag: `python -m doctest -o NORMALIZE_WHITESPACE -v morse.py`

### *Issue 2* (pytest.mark.parametrize) -- [тут](./issue2/test_morse.py)

### *Issue 3* (unittest One Hot) -- [тут](./issue3/is3.py)

### *Issue 4* (pytest One Hot) -- [тут](./issue4/is4.py)

### *Issue 5* (all tests 100% coverage) -- [тут](./issue5/is5.py)
*(команды в терминале)*
Для запуска тестов:
`python -m pytest -v -s is5.py`

Для просмотра процента покрытия:
`python -m pytest -q is5.py --cov=issue_05`

Для создания html отчета:
`python -m pytest -q is5.py --cov=is5 --cov-report html`

