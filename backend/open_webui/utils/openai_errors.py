from __future__ import annotations


def format_openai_verify_error_detail(error: Exception) -> str:
    detail = getattr(error, 'detail', None)
    if detail:
        return detail if isinstance(detail, str) else str(detail)

    message = str(error).strip()
    if message:
        return message

    status_code = getattr(error, 'status_code', None)
    if status_code:
        return f'HTTP Error: {status_code}'

    return 'JackAI: Server Connection Error'
