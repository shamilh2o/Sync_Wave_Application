from h2o_wave import Q, app, handle_on, main

from common import make_base_ui, writeFileContent


@app('/', mode='multicast')
async def serve(q: Q):
    if q.args.submit_btn:
        await writeFileContent(q, q.args.user_input)
        await make_base_ui(q)
    else:
        await make_base_ui(q)
    await q.page.save()
