# Bismarck

Bismarck is a classic card game which is played between two players each striving to defeat the other through strategy and careful planning. Below you will be able to find various aspects of the game like links to documentation, some instructions on how to install and launch the program as well as instructions on how to test it. Not all of the mentioned aspects are yet implemented.

## Documentation

 - [Functional specifications](./documentation/functional_specifications.md)
 - [Working hours](./documentation/working_hours.md)
 - [Changelog](./documentation/changelog.md)
 - [Testing](./documentation/testing_documentation.md)

## Installing

#### Note
As the program is at a very early stage a proper main function is not currently available. Currently it creates all the currently finnished parts of the game.

1. Install the dependencies with command:

```bash
poetry install
```

2. Start the program with command:

```bash
poetry run invoke start
```

## Testing

A test coverage report can be generated with command:
#### Note:
Due to one of the tests relying on shuffling the deck the test might at rare cases fail although nothing is wrong. Run the test again and it should work.
```bash
poetry run invoke coverage-report
```

You can find the generated test in _htmlcov_ folder.

