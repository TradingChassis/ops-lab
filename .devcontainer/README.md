# Dev Container Observability Workflow

Use this local workflow to run the Unit 2 observability stack from inside the Dev Container.

Terminal 1:

```bash
tc metrics serve --artifacts-root artifacts/runs --host 0.0.0.0 --port 8000
```

Terminal 2:

```bash
docker compose -f deploy/observability/docker-compose.yml up
```

Verify:

- Prometheus targets: http://localhost:9090/targets
- Target `ops_lab_metrics` is `UP`
- Grafana: http://localhost:3000
- Dashboard is provisioned automatically

`--host 0.0.0.0` is recommended in the Dev Container so the forwarded metrics port can be reached by the local Compose stack.
