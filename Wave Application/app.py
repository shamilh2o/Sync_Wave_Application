from h2o_wave import Q, app, handle_on, main
from initializers import initialize_app, initialize_client, initialize_user


@app('/', mode='multicast')
async def serve(q: Q):
    await initialize_app(q)
    await initialize_user(q)
    await initialize_client(q)

    await q.page.save()

