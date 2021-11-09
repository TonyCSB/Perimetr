import threading


class Monitor:
    """A dead hand system that monitor changes in network device and act accordingly

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    def __init__(self, method, target, interval, callback, *args, **kwargs):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        self.method = method

    def activate(self):
        print("activate")

    def deactivate(self):
        print("deactivate")

    def changeTarget(self, method, target):
        print("change target")


if __name__ == "__main__":
    print("HI")
