from fabric import task

@task
def deploy(c):
    with c.prefix("source ~/.zshrc"):
        with c.cd("~/projects/highone"):
            c.run("git pull")
            c.run("jekyll build")