# Repositorio #
http://code.google.com/p/django-bigua/source

# Requisitos #
  * Si estoy en el medio de una transacción extensa, que guarde registros en caso de caída del sistema.
  * Utilizar iconos, no solo texto.
  * Colores amigables.
  * Letra grande.
  * Ayuda en línea.
  * Idiomas.
  * Estadísticas. Permitir filtrar los datos por variados parámetros.

# Dudas #
  * ¿Qué datos son necesarios para el login además de la contraseña?
    * **¿Número de socio?**
    * ¿Usuario?
    * ¿Cédula?
    * ¿Cualquiera de los anteriores?
  * ¿Qué pasa cuando un invitado (socio o no) quiere cancelar la reserva?
    * **¿Cancela la reserva?**
    * ¿Cancela su parte y deja la reserva incompleta?
    * ¿Se le informa al admin?
  * ¿El admin puede cancelar la reserva de un usuario?
    * **Sí, pero el usuario debe especificar que se lo permite.**

Opción: El admin puede cancelar la reserva, siempre que lo haga dentro del margen correspondiente. La función del margen es que otro usuario pueda registrar la cancha, no que lo haga el mismo usuario, por lo que esta función se cumple. El público de la cancha de tenis es gente que no siempre tiene una computadora con conexión a Internet a mano, pero si al menos un teléfono celular.

:wq