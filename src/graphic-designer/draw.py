import math
import svgwrite
from shapely.geometry import Polygon, box


def line_rectangle(
    location,
    width,
    direction,
    length,
    *,
    svg=None,
    fill="black",
    stroke=None,
    stroke_width=0,
    clip_box=None,  # (left, right, up, down)
    print_points=False,
    round_digits=3,
):
    x, y = location
    theta = math.radians(direction)

    dx, dy = math.cos(theta), math.sin(theta)
    px, py = -dy, dx  # perpendicular for width

    half_len = length / 2
    half_wid = width / 2

    points = [
        (x + dx * half_len + px * half_wid, y + dy * half_len + py * half_wid),
        (x + dx * half_len - px * half_wid, y + dy * half_len - py * half_wid),
        (x - dx * half_len - px * half_wid, y - dy * half_len - py * half_wid),
        (x - dx * half_len + px * half_wid, y - dy * half_len + py * half_wid),
    ]

    if clip_box:
        left, right, up, down = clip_box

        def parse_svg_size(value, default=300):
            if value is None:
                return default
            if isinstance(value, str) and value.endswith("px"):
                return float(value[:-2])
            return float(value)

        svg_width = (
            parse_svg_size(svg["width"]) if svg and "width" in svg.attribs else 300
        )
        svg_height = (
            parse_svg_size(svg["height"]) if svg and "height" in svg.attribs else 300
        )

        left = left if left is not None else 0
        right = right if right is not None else svg_width
        up = up if up is not None else 0
        down = down if down is not None else svg_height

        rect_poly = Polygon(points)
        clip_rect = box(left, up, right, down)
        clipped = rect_poly.intersection(clip_rect)

        if clipped.is_empty:
            points = []
        else:
            points = list(clipped.exterior.coords)[:-1]

    # Rounding
    points = [(round(px, round_digits), round(py, round_digits)) for px, py in points]

    if print_points:
        print(f"Rectangle points: {points}")

    if svg:
        if not points:
            return None

        polygon_args = dict(points=points, fill=fill, stroke_width=stroke_width)
        if stroke is not None:
            polygon_args["stroke"] = stroke

        polygon = svg.polygon(**polygon_args)
        svg.add(polygon)
        return polygon
    else:
        return points
