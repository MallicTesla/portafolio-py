import reflex as rx
from portafolio import portafolio


def barra_nav() -> rx.Component:
    S_about_id = portafolio.S_about.replace(" ", "-")
    S_technologies_id = portafolio.S_technologies.replace(" ", "-")
    S_projectss_id = portafolio.S_projects.replace(" ", "-")
    S_experience_id = portafolio.S_experience.replace(" ", "-")
    S_training_id = portafolio.S_training.replace(" ", "-")
    S_extras_id = portafolio.S_extras.replace(" ", "-")


    return rx.hstack(
        rx.link (portafolio.S_about, href = "#" + S_about_id),
        rx.link (portafolio.S_technologies, href = "#" + S_technologies_id),
        rx.link (portafolio.S_projects, href = "#" + S_projectss_id),
        rx.link (portafolio.S_experience, href = "#" + S_experience_id),
        rx.link (portafolio.S_training, href = "#" + S_training_id),
        rx.link (portafolio.S_extras, href = "#" + S_extras_id),

        justify_content = "center",
        width = "100%",
        spacing = "9",
    )
