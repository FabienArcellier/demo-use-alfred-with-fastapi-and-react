import alfred


@alfred.command("ci", help="workflow to execute the continuous integration process")
@alfred.option('--backend', '-b', help="run continuous integration for backend", is_flag=True, default=False)
@alfred.option('--frontend', '-f', help="run continuous integration for frontend", is_flag=True, default=False)
def ci(backend: bool, frontend: bool):
    run_backend = backend or not frontend
    run_frontend = frontend or not backend
    run_docker = not backend and not frontend

    if run_backend:
        alfred.invoke_command('backend:lint')
        alfred.invoke_command('backend:tests')

    if run_frontend:
        alfred.invoke_command('frontend:tests')

    if run_docker:
        alfred.invoke_command('docker:build')


