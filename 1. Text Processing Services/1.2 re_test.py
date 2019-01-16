"""
@file: 1.2 re_test.py
@time: 2019/01/16
@author: sch
"""
import re


def Search():
    text = 'Does this text match the pattern?'

    pattern = 'th'
    match = re.search(pattern = pattern, string = text)

    s = match.start()
    e = match.end()

    print("Found \"{pattern}\" in \n\"{text}\" \nfrom {start} to {end} (\"{subtext}\")".format(pattern = pattern,
                                                                                               text = text,
                                                                                               start = s,
                                                                                               end = e,
                                                                                               subtext = text[s:e]))


def Match():
    pattern = "th"
    text = 'Does this text match the pattern?'

    match = re.match(pattern = pattern, string = text)

    s = match.start()
    e = match.end()

    print("Found \"{pattern}\" in \n\"{text}\" \nfrom {start} to {end} (\"{subtext}\")".format(pattern = pattern,
                                                                                               text = text,
                                                                                               start = s,
                                                                                               end = e,
                                                                                               subtext = text[s:e]))


def CompilingExpressions():
    regexes = [re.compile(p) for p in ["this", "index", "text"]]
    text = 'Does this text match the pattern?'

    print("Text -> {}\n".format(text))

    for regex in regexes:
        print("Seeking {} -> ".format(regex.pattern), end = "")
        result = regex.search(text)
        print("match" if result else "not match")


def MultipleMatches():
    text = "'Does this text match the pattern?'"

    pattern_1 = ".*this (.*?) the (.*?)n.*?"
    for match in re.findall(pattern = pattern_1, string = text):
        print(match)

    print()

    pattern_2 = 'th'
    for match in re.finditer(pattern = pattern_2, string = text):
        start = match.start()
        end = match.end()

        print("Found {!r} at {:d}: {:d} ({})".format(pattern_2, start, end, text[start: end]))


if __name__ == '__main__':
    # Search()
    # Match()
    # CompilingExpressions()
    MultipleMatches()
    print()
