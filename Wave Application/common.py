import json
from h2o_wave import Q

from components import (
    get_meta,
    get_header,
    get_footer,
    get_user_input_form,
    get_status
)


async def make_base_ui(q: Q):
    q.client.theme = 'MCAC-Dark'

    q.page['meta'] = get_meta(q.client.theme)
    q.page['header'] = get_header()
    q.page['input_form'] = get_user_input_form(q)
    q.page['footer'] = get_footer()

    content = await getFileContent(q)
    q.page['status'] = get_status(content)


async def getFileContent(q:Q):
    q.user.file_path = "text.txt"

    with open(q.user.file_path, 'r') as file:
        data = file.read()
    print("File Opened")
    file.close()

    return data


async def writeFileContent(q, text):

    with open(q.user.file_path, 'a') as file:
        data = file.write("\n" + text)

    print("File Wrote")
    file.close()

    return data
