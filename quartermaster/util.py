
def enum(*args, **named):
    """enum class factory.

    Provides easy enumerated types in Python. An enumeration is defined as follows:
        
        Animals = enum('Cow', 'Pig', 'Sheep', 'Chicken')
        Coins = enum(Penny=1, Nickle=5, Dime=10, Quarter=25)

    The values can used cleanly and directly:
        
    >>> fred = Animals.Sheep
    >>> if fred == Animals.Cow:
    >>>     print 'Mooo!'

    Comparisons work as expected:
    >>> cent = Coins.Penny
    >>> Coins.Penny == cent
    True

    Including inequalities:
    >>> Coins.Quarter < Coins.Nickel
    False
    >>> Coins.Penny < Coins.Dime
    True

    And don't work across types, even if their values are identical.
    >>> Coins.Penny
    Penny=1
    >>> Animals.Pig
    Pig=1
    >>> Coins.Penny == Animals.Pig
    False

    Enum values can also be looked up, by both name and value:
    >>> Coins['Penny']
    Penny=1
    >>> Coins['Dime'].value()
    10
    >>> Coins[25].name()
    'Quarter'

    """

    prenums = zip(args, range(len(args)))+named.items() 
    h = hash(repr(sorted(prenums, key=lambda x: x[1])))

    def factory(n, s, h):
        class EnumValue:
            __slots__ = []
            __name__ = s
            _hash = h
            def __str__(self): return s
            def __repr__(self):
                return "{0}={1}".format(s, n)
            def __int__(self):
                return n
            def __cmp__(self, other):
                if isinstance(other, int): return n.__cmp__(other)
                if isinstance(other, EnumValue) and h==other._hash: return n.__cmp__(other.value())
                return NotImplemented
            def __getitem__(self, x):
                return (s, n)[x]
            def name(self): return s
            def value(self): return n
        return EnumValue

    enums = dict(map(lambda x: (x[0], factory(x[1], x[0], h)()), prenums))

    t = type('Enum', (), enums)
    lookup = dict(map(lambda x: (x[1], x[0]), prenums))
    def Enum(self, s):
        if type(s) is str:
            if s in lookup.values():
                return getattr(t, s)
            else: raise IndexError("No such name in this enumeration")
        elif type(s) is int:
            if s in lookup:
                return getattr(t, lookup[s])
            else: raise IndexError("No such numeric value in this enumeration")
        raise TypeError("Expected int or string")
    setattr(t, '__call__', Enum)
    _repr = 'enum({0})'.format(', '.join(repr(x) for x in sorted(enums, key=enums.get)))
    setattr(t, '__repr__', lambda self: _repr )
    setattr(t, '__getitem__', Enum)
    def _setattr(self, x, y): raise AttributeError('Enumerations are read-only')
    setattr(t, '__setattr__', _setattr)
    return t()

# Access level for users
AccessLevel = enum(NoAccess=0, User=1, Moderator=5, Admin=10)

