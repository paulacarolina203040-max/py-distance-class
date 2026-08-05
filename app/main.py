class Distance:
    def _init_(self, km: int | float):
        self.km = km

    def _str_(self) -> str:
        return f"Distance: {self.km} kilometers."

    def _repr_(self) -> str:
        return f"Distance(km={self.km})"

    def _add_(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def _radd_(self, other):
        return self._add_(other)

    def _iadd_(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def _mul_(self, other):
        return Distance(self.km * other)

    def _rmul_(self, other):
        return self._mul_(other)

    def _truediv_(self, other):
        return Distance(round(self.km / other, 2))

    def _lt_(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def _gt_(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def _eq_(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def _le_(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def _ge_(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
