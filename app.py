from flask import Flask, render_template, request, redirect
import csv, os

app = Flask(__name__)
ARCHIVO_DATOS = "database.csv"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tipo = request.form["tipo"]
        monto = request.form["monto"]
        descripcion = request.form["descripcion"]

        existe = os.path.exists(ARCHIVO_DATOS)
        with open(ARCHIVO_DATOS, "a", newline="") as f:
            writer = csv.writer(f)
            if not existe: 
                writer.writerow(["tipo","monto","descripcion"])
            writer.writerow([tipo, monto, descripcion])
        return redirect("/")

    registros = []
    total_ingresos = 0
    total_gastos = 0

    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r") as f:
            reader = csv.DictReader(f)
            for r in reader:
                monto = float(r["monto"])
                registros.append(r)
                if r["tipo"] == "ingreso": 
                    total_ingresos += monto
                else: 
                    total_gastos += monto

    saldo = total_ingresos - total_gastos

    # PASO CLAVE: enviar números y no strings
    return render_template(
        "index.html",
        registros=registros,
        ingresos=int(total_ingresos),
        gastos=int(total_gastos),
        saldo=int(saldo)
    )

if __name__ == "__main__":
    app.run(debug=True)
