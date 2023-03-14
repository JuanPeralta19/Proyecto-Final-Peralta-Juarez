from CarsApp.models import Americano, Europeo, Japones

#VEHICULOS AMERICANOS

Americano(marca_de_vehiculo = "Dodge",
          modelo_de_vehiculo = "Charger 1969",
          motor = "Hellcat V8",
          descripcion_vehiculo = "Vehículo 'Muscle' con un motor potente y una estética exterior muy linda.",
          nacionalidad_de_fabricante = "Estadounidense").save()

Americano(marca_de_vehiculo = "Ford",
          modelo_de_vehiculo = "Mustang 1967",
          motor = "V8 4.6Lts",
          descripcion_vehiculo = "Vehículo 'Muscle' con un motor potente y una estética exterior muy linda.",
          nacionalidad_de_fabricante = "Estadounidense").save()

Americano(marca_de_vehiculo = "Chevrolet",
          modelo_de_vehiculo = "Camaro 1969",
          motor = "V8 6.2Lts",
          descripcion_vehiculo = "Vehículo 'Muscle' con un motor potente y una estética exterior muy linda.",
          nacionalidad_de_fabricante = "Estadounidense").save()

#VEHICULOS EUROPEOS

Europeo(marca_de_vehiculo = "Volkswagen",
        modelo_de_vehiculo = "Vento 2020",
        motor = "TSI 2.0 lts I4",
        descripcion_vehiculo = "Vehiculo  compacto alemán, con mucha potencia y confortable.",
        nacionalidad_de_fabricante = "Aleman").save()

Europeo(marca_de_vehiculo = "Volkswagen",
        modelo_de_vehiculo = "Beetle tipo 1",
        motor = "H4 1.1Lts",
        descripcion_vehiculo = "Vehiculo  compacto alemán",
        nacionalidad_de_fabricante = "Aleman").save()

Europeo(marca_de_vehiculo = "Mercedes-Benz",
        modelo_de_vehiculo = "230 G",
        motor = "I4 2.3Lts",
        descripcion_vehiculo = "Camioneta 4x4, muy eficiente.",
        nacionalidad_de_fabricante = "Aleman").save()

#VEHICULOS JAPONESES

Japones(marca_de_vehiculo = "Toyota",
        modelo_de_vehiculo = "Supra 2020",
        motor = "I4 1.9Lts",
        descripcion_vehiculo = "Vehiculo rapido japones.",
        nacionalidad_de_fabricante = "Japones").save()

Japones(marca_de_vehiculo = "Mazda",
        modelo_de_vehiculo = "MX5 1990",
        motor = "I4 1.6Lts",
        descripcion_vehiculo = "Vehiculo del segmento 'C' japones.",
        nacionalidad_de_fabricante = "Japones").save()

Japones(marca_de_vehiculo = "Toyota",
        modelo_de_vehiculo = "Land Cruiser 76",
        motor = "I6 4.5Lts",
        descripcion_vehiculo = "Reconocida como la mejor camioneta OffRoad de la historia.",
        nacionalidad_de_fabricante = "Japones").save()






