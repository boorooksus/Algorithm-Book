from sys import stdin
import re


def get_title(document: str, i: int) -> (int, str):
    while document[i] != '"':
        i += 1
    i += 1
    res = ''
    while document[i] != '"':
        res += document[i]
        i += 1
    return i + 1, res


def get_paragraph(document, i) -> (int, str):
    res = ''
    while True:
        char = document[i]
        if document[i] == '<' and document[i + 1] == '/' \
                and document[i + 2] == 'p':
            break
        elif i < len(document) and document[i] == '<':
            i = skip_tag(document, i)

        res += document[i]
        i += 1

    return i + 2, res


def skip_tag(document, i) -> int:
    while document[i] != '>':
        i += 1

    return i + 1


def main():
    document = stdin.readline().rstrip()

    # divs = re.sub('<main>|</main>', '', document).split('</div>')
    #
    # print(*divs, sep='\n\n==============\n\n')

    # document = re.sub('>', ' ', document)
    tag = ''
    i = 0
    while i < len(document):
        char = document[i]
        if document[i] == '<':
            i += 1
            while i < len(document) and (document[i] != ' ' and document[i] != '>'):
                tag += document[i]
                i += 1

            if tag == 'div':
                i, title = get_title(document, i)
                print(title)
            elif tag == 'p':
                i, paragraph = get_paragraph(document, i + 1)
                print(paragraph)
            tag = ''
        i += 1


if __name__ == "__main__":
    main()
