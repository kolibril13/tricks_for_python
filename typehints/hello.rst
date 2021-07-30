Adding type hints to functions and parameters
---------------------------------------------

If you've never used type hints before, this is a good place to get started:
https://realpython.com/python-type-checking/#hello-types.

When adding type hints to manim, there are some guidelines that should be followed:

* Coordinates have the typehint ``Sequence[float]``, e.g.

.. code:: py
    def set_points_as_corners(self, points: Sequence[float]) -> "VMobject":
        """Given an array of points, set them as corner of the Vmobject."""
* ``**kwargs`` has no typehint

* Mobjects have the typehint "Mobject", e.g.

.. code:: py
    def match_color(self, mobject: "Mobject"):
        """Match the color with the color of another :class:`~.Mobject`."""
        return self.set_color(mobject.get_color())
* Colors have the typehint ``Color``, e.g.

.. code:: py
    def set_color(self, color: Color = YELLOW_C, family: bool = True):
        """Condition is function which takes in one arguments, (x, y, z)."""
* As ``float`` and ``Union[int, float]`` are the same, use only ``float``

* For numpy arrays use the typehint ``np.ndarray``

* Functions that does not return a value should get the type hint ``None``. (This annotations help catch the kinds of subtle bugs where you are trying to use a meaningless return value. )

.. code:: py
    def height(self, value) -> None:
        self.scale_to_fit_height(value)
* When a paramter is None by default, it can get the type hint ``Optional`` 

.. code:: py
    def rotate(
        self,
        angle,
        axis=OUT,
        about_point: Optional[Sequence[float]] = None,
        **kwargs,
    ):
* the .__init__() method always should have None as its return type.

* functions and lambda functions should get the typehint `Callable`

.. code:: py
    rate_func: Callable[float] = lambda t: smooth(1 - t)
    
*  numpy arrays can get type hints with `np.ndarray`

Missing Sections
----------------
* Tools for typehinting
* Link to MyPy
* Mypy and numpy import errors: https://realpython.com/python-type-checking/#running-mypy
* Where to find the alias
* How to use "VMobject" , "Mobject" typehints?