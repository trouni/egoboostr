import streamlit as st
from egoboostr.lib import get_quote, get_gh_user_info

query_params = st.experimental_get_query_params()
col1, col2 = st.columns([1, 4])


def set_gh_username():
    st.experimental_set_query_params(gh=st.session_state.gh_username)


if query_params:
    user = get_gh_user_info(query_params["gh"][0])
    col1.image(user["avatar_url"])
    col2.header(get_quote(user["name"], query_params.get("category", ["dev"])[0]))
else:
    username = st.text_input(
        label="",
        key="gh_username",
        on_change=set_gh_username,
        placeholder="Enter a GitHub username:",
    )
    col1.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Chuck_Norris%2C_The_Delta_Force_1986.jpg/1280px-Chuck_Norris%2C_The_Delta_Force_1986.jpg"
    )
    col2.header(get_quote())
