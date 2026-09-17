# Clase Multa
class Multa:
    TARIFA_POR_DIA = 1.0  # Soles por dia de atraso

    def __init__(self, prestamo, dias_atraso):
        self.prestamo = prestamo
        self.dias_atraso = dias_atraso
        self.monto = round(dias_atraso * self.TARIFA_POR_DIA, 2)
        self.pagada = False

    def pagar(self):
        self.pagada = True

    def __str__(self):
        estado = "Pagada" if self.pagada else "Pendiente"
        return f"Multa de S/ {self.monto:.2f} ({self.dias_atraso} día(s) de atraso) - {estado}"