"""Unit tests for Dev Container local observability integration."""

from __future__ import annotations

import json
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _load_json(path: Path) -> dict:
    loaded = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(loaded, dict)
    return loaded


def test_devcontainer_config_enables_docker_and_forwarded_ports() -> None:
    config_path = _repo_root() / ".devcontainer/devcontainer.json"
    config = _load_json(config_path)

    assert config.get("workspaceFolder") == "/workspaces/ops-lab"

    features = config.get("features")
    assert isinstance(features, dict)
    assert "ghcr.io/devcontainers/features/docker-outside-of-docker:2" in features

    forward_ports = config.get("forwardPorts")
    assert isinstance(forward_ports, list)
    assert set(forward_ports) >= {8000, 9090, 3000}


def test_devcontainer_readme_documents_local_observability_workflow() -> None:
    readme_path = _repo_root() / ".devcontainer/README.md"
    content = readme_path.read_text(encoding="utf-8")

    assert "tc metrics serve --artifacts-root artifacts/runs --host 0.0.0.0 --port 8000" in content
    assert "docker compose -f deploy/observability/docker-compose.yml up" in content
    assert "http://localhost:9090/targets" in content
    assert "http://localhost:3000" in content
    assert "--host 0.0.0.0" in content
