import reflex as rx

"""
Sobre-mí
Tecnologías
Proyectos
Experiencia
Formación
Extra
"""

def barra_nav() -> rx.Component:
    return rx.hstack(
        rx.link ("Sobre mí", href="#Sobre-mí"),
        rx.link ("Tecnologías", href="#Tecnologías"),
        rx.link ("Proyectos", href="#Proyectos"),
        rx.link ("Experiencia", href="#Experiencia"),
        rx.link ("Formación", href="#Formación"),
        rx.link ("Extra", href="#Extra"),

        justify_content = "center",
        width = "100%",
        spacing = "9",
    )
