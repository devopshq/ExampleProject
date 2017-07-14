# -*- coding: utf-8 -*-


import pytest
from exampleproject import Main


class TestMain():

    @pytest.fixture(scope='class', autouse=True)
    def init(self):
        print("This is start of test example.")

    def test_Main(self):
        assert Main.Main() == "This is Main module for ExampleProject that do nosting.\nRead more about DevOpsHQ Community here: https://github.com/devopshq/ExampleProject"
