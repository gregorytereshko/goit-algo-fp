import turtle


def draw_pifagor_tree(branch_len, level):
    if level == 0:
        return
    turtle.forward(branch_len)
    turtle.right(30)
    draw_pifagor_tree(branch_len * 0.7, level - 1)
    turtle.left(60)
    draw_pifagor_tree(branch_len * 0.7, level - 1)
    turtle.right(30)
    turtle.backward(branch_len)


recursion_level = int(input("Enter recursion level: "))

turtle.speed(0)
turtle.left(90)
draw_pifagor_tree(100, recursion_level)
turtle.done()
