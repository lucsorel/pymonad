# pymonad
Some monadic value holders for Python

# Install

Install from the github repository:

* with [pipenv](https://pipenv.readthedocs.io/en/latest/):

```sh
pipenv install git+https://github.com/lucsorel/pymonad.git#egg=pymonad
```

* with `pip`:

```sh
pip3 install git+https://github.com/lucsorel/pymonad.git
```

# Usages

## Val (= Union[Some, Nothing])

A classic `Maybe` or `Optional` monad, with a shorter name and some extra functions (other people discuss wether [Optional is really a monad or not](https://www.sitepoint.com/how-optional-breaks-the-monad-laws-and-why-it-matters/)).

```python
nullableText = 'lullaby'

# None-safe value mapper
upperedText = Val.of(nullableText).map(
    # mapper called only on non-null values
    lambda text: text.upper()
).get() # returns None if the initial value was None, or if the mapper produces a None value

# None-safe value flat-mapper
upperedText = Val.of(nullableText).flatMap(
    # mapper called only on non-null values
    lambda text: Val.of(text.lower())
).get() # returns None if the initial value was None, or if the mapper produces a None value

# default value
Val.of(nullableText).map(
    lambda text: text.upper()
).get('OPTIONAL_DEFAULT_VALUE') # optional default value


# default value in an alternate producer (wraps creation costs)
upperedText = Val.of(nullableText).map(
    lambda text: text.upper()
).orElseCall(lambda: 'ALTERNATE') # called only if necessary

upperedText = Val.of(nullableText).map(
    lambda text: text.upper()
).orElseFlatCall(lambda: Val.of('ALTERNATE')) # called only if necessary


# handles multiple vals
givennameVal = Val.of('Frankie')
lastnameVal = Val.of('Manning')
loweredFullname = Val.flatMapAllOrElse(
    [givennameVal, lastnameVal],
    # called if ALL vals have values
    lambda text1, text2: Val.of(f'{givennameVal} {lastnameVal}'),
    # alternate producer called if at least one val has a None value
    lambda: Val.of('either no text1 nor text2')
).map(
    lambda text: text.lower()
).get()
```

# Licence

Unless stated otherwise all works are licensed under the [MIT license](http://spdx.org/licenses/MIT.html), a copy of which is included [here](LICENSE).

# Contributions

* [Luc Sorel-Giffo](https://github.com/lucsorel)

Pull-requests are welcome and will be processed on a best-effort basis.
