# -*- coding: utf-8 -*-

import pytest
import yaml


class SetupDevEnvironment:
    @pytest.fixture()
    def context(self):
        return {
            "project_slug": "wordpress"
        }

    @pytest.fixture()
    def template(self, cookies):
        return cookies.bake()


class TestDevEnvironment(SetupDevEnvironment):
    def test_has_docker_compose_file(self, template):
        assert template.project.join(
            "dev", "docker", "docker-compose.yml").isfile()

    def test_has_devbox_docker_file(self, template):
        assert template.project.join(
            "dev", "docker", "devbox", "Dockerfile").isfile()

    def test_has_web_docker_file(self, template):
        assert template.project.join(
            "dev", "docker", "web", "Dockerfile").isfile()


class TestDockerComposeFile(SetupDevEnvironment):
    @pytest.fixture()
    def file(self, template):
        return yaml.load(
            template.project.join(
                "dev", "docker", "docker-compose.yml").read())

    @pytest.fixture
    def proj_slug(self, context):
        return context["project_slug"]

    def test_is_valid_yaml(self, file):
        assert file is not None

    def test_is_version_3(self, file):
        assert file["version"] is "3"

    def test_defines_expected_services(self, proj_slug, file):
        services = ["devbox", "web", "db"]
        assert list(file["services"].keys()).sort() == [
            "{}_{}".format(proj_slug, s) for s in services].sort()

    attributes = (
        (("services", "{}_devbox", "image"), "{}:devbox"),
        (("services", "{}_devbox", "container_name"), "{}_devbox"),

        (("services", "{}_db", "container_name"), "{}_db"),

        (("services", "{}_web", "image"), "{}:web"),
        (("services", "{}_web", "container_name"), "{}_web")
    )

    @pytest.mark.parametrize("path, expected", attributes)
    def test_attribute_value(self, file, proj_slug, path, expected):
        attr = file
        for k in path:
            attr = attr[k.format(proj_slug)]

        assert attr == expected.format(proj_slug)


class TestDevboxDockerFile(SetupDevEnvironment):
    @pytest.fixture()
    def file(self, template):
        return template.project.join(
                "dev", "docker", "devbox", "Dockerfile").readlines()

    def test_is_not_empty(self, file):
        assert len(file) is not 0


class TestWebDockerFile(SetupDevEnvironment):
    @pytest.fixture()
    def file(self, template):
        return template.project.join(
                "dev", "docker", "web", "Dockerfile").readlines()

    def test_is_not_empty(self, file):
        assert len(file) is not 0
