import functools

def validate(func):
    @functools.wraps(func)
    def wrapper (x,y,z):
        if 0 <= x <= 256 and 0 <= y <= 256 and 0 <= z <= 256:
            result = func(x,y,z)
        else:
            result = f'Function call is not valid!'
        return result
    return wrapper
    pass

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"
#
# print(set_pixel(0, 127, 300))
# print(set_pixel(0, 127, 255))