from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_backend_default_brand_is_jackai_without_open_webui_suffix():
    env_source = (ROOT / 'backend' / 'open_webui' / 'env.py').read_text()

    assert "WEBUI_NAME = os.getenv('WEBUI_NAME', 'JackAI')" in env_source
    assert "WEBUI_NAME += ' (Open WebUI)'" not in env_source


def test_static_app_shell_uses_jackai_for_initial_title_and_share_metadata():
    app_html = (ROOT / 'src' / 'app.html').read_text()

    assert '<title>JackAI</title>' in app_html
    assert '<title>Open WebUI</title>' not in app_html
