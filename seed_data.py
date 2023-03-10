from CarsApp.models import Americano, Europeo, Japones

Americano(marca_de_vehiculo = "Dodge",
          modelo_de_vehiculo = "Charger 1969",
          motor = "Hellcat V8",
          descripcion_vehiculo = "Vehículo 'Muscle' con un motor potente y una estética exterior muy linda.",
          nacionalidad_de_fabricante = "Estadounidense").save()

Europeo(marca_de_vehiculo = "Volkswagen",
        modelo_de_vehiculo = "Vento 2020",
        motor = "TSI 2.0 lts I4",
        descripcion_vehiculo = "Vehiculo  compacto alemán, con mucha potencia y confortable.",
        nacionalidad_de_fabricante = "Aleman").save()

Japones(marca_de_vehiculo = "Toyota",
        modelo_de_vehiculo = "Corolla 2011",
        motor = "VVT-i  1.8 lts",
        descripcion_vehiculo = "Vehiculo del segmento 'C' japones.",
        nacionalidad_de_fabricante = "Japones").save()





