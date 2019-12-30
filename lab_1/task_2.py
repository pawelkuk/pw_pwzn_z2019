def task_2():
    return (
        "\n".join(
            [
                (" ".join(["*"] * i) if i < 5 else " ".join(["*"] * (10 - i)))
                for i in range(10)
            ]
        )
        + "\n"
    )


assert (
    task_2()
    == """
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
)
