# Ejemplo de una API REST👩‍💻

_Esta es la aplicación web oficial que gestiona todos los servicios de nuestra empresa Nibblux._

### Instrucciones de instalación 💾

* Instalar Anaconda o Miniconda en su equipo, puede descargarlo [aquí](https://docs.conda.io/en/latest/miniconda.html).
* Crear un nuevo entorno virtual, para ello use el comando
```
conda create -n api-rest-ejemplo python==3.9.0
```
* Active el entorno que acaba de crear usando el comando
```
conda activate api-rest-ejemplo
```
* Instale las librerias del proyecto contenidas en el archivo requirements.txt
```
pip install -r requirements.txt
```
* Corra las migraciones contenidas en el proyecto
```
python manage.py migrate
```
* Corra el archivo manage.py con el siguiente comando en su terminal (debe tener su entorno virtual activado)
```
python manage.py runserver
```