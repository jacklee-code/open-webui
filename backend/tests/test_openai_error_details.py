import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HELPER_PATH = ROOT / 'backend/open_webui/utils/openai_errors.py'


def load_helper():
    assert HELPER_PATH.exists(), 'openai error helper module should exist'
    spec = importlib.util.spec_from_file_location('openai_errors', HELPER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_format_openai_verify_error_detail_returns_exception_message():
    module = load_helper()

    detail = module.format_openai_verify_error_detail(
        RuntimeError('Cannot connect to host api.pptoken.cc:443 ssl:default')
    )

    assert detail == 'Cannot connect to host api.pptoken.cc:443 ssl:default'
