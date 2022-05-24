import os

from h2o_wave import ui

from layouts import get_layouts
from wave_utils import WaveColors


def get_meta(theme):
    tracker_id = os.environ.get('TRACKER_ID', "")
    return ui.meta_card(
        box='',
        title="Sync Data",
        layouts=get_layouts(),
        tracker=ui.tracker(type=ui.TrackerType.GA, id=tracker_id),
        themes=[
            ui.theme(
                name='MCAC-Dark',
                primary=WaveColors.h2o,
                text=WaveColors.white,
                card=WaveColors.light_gray,
                page=WaveColors.black,
            )
        ],
        theme=theme,
    )


def get_header():
    return ui.header_card(
        box=ui.box('header'),
        title="Sync Test Application",
        subtitle="Sync changes with multiple users",
        icon='Home',
        icon_color='#000000',
    )


def get_user_input_form(q):
    items = [
        ui.text_l(q.auth.username),
        ui.textbox(name='user_input', label='Input Text', required=True),
        ui.buttons(
            items=[
                ui.button(
                    name="submit_btn",
                    label="Submit",
                    icon="Upload",
                    primary=True,
                ),
            ],
            justify=ui.ButtonsJustify.END
        )
    ]

    return ui.form_card(
        box=ui.box('commands'),
        items=items
    )


def get_footer():
    return ui.footer_card(
        box=ui.box('footer', order=1, width="475px"),
        caption='<p style="text-align: center;">Made with 💛️ using <a href="https://h2oai.github.io/wave/", target="_blank">Wave</a>. (c) 2022 H2O.ai. All rights reserved.</p>' # noqa: E501
    )


def get_status(status):
    return ui.form_card(box='main_center', items=[ui.text_l(status)])

