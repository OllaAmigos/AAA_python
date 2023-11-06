import pytest
from morse import decode

"""Second issue"""


@pytest.mark.parametrize('morse_input, expected_output', [
    ('... --- ...', 'SOS'),
    ('.- -.-- --- -.--', 'AYOY'),
    ('-- .- -- -- .- -- .. .-', 'MAMMAMIA'),
])
def test_decode(morse_input, expected_output):
    """Проверка для верного кодирования"""
    assert decode(morse_input) == expected_output


if __name__ == '__main__':
    pytest.main()
