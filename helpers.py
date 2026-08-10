def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def generate_unique_id(length=8):
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def debounce(wait):
    from threading import Timer
    def decorator(fn):
        timer = None
        def debounced(*args, **kwargs):
            nonlocal timer
            if timer is not None:
                timer.cancel()
            timer = Timer(wait, lambda: fn(*args, **kwargs))
            timer.start()
        return debounced
    return decorator

def to_json(data):
    import json
    return json.dumps(data, indent=4)

