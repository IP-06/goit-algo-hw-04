import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
        return
    
    for angle in [60, -120, 60]:
        koch_curve(t, order - 1, size / 3)
        t.left(angle)

    koch_curve(t, order - 1, size / 3)


def koch_snowflake(order, size=300):
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


def main():
    try:
        level = int(input("Введіть рівень рекурсії (0–5): "))
        if level < 0:
            raise ValueError
    except ValueError:
        print("Помилка введення!")
        return

    koch_snowflake(level)


if __name__ == "__main__":
    main()