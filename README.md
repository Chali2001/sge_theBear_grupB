# sge_theBear_grupB
![model_10-04-2025.png](fotos/model_10-04-2025.png)


## CRUD DE PUNTO DE VENTA

### GET
Fem un get de tots els Punts de Venta
![alt text](fotos/Punt_Venta/foto3.png)

Ara, fem un get pero de un Punt de venda, que aquest s'escollirà per la id
![alt text](fotos/Punt_Venta/foto2.png)

### POST
Creem un Punt de venda, es important dir que l'únic atribut obligatori de posar és reserva
![alt text](fotos/Punt_Venta/foto1.png)

### PUT
L'update es pot fer de tots els atributs alhora o fer-ho per individual

Aquest és un update de tots els atributs alhora
![alt text](fotos/Punt_Venta/putPuntoVenta.png)

Ara, actualitzarem id_pedido
![alt text](fotos/Punt_Venta/putPuntoVentaPedido.png)

Actualitzarem reserva, que aquest es un bool(True o False)
![alt text](fotos/Punt_Venta/putPuntoVentaReserva.png)

L'ultim update serà per actualitzar la id_factura
![alt text](fotos/Punt_Venta/putPuntoVentaFactura.png)

### DELETE
El delete, busca una id d'un Punt de venda i l'elimina
![alt text](fotos/Punt_Venta/DeletePuntoVenta.png)

## CRUD DE FACTURA

### GET
Primer, un get de totes les factures
![alt text](fotos/Factura/getAllFactura.png)

Després, buscarem per id
![alt text](fotos/Factura/getIDFactura.png)

### POST
Amb els post es pot afegir una factura, tots els atributs son Obligatoris
![alt text](fotos/Factura/postFactura.png)

### PUT
L'update es pot fer de tots els atributs alhora o fer-ho per individual

Primer, el update de tots els atributs
![alt text](fotos/Factura/putFactura.png)

Com l'altre, es pot canviar dada per dada, aquesta vegada el cost
![alt text](fotos/Factura/putFacturaCosto.png)

Ara ho podem fer de la data(Tipus de dada: date)
![alt text](fotos/Factura/putFacturaFecha.png)

I per últim del Estat de la factura que es un enum
![alt text](fotos/Factura/putFacturaEstado.png)

### DELETE

I com Punt de venda, ho podem eliminar per id
![alt text](fotos/Factura/DeleteFactura.png)

## CRUD DE PRODUCTOS

### GET

Fem un get de tots el productes.
![alt text](fotos/Producto/Get_Producto.png)

Ara el mateix pero de un producte en especific usant la seva ID
![alt text](fotos/Producto/Get_Producto_ID.png)

### POST

Crearem un producte, on tots els camps son obligatoris
![alt text](fotos/Producto/Create_Producto.png)

### PUT

Amb l'update podrem actualitzar tots els camps alhora o individualment

Amb aquest update actualitzarem tots els camps
![alt text](fotos/Producto/Update_Producto.png)

Amb aquest actualitzarem el camp de preu individualment
![alt text](fotos/Producto/Update_Producto_Precio.png)

I amb aquest el stock
![alt text](fotos/Producto/Update_Producto_Stock.png)

### DELETE

Amb el delete podrem eliminar un producte usant la seva ID
![alt text](fotos/Producto/Delete_Producto.png)


## CRUD DE PEDIDOS

# GET

Amb el get podrem veure totes le comandes creades, el seu estat, el client asociat a la comanda i el producte.
![alt text](fotos/Pedido/Get_Pedido.png)

Amb el seguent Get tan sols veurem la comanda asociada al ID introduit
![alt text](fotos/Pedido/Get_Pedido_ID.png)

# POST

Ara crearem una comanda introduit el ID del client i el del producte
![alt text](fotos/Pedido/Create_Pedido.png)

# PUT

Amb el update podrem actualizar el estat de la comanda
![alt text](fotos/Pedido/Update_Pedido_Estado.png)

# DELETE

El delete eliminara la comanda amb el ID introduit
![alt text](fotos/Pedido/Delete_Pedido.png)