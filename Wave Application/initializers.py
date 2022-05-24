import os

from h2o_wave import Q
from common import make_base_ui, writeFileContent
from user import AppUser


async def initialize_app(q: Q):
    # Initialize only once per app instance
    if q.app.initialized:
        return

    # Setup Cards and Users
    q.app.cards = {}
    q.app.users = {}
    q.app.test = {}

    # Mark the app as initialized
    q.app.initialized = True


async def initialize_user(q: Q):
    user_id = q.auth.subject
    # If this user exists, do nothing
    if user_id in q.app.users:
        return

    # Create a new user
    new_user = AppUser(
        user_id=user_id, email=q.auth.username
    )

    # Set newly created user as current user
    q.user.user = new_user

    # Add user to the list of app Users
    q.app.users[user_id] = new_user
    q.app.test[user_id] = q


async def initialize_client(q: Q):
    if q.client.initialized and q.args.submit_btn:
        await writeFileContent(q, q.args.user_input)
        await make_base_ui(q)
        for val in q.app.test.values():
            if val != q:
                await make_base_ui(val)
                await val.page.save()

        return

    # Crate the first view of the app
    await make_base_ui(q)

    # Mark the client as initialized
    q.client.initialized = True


