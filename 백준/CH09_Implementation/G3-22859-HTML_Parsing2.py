"""
채점결과 틀리다고 나옴
"""

from sys import stdin
import re


def get_title(div: str) -> (int, str):
    if not div:
        return 0, ''

    i = div.index('"') + 1
    res = ''
    while div[i] != '"':
        res += div[i]
        i += 1
    return div.index('>'), res.strip()


def get_para(para) -> str:
    res = ''
    i = 0
    temp = ''
    while i < len(para):
        if para[i] == '<':
            if temp.strip():
                res += temp
            temp = ''
            i = skip_tag(para, i)
            continue

        temp += para[i]
        # res += para[i]
        i += 1
    res += temp
    return res.strip()


def skip_tag(para, i) -> int:
    while para[i] != '>':
        i += 1

    return i + 1


def main():
    document = stdin.readline().rstrip()

    divs = re.sub('<main>|</main>', '', document).split('</div>')
    for div in divs:
        if not div:
            continue
        i, title = get_title(div)
        print('title : ' + title)

        paras = re.sub('<p>|</div>', '', div[i + 1:]).split('</p>')
        for para in paras:
            if para:
                print(get_para(para))


if __name__ == "__main__":
    main()
