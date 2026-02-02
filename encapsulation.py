class Outer:
    """Example of an outer class that contains a nested inner class.

    The nested class can be instantiated with a reference to the
    outer instance so it can access the outer's state.
    """

    def __init__(self, value: int):
        self.value = value

    class Inner:
        """Inner class that uses a reference to an Outer instance."""

        def __init__(self, outer_instance: 'Outer', delta: int):
            self._outer = outer_instance
            self.delta = delta

        def combined(self) -> int:
            """Return the sum of the outer's value and this inner's delta."""
            return self._outer.value + self.delta

    def make_inner(self, delta: int) -> 'Outer.Inner':
        """Factory method to create an Inner bound to this Outer instance."""
        return Outer.Inner(self, delta)


if __name__ == "__main__":
    # Small demo runner
    outer = Outer(10)
    inner = outer.make_inner(5)

    print("Outer value:", outer.value)
    print("Inner delta:", inner.delta)
    print("Combined (outer + inner):", inner.combined())

    # You can also instantiate the inner directly if you have an Outer
    other = Outer(7)
    anon = Outer.Inner(other, 3)
    print("Anon combined:", anon.combined())
