"""
@file: 1.4 textwrap_test.py
@time: 2019/01/16
@author: sch
"""
import pprint
import textwrap

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.\n     It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

print("normal ->\n", sample_text)
print()
print("with textwrap.wrap ->\n", textwrap.wrap(sample_text, width = 50))
print()
print("with textwrap.wrap 2 ->\n", '\n'.join(textwrap.wrap(sample_text, width = 50)))
print()
print("with textwrap.fill width is 50 ->\n", textwrap.fill(sample_text, width = 50))
print()
print("with textwrap.fill width is 100 ->\n", textwrap.fill(sample_text, width = 100))
print()
print("with textwrap.shorten ->\n", textwrap.shorten(sample_text, width = 20))
print()
print("with textwrap.dedent ->\n", textwrap.dedent(sample_text))
print()
print("with textwrap.indent ->\n", textwrap.indent(sample_text, ">"))
