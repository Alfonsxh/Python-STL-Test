"""
@file: string_test.py
@time: 2019/01/16
@author: sch
"""
import inspect
import string


# Some strings for ctype-style character classification
# whitespace = ' \t\n\r\v\f'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_letters = ascii_lowercase + ascii_uppercase
# digits = '0123456789'
# hexdigits = digits + 'abcdef' + 'ABCDEF'
# octdigits = '01234567'
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
# printable = digits + ascii_letters + punctuation + whitespace

def PrintStrings():
    """print str type value in string module"""

    def is_str(value):
        """if it's str type"""
        return isinstance(value, str)

    for name, value in inspect.getmembers(string, is_str):
        if name.startswith('_'):
            continue
        print("%s = %r" % (name, value))


def CapWords():
    """cap words"""

    s = 'The quick brown fox jumped over the lazy dog.'
    print(s)
    print(string.capwords(s))


def FormatterTest():
    """string formatter class test"""

    format_string = string.Formatter()
    s_1 = format_string.format("{a} + {b} = {c}", a = 1, b = 2, c = 3)  # same as str.format()
    print(s_1)


def TemplatesTest():
    """diff templates compare"""

    values = {'var': 'foo'}
    t_1 = string.Template("""
    Variable        : $var
    Escape          : $$
    Variable in text: ${var}iable
    """)
    print('string Template:', t_1.substitute(values))

    t_2 = """
       Variable        : %(var)s
       Escape          : %%
       Variable in text: %(var)siable
       """
    print('Interpolation:', t_2 % values)

    t_3 = """
       Variable        : {var}
       Escape          : {{}}
       Variable in text: {var}iable
       """
    print('Format:', t_3.format(**values))


if __name__ == '__main__':
    # PrintStrings()
    # CapWords()
    # FormatterTest()
    TemplatesTest()
    pass
