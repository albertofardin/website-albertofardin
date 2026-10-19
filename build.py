import base64, re, sys, pathlib
root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent
html = (root/'template.html').read_text()
def sub(m):
    return 'data:image/webp;base64,' + base64.b64encode((root/'img'/f'{m[1]}.webp').read_bytes()).decode()
out = re.sub(r'\{\{(\w+)\}\}', sub, html)
assert '{{' not in out
(root/'site/index.html').write_text(out)
head = '<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
body = out.replace('</style>\n', '</style>\n</head>\n<body>\n', 1) + '\n</body>\n</html>\n'
(root/'site/albertofardin.html').write_text(head + body)
print(len(out)//1024, 'KB')
