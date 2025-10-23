from string_utils import StringUtils

import pytest

stringutils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected',
                         [('skypro', 'Skypro'),
                          ('hello, world!', 'Hello, world!')])
def test_capitalize_positive(input_str, expected):
    assert stringutils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected',
                         [('123abc', '123abc'),
                          ('', ''),
                          ('  ', '  ')])
def test_capitalize_negative(input_str, expected):
    assert stringutils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected',
                         [('     skypro', 'skypro'),
                          ('     ', '')])
def test_trim_positive(input_str, expected):
    assert stringutils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected',
                         [('skypro   ', 'skypro   '), ('a b', 'a b')
                          ])
def test_trim_negative(input_str, expected):
    assert stringutils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, input_symb, expected',
                         [('Skypro', 'o', True),
                          ('Hello, world!', 'w', True),
                          ('www!', '!', True),
                          ('#$%^','$', True)])
def test_contains_positive(input_str, input_symb, expected):
    assert stringutils.contains(input_str, input_symb) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, input_symb, expected',
                         [('Hello', '2', False),
                              ('%$#%', '!', False),
                          ('World', 'о', False)]) # русская "о"
def test_contains_negative(input_str, input_symb, expected):
    assert stringutils.contains(input_str, input_symb) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, input_symb, expected',
                         [('Skypro', 'p', 'Skyro'),
                          ('123abc', '2', '13abc'),
                          (' ', ' ', '')])
def test_delete_symbol_positive(input_str, input_symb, expected):
    assert stringutils.delete_symbol(input_str, input_symb) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, input_symb, expected',
                         [('123asd', '4', '123asd'),
                          ('world', 'о', 'world')])
def test_delete_symbol_negative(input_str, input_symb, expected):
    assert stringutils.delete_symbol(input_str, input_symb) == expected
