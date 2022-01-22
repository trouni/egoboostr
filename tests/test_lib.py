from egoboostr.lib import get_quote, get_gh_user_info


def test_get_quote():
    quote = get_quote()
    assert len(quote) > 0


def test_get_gh_user_info():
    user = get_gh_user_info("trouni")
    assert "id" in user.keys()
