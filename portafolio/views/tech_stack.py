import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technology
from portafolio.styles.styles import EmSize, Size
from portafolio import portafolio


def tech_stack(technologies: list[Technology]) -> rx.Component:
    S_id = portafolio.S_technologies.replace(" ", "-")

    return rx.section (
        rx.vstack(
            heading (portafolio.S_technologies),
            rx.flex(
                *[
                    rx.badge(
                        rx.box(
                            class_name=technology.icon,
                            font_size="24px"
                        ),
                        rx.text(technology.name),
                        size="2"
                    )
                    for technology in technologies
                ],
                wrap="wrap",
                spacing=Size.SMALL.value
            ),
            spacing=Size.DEFAULT.value
        ), id = S_id
    )
