def keep_learning_asynchronous():
    yield "Educative"
    yield 10
    return "is great"


if __name__ == "__main__":
    gen = keep_learning_asynchronous()

    # first_string = next(gen)
    # print(first_string)
    for item in gen:
        print(item)

    try:
        next(gen)
    except StopIteration as e:
        second_string = e.value
        print(second_string)