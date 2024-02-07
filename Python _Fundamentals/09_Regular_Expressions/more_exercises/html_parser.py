import re

html_link = input()

title_regex = r"<title>([^<>]*)<\/title>"
body_regex = r'<body>.*<\/body>'

title = re.findall(title_regex, html_link)
print(f'Title: {"".join(title)}')

body = re.findall(body_regex, html_link)
body = "".join(body)

filter_content_regex = r">([^><]*)<"
content = re.findall(filter_content_regex, body)
content = ''.join(content)
content = content.replace('\\n', '')
print(f'Content: {content}')
