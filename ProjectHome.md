# Proyecto Biguá #
Un sistema de reserva de canchas de tenis, enfocado en usabilidad.

## ¿Qué es? ##
Es una aplicación web desarrollada como tercer obligatorio para la materia Análisis de Sistemas de la carrera [Analista Programador](http://www.ort.edu.uy/index.php?id=AAAHAHAB) de la [Universidad ORT, Uruguay](http://www.ort.edu.uy/). Puedes verlo en funcionamiento en el [sitio de prueba](http://bigua.django.dnsalias.net). Si no anda es porque apagué la máquina =)

**Docente**: Carlos Nieves

Para obtener una copia del [código fuente del sistema](http://code.google.com/p/django-bigua/source) basta con hacer un [checkout](http://svnbook.red-bean.com/nightly/en/svn.ref.svn.c.checkout.html) del [svn](http://subversion.tigris.org/):
```
svn checkout http://django-bigua.googlecode.com/svn/trunk/ django-bigua
```
Sino puedes [bajarte el código comprimido](http://code.google.com/p/django-bigua/downloads/list), con la desventaja de que seguramente esté desactualizado con respecto al svn.

### Datos de prueba ###
#### Socio ####
  * Usuario: ana
  * Password: ana

  * Usuario: danny
  * Password: danny

#### Administrador ####
  * Usuario: alvaro
  * Password: alvaro
_Use con responsabilidad =)_

## Desarrolladores ##
  * Alvaro Mouriño
  * Daniel Alaniz

Sitio desarrollado en [python](http://www.python.org/), sobre [django](http://www.djangoproject.com/). Puedes leer toda la [documentación de django](http://www.djangoproject.com/documentation/), este maravilloso framework para desarrollo web, en el sitio del proyecto donde además encontrarás una [guía paso a paso de como instalarlo](http://www.djangoproject.com/documentation/install/) en tu sistema operativo preferido.

## Características ##
  * Diseñado [potenciando la usabilidad](http://code.google.com/p/django-bigua/wiki/FirstPrinciplesOfInteractionDesign) sin sacrificar accesibilidad.
  * Todo el sitio es usable sin javascript.
  * A partir de las 11:50 se habilita el alquiler para el día siguiente: Para esto chequea contra un servidor NTP la hora actual, si éste no responde, o no devuelve información comprensible se utiliza la hora del sistema (servidor).
  * 100% traducido al inglés.
  * 100% traducible a otros idiomas.
  * XHTML 1.0 válido.
  * Diseño testeado en IE, Gecko y KHTML.

## Apps y bibliotecas de terceros ##
  * [django-menuse](http://code.google.com/p/django-menuse/): Una app para crear menús muy sencilla y práctica.
  * De toda la mágia de la traducción de contenidos se encarga [django-multilingual](http://code.google.com/p/django-multilingual/).
  * Todo el client-side eye-candy se lo debemos a [jquery](http://www.jquery.com/).
  * Utiliza también [behaviour](http://www.bennolan.com/behaviour/) para aplicar reglas de javascript.
  * Los excelentes iconos son gracias al trabajo del [Proyecto Tango Desktop](http://tango.freedesktop.org/Tango_Desktop_Project).

## Bibliografía ##
  * "Don't make me think" Steve Krug. New Riders.
  * "Designing Interfaces" Jenifer Tidwell. O'Reilly.
Ambos libros prestados por la biblioteca de la Universidad. El primero es realmente excelente, sumamente recomendable.

## En fin... ##
Nosotros aprendimos mucho haciéndolo, esperamos que a vos también te sirva.

**FIXME**: Por alguna extraña razón solo funciona en Firefox, en un principio funcionaba también en Internet Exploiter 6 y Konqueror (¿podemos asumir que en Safari también?) pero behaviour tiene algúna incompatibilidad que rompe todo.

**TODO**: Reemplazar la funcionalidad que se utilizaba de behaviour por jquery.

:wq