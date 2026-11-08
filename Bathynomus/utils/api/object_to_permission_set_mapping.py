import logging

_logger = logging.getLogger(__name__)
_mapping = {
    'product': 'product',
    'test_case': 'test_case',
    'test_run': 'test_run',
}

def get_object_permission_set(destination: str) -> str | None:
    try:
        return _mapping[destination]
    except KeyError:
        _logger.error(
            "get_object_permission_set: unknown destination: %s | KeyError: %s",
            destination,
            KeyError
        )
        return None
