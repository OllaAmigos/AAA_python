*(команды в терминале)*
Для запуска тестов:
`python -m pytest -v -s is5.py`

Для просмотра процента покрытия:
`python -m pytest -q is5.py --cov=issue_05`

Для создания html отчета:
`python -m pytest -q is5.py --cov=is5 --cov-report html`
