import subprocess
import sys

print("========================================")
print(" EJECUCION DE PRUEBAS")
print("========================================")

pruebas = subprocess.run(
    [
        sys.executable,
        "-m",
        "coverage",
        "run",
        "manage.py",
        "test"
    ],
    capture_output=True,
    text=True
)

print(pruebas.stdout)
print(pruebas.stderr)

print("========================================")
print(" REPORTE DE COBERTURA")
print("========================================")

cobertura = subprocess.run(
    [
        sys.executable,
        "-m",
        "coverage",
        "report",
        "-m"
    ],
    capture_output=True,
    text=True
)

print(cobertura.stdout)

if pruebas.returncode == 0:
    print("Las pruebas finalizaron correctamente.")
else:
    print("Se detectaron pruebas con errores o fallos.")