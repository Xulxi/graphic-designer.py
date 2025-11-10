from .draw import line_rectangle
import svgwrite


def main():
    dwg = svgwrite.Drawing("test.svg", size=("319.705px", "200px"), profile="full")

    # K N
    line_rectangle(
        (10, 100),
        20,
        270,
        200,
        svg=dwg,
        fill="white",
        print_points=True,
    )

    # K NE
    line_rectangle(
        (10, 100),
        20,
        315,
        350,
        svg=dwg,
        fill="white",
        clip_box=(10, None, 0, None),
        print_points=True,
    )

    # K SE
    line_rectangle(
        (10, 100),
        20,
        45,
        350,
        svg=dwg,
        fill="white",
        clip_box=(10, None, None, 200),
        print_points=True,
    )

    # .
    line_rectangle(
        (158.284, 185.858),
        20,
        45,
        20,
        svg=dwg,
        fill="white",
        print_points=True,
    )

    # S NE
    line_rectangle(
        (246.568, 50),
        20,
        315,
        450,
        svg=dwg,
        fill="white",
        clip_box=(192.426, None, 0, 110),
        print_points=True,
    )

    # S SW
    line_rectangle(
        (165.563, 250),
        20,
        135,
        450,
        svg=dwg,
        fill="white",
        clip_box=(None, 319.705, 90, 200),
        print_points=True,
    )

    # S E
    line_rectangle(
        (256.066, 100),
        20,
        0,
        127.279,
        svg=dwg,
        fill="white",
        print_points=True,
    )

    dwg.save()
    print("✅ Generated test.svg")
    help(line_rectangle)


if __name__ == "__main__":
    main()
