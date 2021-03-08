# noxfile.py
import nox


@nox.session(python=["3.8", "3.7"])
def tests(session):
    # More info: https://nox.thea.codes/en/stable/config.html#passing-arguments-into-sessions
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
