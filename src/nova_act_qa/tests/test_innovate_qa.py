import pytest

from nova_act_qa.utils.nova_act import NovaAct


@pytest.mark.parametrize("nova", ["https://innovateqaevents.com/"], indirect=True)
def test_landing_page(nova: NovaAct):
    nova.test_bool("Am I on the Innovate QA landing page?")
    nova.test_str("Conference date", "June 5, 2025")
    nova.test_str("Conference location", "Hilton Garden Inn 1800 NW Gilman Blvd Seattle, WA")


@pytest.mark.parametrize(
    "nova", ["https://innovateqaevents.com/2025-program-speakers"], indirect=True
)
def test_program_speakers_page(nova: NovaAct):
    nova.test_str("Agenda on June 4", "Social Networking")
    nova.test(
        "3 Agenda columns on June 5",
        ["Leadership Track", "IC Track", "Workshop/Discussion"],
        {"type": "array", "items": {"type": "string"}},
    )
    contact_button_text = "Drop us a line!"
    contact_button = nova.page.get_by_role("button", name=contact_button_text)
    contact_button.scroll_into_view_if_needed()
    nova.act(f"Click the {contact_button_text} button")
    nova.act("Click the Send button")
    nova.test_bool("There is an input validation error message")
