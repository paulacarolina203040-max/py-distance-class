from __future__ import annotations


class Distance:
    def _init_(self, km: float) -> None:
        self.km: float = km

    def _str_(self) -> str:
        return f"Distance: {self.km} kilometers."

    def _repr_(self) -> str:
        return f"Distance(km={self.km})"

    def _add_(
        self,
        other: Distance | float
    ) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def _radd_(
        self,
        other: Distance | float
    ) -> Distance:
        return self._add_(other)

    def _iadd_(
        self,
        other: Distance | float
    ) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def _mul_(
        self,
        other: float
    ) -> Distance:
        return Distance(self.km * other)

    def _rmul_(
        self,
        other: float
    ) -> Distance:
        return self._mul_(other)

    def _truediv_(
        self,
        other: float
    ) -> Distance:
        return Distance(round(self.km / other, 2))

    def _lt_(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def _gt_(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def _eq_(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def _le_(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def _ge_(
        self,
        other: Distance | float
    ) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
