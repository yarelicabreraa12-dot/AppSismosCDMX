import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "🚨 App Sismos CDMX"
    page.bgcolor = "#FFFFFF"
    page.padding = 0
    
    # ========== FUNCIÓN PARA VOLVER AL MENÚ ==========
    def volver_menu(e):
        page.clean()
        mostrar_menu()
    
    # ========== MENÚ PRINCIPAL ==========
    def mostrar_menu():
        page.clean()
        
        # Encabezado
        encabezado = ft.Container(
            content=ft.Column([
                ft.Text("🚨", size=40, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    "APP SISMOS CDMX",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color="#FFFFFF"
                ),
                ft.Text(
                    "Sistema de Prevención Sísmica",
                    size=14,
                    text_align=ft.TextAlign.CENTER,
                    color="#FFCDD2"
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="#C62828",
            padding=20,
            height=150
        )
        
        # Función para crear botones
        def crear_boton(texto, color, accion):
            return ft.Container(
                content=ft.ElevatedButton(
                    text=texto,
                    bgcolor=color,
                    color="#FFFFFF",
                    width=350,
                    height=60,
                    on_click=accion
                ),
                margin=5
            )
        
        # Lista de botones
        botones = ft.Column([
            crear_boton(
                "📊 Información de Sismos",
                "#E53935",
                lambda e: pantalla_info_sismos()
            ),
            crear_boton(
                "🛡️ Recomendaciones Preventivas",
                "#E53935",
                lambda e: pantalla_prevencion()
            ),
            crear_boton(
                "⚠️ Instrucciones DURANTE Sismo",
                "#E53935",
                lambda e: pantalla_durante_sismo()
            ),
            crear_boton(
                "✅ Acciones DESPUÉS del Sismo",
                "#E53935",
                lambda e: pantalla_post_sismo()
            ),
            crear_boton(
                "🆘 BOTÓN SOS",
                "#B71C1C",
                lambda e: pantalla_sos()
            ),
            crear_boton(
                "📝 Registrar Sismo",
                "#F57C00",
                lambda e: pantalla_registrar()
            ),
            crear_boton(
                "🎒 Kit de Emergencia",
                "#F57C00",
                lambda e: pantalla_kit()
            ),
            crear_boton(
                "📞 Contactos de Emergencia",
                "#F57C00",
                lambda e: pantalla_contactos()
            ),
        ], scroll=ft.ScrollMode.AUTO, spacing=0)
        
        # Créditos de las creadoras
        creditos = ft.Container(
            content=ft.Column([
                ft.Divider(height=1, color="#E0E0E0"),
                ft.Text(
                    "👩‍💻 Creadoras de la App",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color="#C62828"
                ),
                ft.Text(
                    "Vazquez Torralva Abigail Valeria",
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    color="#424242"
                ),
                ft.Text(
                    "Cabrera Cruz Yareli Rubi",
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    color="#424242"
                ),
                ft.Text(
                    "Ramirez Bautista Jimena Monserrat",
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    color="#424242"
                ),
                ft.Text(
                    "Ortiz Garcia Italia Nicole",
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    color="#424242"
                ),
                ft.Text(
                    "© 2025",
                    size=10,
                    text_align=ft.TextAlign.CENTER,
                    color="#757575"
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            padding=15,
            bgcolor="#F5F5F5"
        )
        
        # Agregar todo a la página
        page.add(
            encabezado,
            ft.Container(
                content=botones,
                alignment=ft.alignment.center,
                padding=15
            ),
            creditos
        )
        page.update()
    
    # ========== PANTALLA INFO SISMOS ==========
    def pantalla_info_sismos():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "📊 SISMOS RECIENTES",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        # Datos de sismos
        sismos = [
            {"fecha": "15 Enero 2024", "magnitud": 5.2, "epicentro": "Guerrero", "prof": 45},
            {"fecha": "10 Enero 2024", "magnitud": 4.8, "epicentro": "Oaxaca", "prof": 12},
            {"fecha": "05 Enero 2024", "magnitud": 3.9, "epicentro": "Puebla", "prof": 58}
        ]
        
        # Crear tarjetas
        def crear_tarjeta_sismo(sismo):
            return ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f"📅 {sismo['fecha']}", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Magnitud: {sismo['magnitud']}"),
                        ft.Text(f"Epicentro: {sismo['epicentro']}"),
                        ft.Text(f"Profundidad: {sismo['prof']} km"),
                    ]),
                    padding=15,
                    width=350
                ),
                elevation=3
            )
        
        lista_sismos = ft.Column([
            crear_tarjeta_sismo(sismo) for sismo in sismos
        ], spacing=10, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            ft.Container(content=lista_sismos, padding=15, expand=True),
            ft.Container(
                content=ft.Text(
                    "📡 Fuente: Servicio Sismológico Nacional",
                    size=12,
                    color="#616161",
                    text_align=ft.TextAlign.CENTER
                ),
                padding=10
            )
        )
        page.update()
    
    # ========== PANTALLA PREVENCIÓN ==========
    def pantalla_prevencion():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "🛡️ PREVENCIÓN",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        recomendaciones = [
            "Identifica las ZONAS SEGURAS en tu casa, escuela y trabajo",
            "Participa en SIMULACROS regularmente",
            "Prepara un KIT DE EMERGENCIA familiar",
            "Asegura MUEBLES PESADOS a las paredes",
            "Conoce la ubicación de LLAVES de gas y agua",
            "Ten a la mano CONTACTOS DE EMERGENCIA",
            "Revisa que tu edificio cumpla con NORMAS ANTISÍSMICAS",
            "Mantén DOCUMENTOS IMPORTANTES en lugar accesible",
            "Establece un PUNTO DE REUNIÓN familiar",
            "Descarga la app de ALERTA SÍSMICA oficial"
        ]
        
        def crear_card_recomendacion(texto):
            return ft.Card(
                content=ft.Container(
                    content=ft.Row([
                        ft.Text("✅", size=24),
                        ft.Text(texto, size=14, expand=True)
                    ]),
                    padding=15,
                    width=350
                ),
                elevation=2
            )
        
        lista_recomendaciones = ft.Column([
            crear_card_recomendacion(rec) for rec in recomendaciones
        ], spacing=8, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            ft.Container(content=lista_recomendaciones, padding=15, expand=True),
            ft.Container(
                content=ft.Text(
                    "⚠️ La preparación salva vidas",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#C62828",
                    text_align=ft.TextAlign.CENTER
                ),
                padding=15
            )
        )
        page.update()
    
    # ========== PANTALLA DURANTE SISMO ==========
    def pantalla_durante_sismo():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "⚠️ DURANTE EL SISMO",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        # Texto de instrucciones
        texto_instrucciones = ft.Text(
            "Selecciona tu ubicación",
            size=15,
            color="#000000"
        )
        
        area_instrucciones = ft.Container(
            content=texto_instrucciones,
            bgcolor="#FFEBEE",
            padding=20,
            border_radius=10,
            expand=True
        )
        
        # Función para mostrar instrucciones
        def mostrar_instrucciones(ubicacion):
            instrucciones = {
                "casa": """🏠 EN CASA:

🔺 Mantén la CALMA
🔺 Aléjate de VENTANAS y ESPEJOS
🔺 Protégete bajo MESA RESISTENTE
🔺 Aléjate de objetos que puedan caer
🔺 NO uses ELEVADORES
🔺 NO salgas durante el temblor

⚠️ AGACHARSE, CUBRIRSE Y SUJETARSE""",
                
                "escuela": """🏫 EN ESCUELA:

🔺 Sigue indicaciones del MAESTRO
🔺 Ubícate en ZONA SEGURA
🔺 Aléjate de VENTANAS
🔺 Protege CABEZA y CUELLO
🔺 NO corras hacia salidas
🔺 Mantén la calma

⚠️ ZONA SEGURA ESCOLAR""",
                
                "oficina": """🏢 EN OFICINA:

🔺 Aléjate de VENTANALES
🔺 Protégete bajo ESCRITORIO
🔺 NO uses ELEVADORES
🔺 Aléjate de LIBREROS
🔺 Si estás en piso alto, NO bajes
🔺 Espera a que termine el movimiento

⚠️ MANTÉN LA CALMA""",
                
                "vehiculo": """🚗 EN VEHÍCULO:

🔺 DETENTE en lugar seguro
🔺 Aléjate de PUENTES y CABLES
🔺 Permanece DENTRO del vehículo
🔺 Enciende luces INTERMITENTES
🔺 Escucha la RADIO

⚠️ NO SALGAS DEL AUTO""",
                
                "calle": """🛣️ EN LA CALLE:

🔺 Aléjate de EDIFICIOS y POSTES
🔺 Busca ÁREA ABIERTA
🔺 Protege tu CABEZA
🔺 Aléjate de ANUNCIOS
🔺 NO te acerques a fachadas

⚠️ BUSCA ESPACIO ABIERTO"""
            }
            texto_instrucciones.value = instrucciones.get(ubicacion, "Selecciona una opción")
            page.update()
        
        # Botones de ubicación
        botones = ft.Column([
            ft.Text("¿Dónde te encuentras?", size=16, weight=ft.FontWeight.BOLD),
            ft.Row([
                ft.ElevatedButton(
                    "🏠 Casa",
                    bgcolor="#1976D2",
                    color="#FFFFFF",
                    expand=True,
                    on_click=lambda e: mostrar_instrucciones("casa")
                ),
                ft.ElevatedButton(
                    "🏫 Escuela",
                    bgcolor="#1976D2",
                    color="#FFFFFF",
                    expand=True,
                    on_click=lambda e: mostrar_instrucciones("escuela")
                )
            ], spacing=10),
            ft.Row([
                ft.ElevatedButton(
                    "🏢 Oficina",
                    bgcolor="#1976D2",
                    color="#FFFFFF",
                    expand=True,
                    on_click=lambda e: mostrar_instrucciones("oficina")
                ),
                ft.ElevatedButton(
                    "🚗 Vehículo",
                    bgcolor="#1976D2",
                    color="#FFFFFF",
                    expand=True,
                    on_click=lambda e: mostrar_instrucciones("vehiculo")
                )
            ], spacing=10),
            ft.ElevatedButton(
                "🛣️ Calle",
                bgcolor="#1976D2",
                color="#FFFFFF",
                width=350,
                on_click=lambda e: mostrar_instrucciones("calle")
            )
        ], spacing=10)
        
        page.add(
            encabezado,
            ft.Container(content=botones, padding=15),
            ft.Container(content=area_instrucciones, padding=15, expand=True)
        )
        page.update()
    
    # ========== PANTALLA POST SISMO ==========
    def pantalla_post_sismo():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "✅ DESPUÉS DEL SISMO",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        acciones = [
            "1️⃣ Mantén la CALMA y verifica tu estado",
            "2️⃣ Revisa si hay LESIONADOS y presta primeros auxilios",
            "3️⃣ Evacúa si es necesario (sin correr)",
            "4️⃣ Verifica FUGAS DE GAS (por olor, no enciendas cerillos)",
            "5️⃣ Cierra las llaves de GAS y AGUA",
            "6️⃣ Desconecta la ELECTRICIDAD si hay daños",
            "7️⃣ NO enciendas cerillos ni uses INTERRUPTORES",
            "8️⃣ Revisa DAÑOS ESTRUCTURALES en el edificio",
            "9️⃣ Usa el teléfono SOLO para emergencias",
            "🔟 Mantente informado por RADIO",
        ]
        
        lista = ft.Column([
            ft.Card(
                content=ft.Container(
                    content=ft.Text(accion, size=14),
                    padding=15,
                    width=350
                ),
                elevation=2
            ) for accion in acciones
        ], spacing=8, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            ft.Container(content=lista, padding=15, expand=True),
            ft.Container(
                content=ft.Text(
                    "⏰ Las réplicas pueden ocurrir minutos, horas o días después",
                    size=14,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD
                ),
                padding=15,
                bgcolor="#FFF3E0"
            )
        )
        page.update()
    
    # ========== PANTALLA SOS ==========
    def pantalla_sos():
        page.clean()
        page.bgcolor = "#B71C1C"
        
        # Variable para controlar el estado de la alarma
        alarma_activa = {"estado": False}
        
        # Audio de emergencia (beep continuo simulado)
        audio_alarma = ft.Audio(
            src="https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3",
            autoplay=False,
            volume=1,
            balance=0,
            on_loaded=lambda _: print("Audio cargado"),
        )
        page.overlay.append(audio_alarma)
        
        # Botón de alarma
        boton_alarma = ft.ElevatedButton(
            content=ft.Text("🔔 ACTIVAR ALARMA", size=20, weight=ft.FontWeight.BOLD),
            bgcolor="#FF9800",
            color="#FFFFFF",
            width=300,
            height=80,
        )
        
        def toggle_alarma(e):
            if not alarma_activa["estado"]:
                # Activar alarma
                alarma_activa["estado"] = True
                boton_alarma.content = ft.Text("🔕 DESACTIVAR ALARMA", size=20, weight=ft.FontWeight.BOLD)
                boton_alarma.bgcolor = "#4CAF50"
                audio_alarma.src = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"
                audio_alarma.autoplay = True
                audio_alarma.release_mode = ft.audio.ReleaseMode.LOOP
                audio_alarma.update()
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("🔔 Alarma de emergencia ACTIVADA"),
                    bgcolor="#FF9800"
                )
                page.snack_bar.open = True
            else:
                # Desactivar alarma
                alarma_activa["estado"] = False
                boton_alarma.content = ft.Text("🔔 ACTIVAR ALARMA", size=20, weight=ft.FontWeight.BOLD)
                boton_alarma.bgcolor = "#FF9800"
                audio_alarma.pause()
                audio_alarma.update()
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("🔕 Alarma de emergencia DESACTIVADA"),
                    bgcolor="#4CAF50"
                )
                page.snack_bar.open = True
            page.update()
        
        boton_alarma.on_click = toggle_alarma
        
        def llamar_911(e):
            def cerrar_dialogo(e):
                dialogo.open = False
                page.update()
            
            def confirmar_llamada(e):
                dialogo.open = False
                page.update()
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("📞 Llamando al 911..."),
                    bgcolor="#4CAF50"
                )
                page.snack_bar.open = True
                page.update()
            
            dialogo = ft.AlertDialog(
                title=ft.Text("⚠️ LLAMADA DE EMERGENCIA"),
                content=ft.Text("¿Confirmas llamar al 911?"),
                actions=[
                    ft.TextButton("SÍ, LLAMAR", on_click=confirmar_llamada),
                    ft.TextButton("Cancelar", on_click=cerrar_dialogo)
                ]
            )
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        
        titulo = ft.Container(
            content=ft.Text(
                "🆘 EMERGENCIA",
                size=36,
                weight=ft.FontWeight.BOLD,
                color="#FFFFFF",
                text_align=ft.TextAlign.CENTER
            ),
            padding=20
        )
        
        # Contenedor para botón de alarma
        contenedor_alarma = ft.Container(
            content=boton_alarma,
            padding=10
        )
        
        boton_911 = ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text("📞 LLAMAR 911", size=28, weight=ft.FontWeight.BOLD),
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300,
                height=120,
                on_click=llamar_911
            ),
            padding=20
        )
        
        otros_servicios = ft.Column([
            ft.Text(
                "OTROS SERVICIOS DE EMERGENCIA",
                size=16,
                color="#FFFFFF",
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            ft.ElevatedButton(
                "📍 Compartir Mi Ubicación",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300
            ),
            ft.ElevatedButton(
                "🚒 Bomberos",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300,
                on_click=llamar_911
            ),
            ft.ElevatedButton(
                "🚑 Cruz Roja",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300
            ),
            ft.ElevatedButton(
                "🏥 Protección Civil",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        
        instrucciones = ft.Container(
            content=ft.Column([
                ft.Text(
                    "⚠️ SI ESTÁS ATRAPADO:",
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                ),
                ft.Text("• Golpea 3 veces, pausa, 3 veces (SOS)", size=12, color="#FFFFFF"),
                ft.Text("• Usa un SILBATO si lo tienes", size=12, color="#FFFFFF"),
                ft.Text("• Grita solo si es necesario", size=12, color="#FFFFFF"),
                ft.Text("• Protege boca y nariz del polvo", size=12, color="#FFFFFF")
            ]),
            bgcolor="#424242",
            padding=15,
            border_radius=10
        )
        
        def volver_y_detener(e):
            # Detener alarma si está activa
            if alarma_activa["estado"]:
                audio_alarma.pause()
                audio_alarma.update()
            setattr(page, 'bgcolor', "#FFFFFF")
            volver_menu(e)
        
        boton_volver = ft.ElevatedButton(
            "← Volver al Menú",
            bgcolor="#424242",
            color="#FFFFFF",
            on_click=volver_y_detener
        )
        
        page.add(
            ft.Column([
                titulo,
                contenedor_alarma,
                boton_911,
                otros_servicios,
                instrucciones,
                boton_volver
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20, scroll=ft.ScrollMode.AUTO)
        )
        page.update()
    
    # ========== PANTALLA REGISTRAR SISMO ==========
    def pantalla_registrar():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "📝 REGISTRAR SISMO",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        input_magnitud = ft.TextField(
            label="Magnitud (Escala Richter)",
            hint_text="Ej: 5.2",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=350
        )
        
        dropdown_profundidad = ft.Dropdown(
            label="Profundidad",
            options=[
                ft.dropdown.Option("Superficial (0-70km)"),
                ft.dropdown.Option("Intermedio (70-300km)"),
                ft.dropdown.Option("Profundo (>300km)")
            ],
            width=350
        )
        
        input_zona = ft.TextField(
            label="Zona/Epicentro",
            hint_text="Ej: Guerrero, Oaxaca...",
            width=350
        )
        
        input_intensidad = ft.TextField(
            label="Intensidad (I-XII)",
            hint_text="Ej: VI",
            width=350
        )
        
        checkbox_sentiste = ft.Checkbox(label="¿Lo sentiste?")
        
        def guardar_sismo(e):
            if input_magnitud.value:
                try:
                    magnitud = float(input_magnitud.value)
                    
                    if magnitud < 4.0:
                        nivel = "🟢 SISMO MENOR"
                        desc = "Generalmente no causa daños"
                    elif magnitud < 5.0:
                        nivel = "🟡 SISMO LIGERO"
                        desc = "Puede causar daños menores"
                    elif magnitud < 6.0:
                        nivel = "🟠 SISMO MODERADO"
                        desc = "Puede causar daños considerables"
                    elif magnitud < 7.0:
                        nivel = "🔴 SISMO FUERTE"
                        desc = "Puede causar daños severos"
                    else:
                        nivel = "🔴 SISMO MAYOR"
                        desc = "Puede causar destrucción"
                    
                    def cerrar(e):
                        dialogo.open = False
                        page.update()
                        input_magnitud.value = ""
                        input_zona.value = ""
                        input_intensidad.value = ""
                        checkbox_sentiste.value = False
                        page.update()
                    
                    dialogo = ft.AlertDialog(
                        title=ft.Text("✅ Sismo Registrado"),
                        content=ft.Text(f"Guardado exitosamente\n\nNivel: {nivel}\n{desc}"),
                        actions=[ft.TextButton("OK", on_click=cerrar)]
                    )
                    page.dialog = dialogo
                    dialogo.open = True
                    page.update()
                    
                except:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text("❌ Ingresa una magnitud válida"),
                        bgcolor="#D32F2F"
                    )
                    page.snack_bar.open = True
                    page.update()
            else:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("❌ Por favor ingresa la magnitud"),
                    bgcolor="#D32F2F"
                )
                page.snack_bar.open = True
                page.update()
        
        boton_guardar = ft.ElevatedButton(
            "💾 GUARDAR SISMO",
            bgcolor="#4CAF50",
            color="#FFFFFF",
            width=350,
            height=60,
            on_click=guardar_sismo
        )
        
        formulario = ft.Column([
            input_magnitud,
            dropdown_profundidad,
            input_zona,
            input_intensidad,
            checkbox_sentiste,
            boton_guardar
        ], spacing=15, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            ft.Container(content=formulario, padding=20, expand=True)
        )
        page.update()
    
    # ========== PANTALLA KIT DE EMERGENCIA ==========
    def pantalla_kit():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "🎒 KIT DE EMERGENCIA",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        progreso_label = ft.Text(
            "Progreso: 0/10 (0%)",
            size=18,
            weight=ft.FontWeight.BOLD,
            color="#2E7D32"
        )
        
        progreso_container = ft.Container(
            content=progreso_label,
            padding=15,
            bgcolor="#E8F5E9"
        )
        
        items_kit = [
            "Agua (3 litros por persona)",
            "Alimentos no perecederos",
            "Botiquín de primeros auxilios",
            "Linterna y pilas",
            "Radio portátil",
            "Silbato",
            "Documentos importantes",
            "Dinero en efectivo",
            "Medicamentos",
            "Herramientas básicas"
        ]
        
        checkboxes = []
        
        def actualizar_progreso(e):
            completados = sum(1 for cb in checkboxes if cb.value)
            total = len(checkboxes)
            porcentaje = (completados / total) * 100
            progreso_label.value = f"Progreso: {completados}/{total} ({porcentaje:.0f}%)"
            if porcentaje == 100:
                progreso_label.value += " 🎉 ¡COMPLETO!"
            page.update()
        
        def crear_item_kit(texto):
            checkbox = ft.Checkbox(
                label=texto,
                on_change=actualizar_progreso
            )
            checkboxes.append(checkbox)
            
            return ft.Card(
                content=ft.Container(
                    content=checkbox,
                    padding=10,
                    width=350
                ),
                elevation=2
            )
        
        lista_kit = ft.Column([
            crear_item_kit(item) for item in items_kit
        ], spacing=8, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            progreso_container,
            ft.Container(content=lista_kit, padding=15, expand=True)
        )
        page.update()
    
    # ========== PANTALLA CONTACTOS DE EMERGENCIA ==========
    def pantalla_contactos():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "📞 CONTACTOS",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        contactos_lista = []
        
        lista_contactos_text = ft.Text(
            "No hay contactos guardados",
            size=14,
            color="#616161"
        )
        
        lista_contactos_container = ft.Container(
            content=lista_contactos_text,
            padding=15,
            expand=True
        )
        
        input_nombre = ft.TextField(
            label="Nombre completo",
            width=350
        )
        
        input_telefono = ft.TextField(
            label="Teléfono (10 dígitos)",
            keyboard_type=ft.KeyboardType.PHONE,
            width=350
        )
        
        input_relacion = ft.TextField(
            label="Relación (familiar/amigo)",
            width=350
        )
        
        def actualizar_lista():
            if contactos_lista:
                texto = "📞 CONTACTOS DE EMERGENCIA\n\n"
                for i, contacto in enumerate(contactos_lista, 1):
                    texto += f"{i}. {contacto['nombre']}\n"
                    texto += f"   📱 {contacto['telefono']}\n"
                    texto += f"   👤 {contacto['relacion']}\n\n"
                lista_contactos_text.value = texto
            else:
                lista_contactos_text.value = "No hay contactos guardados"
            page.update()
        
        def agregar_contacto(e):
            if input_nombre.value and input_telefono.value:
                if len(input_telefono.value) == 10:
                    contacto = {
                        "nombre": input_nombre.value,
                        "telefono": input_telefono.value,
                        "relacion": input_relacion.value or "No especificada"
                    }
                    contactos_lista.append(contacto)
                    
                    input_nombre.value = ""
                    input_telefono.value = ""
                    input_relacion.value = ""
                    
                    actualizar_lista()
                    
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text("✅ Contacto agregado"),
                        bgcolor="#4CAF50"
                    )
                    page.snack_bar.open = True
                    page.update()
                else:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text("❌ El teléfono debe tener 10 dígitos"),
                        bgcolor="#D32F2F"
                    )
                    page.snack_bar.open = True
                    page.update()
            else:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("❌ Completa nombre y teléfono"),
                    bgcolor="#D32F2F"
                )
                page.snack_bar.open = True
                page.update()
        
        formulario = ft.Container(
            content=ft.Column([
                ft.Text("Agregar Nuevo Contacto", weight=ft.FontWeight.BOLD, size=16),
                input_nombre,
                input_telefono,
                input_relacion,
                ft.ElevatedButton(
                    "➕ Agregar Contacto",
                    bgcolor="#4CAF50",
                    color="#FFFFFF",
                    width=350,
                    on_click=agregar_contacto
                )
            ], spacing=10),
            bgcolor="#F5F5F5",
            padding=15,
            border_radius=10
        )
        
        page.add(
            encabezado,
            ft.Container(content=formulario, padding=15),
            lista_contactos_container
        )
        page.update()
    
    # ========== INICIAR APP ==========
    mostrar_menu()

# Ejecutar la app
ft.app(target=main)