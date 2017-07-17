from exampleproject.Main import Main

if __name__ == "__main__":
    print(Main())

    import pkg_resources  # part of standart setuptools
    print("Version of ExampleProject is [ {} ]".format(pkg_resources.get_distribution('dohq-example-project').version))

