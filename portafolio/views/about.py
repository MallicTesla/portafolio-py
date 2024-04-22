import reflex as rx
from portafolio.components.heading import heading
from portafolio import portafolio


def about(description: str) -> rx.Component:
    S_id = portafolio.S_about.replace(" ", "-")

    return rx.section (
        rx.vstack(
            heading(portafolio.S_about),
            rx.html(description)
        ),
        id = S_id
    )