import pytest

from nova_act_qa.utils._types import AssertType
from nova_act_qa.utils.nova_act import NovaAct

NOVA_ACT_URL = "https://nova.amazon.com/act"


@pytest.mark.parametrize("nova", ["https://nova.amazon.com"], indirect=True)
def test_navigation(nova: NovaAct):
    nova.test_bool("Is Act on the side nav?")
    nova.act("Go to the Act page")
    assert nova.page.url == NOVA_ACT_URL


@pytest.mark.parametrize("nova", ["https://nova.amazon.com/act"], indirect=True)
def test_landing_page(nova: NovaAct):
    nova.test_bool("Am I on the Nova Act landing page?")
    nova.test_bool("Is there a Get Started section?")
    nova.test_str("The pip install command for the SDK", "pip install nova-act")
    nova.test_str("API Key button text", "Generate key")
