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

print(sample_text)
print(textwrap.dedent(sample_text))
print(textwrap.indent(sample_text, "go"))
pprint.pprint(textwrap.wrap(sample_text, width = 50))
print()
print(textwrap.fill(sample_text, width = 50))
print()
print(textwrap.shorten(sample_text, width = 20))
