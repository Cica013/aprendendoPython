import subprocess

# Windows - ping127.0.0.1

proc = subprocess.run(
    ['ping', '127.0.0.1']
)

