from gtts import gTTS

texto = """
Lista Celeste.
Decálogo de Compromiso y Acción Gremial.

Uno. Información en tiempo real y multicanal.
Nos comprometemos a romper las barreras de comunicación mediante la implementación de un ecosistema digital integrado: WhatsApp corporativo, redes sociales y boletín informativo, que permita a cada afiliado recibir novedades, beneficios y gestiones al instante, garantizando una comunicación directa y sin intermediarios.

Dos. El reencuentro: hacia la gran fiesta del tres de abril.
Entendemos el valor de la unión fuera del ámbito laboral. Por ello, trabajaremos firmemente en la recuperación de nuestra tradicional celebración del tres de abril, Día del Papelero, proyectándola como el gran evento de fraternidad que todos merecemos.

Tres. Transparencia absoluta ante la controversia.
Nuestra gestión se basará en la claridad técnica y objetiva. Frente a cualquier tema polémico, responderemos con datos precisos y documentación abierta, eliminando dudas y rumores para que el afiliado siempre tenga la certeza de la verdad.

Cuatro. Diálogo firme con las prioridades en el trabajador.
Creemos en la negociación como herramienta fundamental, pero bajo una premisa innegociable: el beneficio del trabajador siempre estará primero. Dialogamos para construir, manteniendo nuestras convicciones intactas ante cualquier conflicto, priorizando en los cuerpos de delegados las metodologías de trabajo y las formas de diálogo con compañeros y empresas.

Cinco. Renovación con base sólida y sangre nueva.
Somos la conjunción entre la experiencia en la gestión gremial y el empuje de compañeros con amplio recorrido en las empresas, que aportan ideas y proyectos innovadores. Este equipo se ha consolidado para afrontar los desafíos actuales y futuros con una mirada moderna y comprometida.

Seis. Democracia participativa: más reuniones y asambleas.
El sindicato se construye de abajo hacia arriba. Por ello, promoveremos reuniones y asambleas periódicas donde cada compañero pueda expresarse, garantizando que las decisiones importantes se tomen de manera colectiva.

Siete. Austeridad y control de activos.
Cuidaremos rigurosamente el patrimonio de la institución. Se utilizarán todas las herramientas necesarias para asegurar una administración eficiente de los recursos, orientada a mejorar los beneficios del afiliado.

Ocho. Un secretario general de puertas abiertas.
Garantizamos la presencia constante del secretario general en la sede sindical, disponible y accesible para escuchar personalmente inquietudes, sugerencias y reclamos de cada compañero que lo requiera.

Nueve. Compromiso con la comunidad y el interés social.
Nuestra institución debe ser un actor activo dentro de la sociedad. Impulsaremos actividades solidarias, culturales y de interés social que fortalezcan el rol del gremio como referente de valores humanos, promoviendo además una participación destacada de las compañeras papeleras y de los compañeros jubilados papeleros.

Diez. Crecimiento integral de la familia gremial.
Potenciaremos el desarrollo del afiliado y su entorno familiar mediante programas de formación, talleres inclusivos y actividades educativas, convencidos de que invertir en el conocimiento y el bienestar de nuestras familias es asegurar el futuro de nuestra organización.

Este es el momento de dar el paso.
Los invitamos a apoyar a la Lista Celeste.

Por un sindicato presente y de los trabajadores.
Vamos por la renovación.
Vamos con la Celeste.

"""

tts = gTTS(text=texto, lang="es", slow=False)
tts.save("lista_celeste.mp3")

print("Audio generado correctamente")