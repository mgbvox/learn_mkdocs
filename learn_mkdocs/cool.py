class Person:
    """
    A person. Sometimes cool.
    """

    def __init__(self, name: str, age: float):
        """
        Make a person.

        Args:
            name: Their name.
            age: Their age.
        """

        self.name = name
        self.age = age


def do_stuff(a: int, b: float = 3.0) -> str:
    """
    Does cool stuff with a.

    Args:
        a: A thing to do stuff with.
        b: A thing to do stuff with as well.

    Examples:
        do_stuff(3)

    Returns:
        A cool string.

    """
    return f"Did cool stuff with {a+b}"
