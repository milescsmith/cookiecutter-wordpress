# -*- coding: utf-8 -*-

import pytest
import json


class SetupTemplate:
    @pytest.fixture()
    def context(self):
        return None

    @pytest.fixture()
    def template(self, cookies, context):
        if context is None:
            return cookies.bake()
        else:
            return cookies.bake(extra_context=context)


class TestCreateTemplate(SetupTemplate):
    def test_exit_code_is_zero(self, template):
        assert template.exit_code == 0

    def test_no_exception(self, template):
        assert template.exception is None

    def test_dir_created(self, template):
        assert template.project.isdir()

    def test_project_name_is_correct(self, template):
        assert template.project.basename == "wordpress"

    files = (
        ("composer.json"),
        ("Makefile"),
    )

    @pytest.mark.parametrize("file", files)
    def test_file_was_created(self, template, file):
        top_level_files = [f.basename for f in template.project.listdir()]
        assert file in top_level_files


class TestComposerJson(SetupTemplate):
    @pytest.fixture
    def context(self):
        return {
            "project_name": "wordpress",
            "version": "0.1.0",
            "wordpress_version": "4.8",
        }

    @pytest.fixture
    def file(self, template):
        return template.project.join("composer.json").readlines()

    @pytest.fixture
    def parsed_file(self, file):
        return json.loads("".join(file))

    def test_not_empty(self, file):
        assert len("".join(file).strip()) is not 0

    def test_is_valid_json(self, parsed_file):
        assert parsed_file is not None

    def test_has_project_name(self, context, parsed_file):
        assert parsed_file["name"] == context["project_name"]

    def test_has_version(self, context, parsed_file):
        assert parsed_file["version"] == context["version"]

    def test_has_wordpress_version(self, context, parsed_file):
        assert parsed_file["require"]["johnpbloch/wordpress"] == \
               context["wordpress_version"]


class TestMakefile(SetupTemplate):
    @pytest.fixture
    def file(self, template):
        return template.project.join("Makefile").readlines()

    def test_not_empty(self, file):
        assert len(file) is not 0

    targets = (
        ("install: composer.json\n"),
    )

    @pytest.mark.parametrize("target", targets)
    def test_contains_target(self, file, target):
        assert target in file
