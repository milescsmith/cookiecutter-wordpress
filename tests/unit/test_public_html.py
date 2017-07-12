# -*- coding: utf-8 -*-

import pytest


class SetupPublicHtml:
    @pytest.fixture()
    def context(self):
        return None

    @pytest.fixture()
    def template(self, cookies, context):
        if context is None:
            return cookies.bake()
        else:
            return cookies.bake(extra_context=context)


class TestPublicHtml(SetupPublicHtml):
    files = (
        (".htaccess"),
        ("index.php"),
        ("wp-config.php"),
    )

    @pytest.mark.parametrize("file", files)
    def test_has_file(self, template, file):
        assert template.project.join("public_html", file).isfile()


class TestHtaccessFile(SetupPublicHtml):
    @pytest.fixture()
    def file(self, template):
        return template.project.join(
            "public_html", ".htaccess").readlines()

    def test_is_not_empty(self, file):
        assert len(file) is not 0


class TestIndexPhpFile(SetupPublicHtml):
    @pytest.fixture()
    def file(self, template):
        return template.project.join(
            "public_html", "index.php").readlines()

    def test_is_not_empty(self, file):
        assert len(file) is not 0


class TestWpConfigPhpFile(SetupPublicHtml):
    @pytest.fixture()
    def file(self, template):
        return template.project.join(
            "public_html", "wp-config.php").readlines()

    def test_is_not_empty(self, file):
        assert len(file) is not 0
