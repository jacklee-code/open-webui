from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_backend_default_brand_is_jackai_without_open_webui_suffix():
    env_source = (ROOT / 'backend' / 'open_webui' / 'env.py').read_text()

    assert "WEBUI_NAME = os.getenv('WEBUI_NAME', 'JackAI')" in env_source
    assert "WEBUI_NAME += ' (Open WebUI)'" not in env_source
