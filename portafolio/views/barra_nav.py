import reflex as rx
from portafolio import portafolio


def barra_nav() -> rx.Component:
    S_about_id = portafolio.S_about.replace(" ", "-")


    return rx.hstack(
        rx.link (portafolio.S_about,href="#" + S_about_id),
        rx.link ("Tecnologías", href="#Tecnologías"),
        rx.link ("Proyectos", href="#Proyectos"),
        rx.link ("Experiencia", href="#Experiencia"),
        rx.link ("Formación", href="#Formación"),
        rx.link ("Extra", href="#Extra"),

        justify_content = "center",
        width = "100%",
        spacing = "9",
    )
