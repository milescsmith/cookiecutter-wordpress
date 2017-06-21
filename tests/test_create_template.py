# -*- coding: utf-8 -*-

import pytest


class TestCreateTemplate:
    @pytest.fixture()
    def template(self, cookies):
        return cookies.bake()

    def test_exit_code_is_zero(self, template):
        assert template.exit_code == 0

    def test_no_exception(self, template):
        assert template.exception is None

    def test_dir_created(self, template):
        assert template.project.isdir()

    def test_project_name_is_correct(self, template):
        assert template.project.basename == "wordpress"
