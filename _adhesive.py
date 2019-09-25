import adhesive
from adhesive import scm
from adhesive.workspace import docker


@adhesive.task('Build Docker Container')
def build_docker_container(context):
    scm.checkout(context.workspace)
    docker.build(context.workspace, "bmst/python-rst-validator")


adhesive.build()

