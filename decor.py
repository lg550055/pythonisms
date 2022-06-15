import time
from functools import wraps


def timer(func):
  @wraps(func)
  def wrapper_timer(*args, **kwargs):
    start_time = time.perf_counter()
    value = func(*args, **kwargs)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f'Finished {func.__name__!r} in {run_time:.4f} secs')
    return value
  return wrapper_timer


def debug(func):
  @wraps(func)
  def wrapper_debug(*args):
    args_repr = [repr(a) for a in args]
    signature = ", ".join(args_repr)
    print(f"Calling {func.__name__}({signature})")
    value = func(*args)
    print(f"{func.__name__!r} returned {value!r}")
    return value
  return wrapper_debug


def procrastinate(func):
  @wraps(func)
  def wrapper(*args):
    time.sleep(1)
    return func(*args)
  return wrapper


def truncate(func):
  @wraps(func)
  def wrapper(*args):
    original = func(*args)
    return original[1:]
  return wrapper

@timer
def waste_time(n):
  for _ in range(n):
    time.sleep(1)

@timer
@procrastinate
@debug
@truncate
def greeting(name):
  return f'Hello {name}!'


if __name__ == '__main__':
  # waste_time(3)
  greeting('Juan Javier')
