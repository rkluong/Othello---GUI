
import math

class Point:
    def __init__(self, frac_x: float, frac_y: float):
        self._frac_x = frac_x
        self._frac_y = frac_y

    def frac_coordinate(self, rows:int, columns:int) -> (float, float):
        "returns fractional coordinates given row and column"
        return (math.floor(self._frac_x*rows), math.floor(
            self._frac_y*columns)
                )
    
    def pixel(self, width: float, height: float) -> (float, float):
        "returns pixel coordinate tuple given width and height"
        return(int(self._frac_x * width), int(self._frac_y * height))
    

    def from_pixel(self, pixel_x: float, pixel_y:float, width:float, height:float) -> 'point':
        "returns the distance from pixel coordinate"
        return (pixel_x/ width, pixel_y/height)

    
