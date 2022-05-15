# Bismarck

Bismarck is a classic card game which is played between two players each striving to defeat the other through strategy and careful planning. Below you will be able to find various aspects of the game like links to documentation, some instructions on how to install and launch the program as well as instructions on how to test it. Not all of the mentioned aspects are yet implemented.

## Documentation

 - [Instructions](./documentation/instructions.md)
 - [Functional specifications](./documentation/functional_specifications.md)
 - [Working hours](./documentation/working_hours.md)
 - [Changelog](./documentation/changelog.md)
 - [Testing](./documentation/testing_documentation.md)
 - [Architecture](./documentation/architecture.md)
 - [Releases](https://github.com/Catrovitch/ot-harjoitustyo/releases)

## Installing

1. Install the dependencies with command:

```bash
poetry install
```

1. To initialize or reset the database:

```bash
poetry run invoke build
```

3. Start the program with command:
- Note: If running the program via a virtual machine, make sure it is running in fullscreen mode for Bismarck to run optimally.

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

## Clean Code

A clean code rating can be generated with command:

```bash
pylint src
```

