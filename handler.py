from typing import Any, Dict, Callable

def handle_request(request: Dict[str, Any], process: Callable[[Dict[str, Any]], Dict[str, Any]]) -> Dict[str, Any]:
    """Handles an incoming request and processes it.

    Args:
        request (Dict[str, Any]): The incoming request data.
        process (Callable[[Dict[str, Any]], Dict[str, Any]]): A function to process the request.

    Returns:
        Dict[str, Any]: The processed response.
    """
    response = process(request)
    return response


def log_response(response: Dict[str, Any]) -> None:
    """Logs the response data.

    Args:
        response (Dict[str, Any]): The response data to log.
    """
    print(f'Response: {response}')