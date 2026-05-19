#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Juego de Modo Carrera de Fútbol Realista
Con futbolistas y clubes reales
"""

import random
import json
from datetime import datetime
from typing import List, Dict, Optional
import os

# ============================================================================
# DATOS DE JUGADORES REALES
# ============================================================================

JUGADORES = [
    # Porteros
    {"nombre": "Thibaut Courtois", "edad": 31, "nacionalidad": "Bélgica", "posicion": "POR", "valor": 45000000, "habilidad": 89},
    {"nombre": "Alisson Becker", "edad": 30, "nacionalidad": "Brasil", "posicion": "POR", "valor": 50000000, "habilidad": 89},
    {"nombre": "Ederson", "edad": 30, "nacionalidad": "Brasil", "posicion": "POR", "valor": 45000000, "habilidad": 87},
    {"nombre": "Jan Oblak", "edad": 30, "nacionalidad": "Eslovenia", "posicion": "POR", "valor": 45000000, "habilidad": 88},
    {"nombre": "Manuel Neuer", "edad": 37, "nacionalidad": "Alemania", "posicion": "POR", "valor": 15000000, "habilidad": 85},
    {"nombre": "Marc-André ter Stegen", "edad": 31, "nacionalidad": "Alemania", "posicion": "POR", "valor": 40000000, "habilidad": 87},
    {"nombre": "Gianluigi Donnarumma", "edad": 24, "nacionalidad": "Italia", "posicion": "POR", "valor": 55000000, "habilidad": 86},
    {"nombre": "Mike Maignan", "edad": 28, "nacionalidad": "Francia", "posicion": "POR", "valor": 35000000, "habilidad": 84},
    
    # Defensas Centrales
    {"nombre": "Virgil van Dijk", "edad": 32, "nacionalidad": "Países Bajos", "posicion": "DEF", "valor": 55000000, "habilidad": 89},
    {"nombre": "Ruben Dias", "edad": 26, "nacionalidad": "Portugal", "posicion": "DEF", "valor": 75000000, "habilidad": 88},
    {"nombre": "Antonio Rudiger", "edad": 30, "nacionalidad": "Alemania", "posicion": "DEF", "valor": 45000000, "habilidad": 85},
    {"nombre": "Marquinhos", "edad": 29, "nacionalidad": "Brasil", "posicion": "DEF", "valor": 60000000, "habilidad": 86},
    {"nombre": "Eder Militao", "edad": 25, "nacionalidad": "Brasil", "posicion": "DEF", "valor": 70000000, "habilidad": 85},
    {"nombre": "William Saliba", "edad": 22, "nacionalidad": "Francia", "posicion": "DEF", "valor": 65000000, "habilidad": 84},
    {"nombre": "Ronald Araujo", "edad": 24, "nacionalidad": "Uruguay", "posicion": "DEF", "valor": 60000000, "habilidad": 84},
    {"nombre": "Alessandro Bastoni", "edad": 24, "nacionalidad": "Italia", "posicion": "DEF", "valor": 55000000, "habilidad": 83},
    
    # Laterales
    {"nombre": "Trent Alexander-Arnold", "edad": 25, "nacionalidad": "Inglaterra", "posicion": "LAT", "valor": 70000000, "habilidad": 86},
    {"nombre": "Alphonso Davies", "edad": 23, "nacionalidad": "Canadá", "posicion": "LAT", "valor": 65000000, "habilidad": 84},
    {"nombre": "Achraf Hakimi", "edad": 25, "nacionalidad": "Marruecos", "posicion": "LAT", "valor": 65000000, "habilidad": 85},
    {"nombre": "Joao Cancelo", "edad": 29, "nacionalidad": "Portugal", "posicion": "LAT", "valor": 50000000, "habilidad": 84},
    {"nombre": "Theo Hernandez", "edad": 26, "nacionalidad": "Francia", "posicion": "LAT", "valor": 60000000, "habilidad": 84},
    {"nombre": "Andrew Robertson", "edad": 29, "nacionalidad": "Escocia", "posicion": "LAT", "valor": 45000000, "habilidad": 83},
    {"nombre": "Kyle Walker", "edad": 33, "nacionalidad": "Inglaterra", "posicion": "LAT", "valor": 25000000, "habilidad": 81},
    {"nombre": "Jules Kounde", "edad": 25, "nacionalidad": "Francia", "posicion": "LAT", "valor": 55000000, "habilidad": 83},
    
    # Mediocentros
    {"nombre": "Kevin De Bruyne", "edad": 32, "nacionalidad": "Bélgica", "posicion": "MED", "valor": 70000000, "habilidad": 91},
    {"nombre": "Rodri", "edad": 27, "nacionalidad": "España", "posicion": "MED", "valor": 90000000, "habilidad": 89},
    {"nombre": "Jude Bellingham", "edad": 20, "nacionalidad": "Inglaterra", "posicion": "MED", "valor": 120000000, "habilidad": 88},
    {"nombre": "Pedri", "edad": 21, "nacionalidad": "España", "posicion": "MED", "valor": 80000000, "habilidad": 85},
    {"nombre": "Gavi", "edad": 19, "nacionalidad": "España", "posicion": "MED", "valor": 70000000, "habilidad": 83},
    {"nombre": "Declan Rice", "edad": 24, "nacionalidad": "Inglaterra", "posicion": "MED", "valor": 90000000, "habilidad": 85},
    {"nombre": "Bruno Fernandes", "edad": 29, "nacionalidad": "Portugal", "posicion": "MED", "valor": 70000000, "habilidad": 86},
    {"nombre": "Luka Modric", "edad": 38, "nacionalidad": "Croacia", "posicion": "MED", "valor": 10000000, "habilidad": 84},
    {"nombre": "Toni Kroos", "edad": 34, "nacionalidad": "Alemania", "posicion": "MED", "valor": 20000000, "habilidad": 85},
    {"nombre": "Frenkie de Jong", "edad": 26, "nacionalidad": "Países Bajos", "posicion": "MED", "valor": 70000000, "habilidad": 85},
    {"nombre": "Federico Valverde", "edad": 25, "nacionalidad": "Uruguay", "posicion": "MED", "valor": 80000000, "habilidad": 85},
    {"nombre": "Martin Odegaard", "edad": 24, "nacionalidad": "Noruega", "posicion": "MED", "valor": 75000000, "habilidad": 85},
    
    # Extremos
    {"nombre": "Vinicius Jr", "edad": 23, "nacionalidad": "Brasil", "posicion": "EXT", "valor": 120000000, "habilidad": 89},
    {"nombre": "Kylian Mbappe", "edad": 25, "nacionalidad": "Francia", "posicion": "EXT", "valor": 180000000, "habilidad": 92},
    {"nombre": "Mohamed Salah", "edad": 31, "nacionalidad": "Egipto", "posicion": "EXT", "valor": 65000000, "habilidad": 88},
    {"nombre": "Bukayo Saka", "edad": 22, "nacionalidad": "Inglaterra", "posicion": "EXT", "valor": 90000000, "habilidad": 85},
    {"nombre": "Phil Foden", "edad": 23, "nacionalidad": "Inglaterra", "posicion": "EXT", "valor": 80000000, "habilidad": 85},
    {"nombre": "Rafael Leao", "edad": 24, "nacionalidad": "Portugal", "posicion": "EXT", "valor": 70000000, "habilidad": 84},
    {"nombre": "Khvicha Kvaratskhelia", "edad": 22, "nacionalidad": "Georgia", "posicion": "EXT", "valor": 75000000, "habilidad": 84},
    {"nombre": "Jamal Musiala", "edad": 20, "nacionalidad": "Alemania", "posicion": "EXT", "valor": 90000000, "habilidad": 84},
    {"nombre": "Lamine Yamal", "edad": 16, "nacionalidad": "España", "posicion": "EXT", "valor": 50000000, "habilidad": 79},
    {"nombre": "Rodrygo", "edad": 23, "nacionalidad": "Brasil", "posicion": "EXT", "valor": 80000000, "habilidad": 84},
    
    # Delanteros
    {"nombre": "Erling Haaland", "edad": 23, "nacionalidad": "Noruega", "posicion": "DEL", "valor": 170000000, "habilidad": 91},
    {"nombre": "Harry Kane", "edad": 30, "nacionalidad": "Inglaterra", "posicion": "DEL", "valor": 90000000, "habilidad": 89},
    {"nombre": "Robert Lewandowski", "edad": 35, "nacionalidad": "Polonia", "posicion": "DEL", "valor": 35000000, "habilidad": 87},
    {"nombre": "Victor Osimhen", "edad": 25, "nacionalidad": "Nigeria", "posicion": "DEL", "valor": 110000000, "habilidad": 86},
    {"nombre": "Lautaro Martinez", "edad": 26, "nacionalidad": "Argentina", "posicion": "DEL", "valor": 90000000, "habilidad": 85},
    {"nombre": "Darwin Nunez", "edad": 24, "nacionalidad": "Uruguay", "posicion": "DEL", "valor": 70000000, "habilidad": 82},
    {"nombre": "Julian Alvarez", "edad": 23, "nacionalidad": "Argentina", "posicion": "DEL", "valor": 70000000, "habilidad": 83},
    {"nombre": "Dusan Vlahovic", "edad": 23, "nacionalidad": "Serbia", "posicion": "DEL", "valor": 70000000, "habilidad": 83},
    {"nombre": "Gabriel Jesus", "edad": 26, "nacionalidad": "Brasil", "posicion": "DEL", "valor": 55000000, "habilidad": 82},
    {"nombre": "Alexander Isak", "edad": 24, "nacionalidad": "Suecia", "posicion": "DEL", "valor": 65000000, "habilidad": 82},
]

# ============================================================================
# DATOS DE CLUBES REALES
# ============================================================================

CLUBES = [
    # La Liga
    {"nombre": "Real Madrid", "liga": "La Liga", "pais": "España", "presupuesto": 200000000, "prestigio": 95},
    {"nombre": "FC Barcelona", "liga": "La Liga", "pais": "España", "presupuesto": 150000000, "prestigio": 94},
    {"nombre": "Atletico Madrid", "liga": "La Liga", "pais": "España", "presupuesto": 100000000, "prestigio": 87},
    {"nombre": "Sevilla FC", "liga": "La Liga", "pais": "España", "presupuesto": 60000000, "prestigio": 82},
    {"nombre": "Real Sociedad", "liga": "La Liga", "pais": "España", "presupuesto": 50000000, "prestigio": 80},
    
    # Premier League
    {"nombre": "Manchester City", "liga": "Premier League", "pais": "Inglaterra", "presupuesto": 220000000, "prestigio": 94},
    {"nombre": "Liverpool FC", "liga": "Premier League", "pais": "Inglaterra", "presupuesto": 180000000, "prestigio": 92},
    {"nombre": "Arsenal FC", "liga": "Premier League", "pais": "Inglaterra", "presupuesto": 160000000, "prestigio": 90},
    {"nombre": "Manchester United", "liga": "Premier League", "pais": "Inglaterra", "presupuesto": 170000000, "prestigio": 91},
    {"nombre": "Chelsea FC", "liga": "Premier League", "pais": "Inglaterra", "presupuesto": 200000000, "prestigio": 89},
    {"nombre": "Tottenham Hotspur", "liga": "Premier League", "pais": "Inglaterra", "presupuesto": 130000000, "prestigio": 86},
    {"nombre": "Newcastle United", "liga": "Premier League", "pais": "Inglaterra", "presupuesto": 120000000, "prestigio": 83},
    
    # Serie A
    {"nombre": "Inter Milan", "liga": "Serie A", "pais": "Italia", "presupuesto": 100000000, "prestigio": 88},
    {"nombre": "AC Milan", "liga": "Serie A", "pais": "Italia", "presupuesto": 110000000, "prestigio": 88},
    {"nombre": "Juventus", "liga": "Serie A", "pais": "Italia", "presupuesto": 120000000, "prestigio": 89},
    {"nombre": "Napoli", "liga": "Serie A", "pais": "Italia", "presupuesto": 90000000, "prestigio": 86},
    {"nombre": "AS Roma", "liga": "Serie A", "pais": "Italia", "presupuesto": 80000000, "prestigio": 84},
    
    # Bundesliga
    {"nombre": "Bayern Munich", "liga": "Bundesliga", "pais": "Alemania", "presupuesto": 180000000, "prestigio": 93},
    {"nombre": "Borussia Dortmund", "liga": "Bundesliga", "pais": "Alemania", "presupuesto": 100000000, "prestigio": 86},
    {"nombre": "RB Leipzig", "liga": "Bundesliga", "pais": "Alemania", "presupuesto": 80000000, "prestigio": 82},
    {"nombre": "Bayer Leverkusen", "liga": "Bundesliga", "pais": "Alemania", "presupuesto": 70000000, "prestigio": 81},
    
    # Ligue 1
    {"nombre": "Paris Saint-Germain", "liga": "Ligue 1", "pais": "Francia", "presupuesto": 200000000, "prestigio": 90},
    {"nombre": "Olympique Marseille", "liga": "Ligue 1", "pais": "Francia", "presupuesto": 60000000, "prestigio": 80},
    {"nombre": "AS Monaco", "liga": "Ligue 1", "pais": "Francia", "presupuesto": 70000000, "prestigio": 79},
    {"nombre": "Olympique Lyon", "liga": "Ligue 1", "pais": "Francia", "presupuesto": 55000000, "prestigio": 78},
]

# Distribución inicial de jugadores por club (aleatoria pero realista)
DISTRIBUCION_INICIAL = {
    "Real Madrid": ["Vinicius Jr", "Jude Bellingham", "Federico Valverde", "Eder Militao", "Rodrygo", "Toni Kroos", "Luka Modric", "Thibaut Courtois", "Antonio Rudiger"],
    "FC Barcelona": ["Pedri", "Gavi", "Robert Lewandowski", "Ronald Araujo", "Jules Kounde", "Marc-André ter Stegen"],
    "Manchester City": ["Erling Haaland", "Kevin De Bruyne", "Rodri", "Ruben Dias", "Phil Foden", "Ederson", "Kyle Walker"],
    "Liverpool FC": ["Mohamed Salah", "Virgil van Dijk", "Alisson Becker", "Trent Alexander-Arnold", "Andrew Robertson", "Darwin Nunez"],
    "Arsenal FC": ["Bukayo Saka", "Martin Odegaard", "William Saliba", "Declan Rice", "Gabriel Jesus"],
    "Paris Saint-Germain": ["Kylian Mbappe"],
    "Bayern Munich": ["Harry Kane", "Manuel Neuer", "Alphonso Davies", "Jamal Musiala"],
    "Inter Milan": ["Lautaro Martinez", "Alessandro Bastoni"],
    "AC Milan": ["Rafael Leao", "Theo Hernandez", "Mike Maignan"],
    "Napoli": ["Victor Osimhen", "Khvicha Kvaratskhelia"],
    "Manchester United": ["Bruno Fernandes"],
    "Chelsea FC": [],
    "Tottenham Hotspur": [],
    "Newcastle United": ["Alexander Isak"],
    "Atletico Madrid": ["Jan Oblak"],
    "Sevilla FC": [],
    "Real Sociedad": [],
    "Juventus": ["Dusan Vlahovic"],
    "AS Roma": [],
    "Borussia Dortmund": [],
    "RB Leipzig": [],
    "Bayer Leverkusen": [],
    "Olympique Marseille": [],
    "AS Monaco": [],
    "Olympique Lyon": [],
}


class Jugador:
    """Clase que representa un jugador de fútbol"""
    
    def __init__(self, datos: Dict):
        self.nombre = datos["nombre"]
        self.edad = datos["edad"]
        self.nacionalidad = datos["nacionalidad"]
        self.posicion = datos["posicion"]
        self.valor = datos["valor"]
        self.habilidad = datos["habilidad"]
        self.club = None
        self.goles_temporada = 0
        self.asistencias_temporada = 0
        self.partidos_jugados = 0
        self.felicidad = 80  # 0-100
        
    def envejecer(self):
        """El jugador envejece un año"""
        self.edad += 1
        if self.edad >= 30:
            self.habilidad -= random.randint(1, 3)
        elif self.edad <= 25:
            self.habilidad += random.randint(0, 2)
        self.habilidad = max(50, min(99, self.habilidad))
        
    def to_dict(self) -> Dict:
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "nacionalidad": self.nacionalidad,
            "posicion": self.posicion,
            "valor": self.valor,
            "habilidad": self.habilidad,
            "club": self.club.nombre if self.club else None,
            "goles_temporada": self.goles_temporada,
            "asistencias_temporada": self.asistencias_temporada,
            "partidos_jugados": self.partidos_jugados,
            "felicidad": self.felicidad
        }
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.edad}) - {self.posicion} - {self.habilidad} OVR - €{self.valor/1000000:.1f}M"


class Club:
    """Clase que representa un club de fútbol"""
    
    def __init__(self, datos: Dict):
        self.nombre = datos["nombre"]
        self.liga = datos["liga"]
        self.pais = datos["pais"]
        self.presupuesto = datos["presupuesto"]
        self.prestigio = datos["prestigio"]
        self.jugadores: List[Jugador] = []
        self.puntos_liga = 0
        self.partidos_jugados = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.victorias = 0
        self.empates = 0
        self.derrotas = 0
        
    def agregar_jugador(self, jugador: Jugador):
        """Agrega un jugador al club"""
        jugador.club = self
        self.jugadores.append(jugador)
        
    def remover_jugador(self, jugador: Jugador):
        """Remueve un jugador del club"""
        if jugador in self.jugadores:
            self.jugadores.remove(jugador)
            jugador.club = None
            
    def valor_plantilla(self) -> int:
        """Calcula el valor total de la plantilla"""
        return sum(j.valor for j in self.jugadores)
    
    def habilidad_promedio(self) -> float:
        """Calcula la habilidad promedio de la plantilla"""
        if not self.jugadores:
            return 0
        return sum(j.habilidad for j in self.jugadores) / len(self.jugadores)
    
    def resetear_estadisticas_temporada(self):
        """Resetea las estadísticas de temporada"""
        self.puntos_liga = 0
        self.partidos_jugados = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.victorias = 0
        self.empates = 0
        self.derrotas = 0
        for jugador in self.jugadores:
            jugador.goles_temporada = 0
            jugador.asistencias_temporada = 0
            jugador.partidos_jugados = 0
    
    def to_dict(self) -> Dict:
        return {
            "nombre": self.nombre,
            "liga": self.liga,
            "pais": self.pais,
            "presupuesto": self.presupuesto,
            "prestigio": self.prestigio,
            "jugadores": [j.to_dict() for j in self.jugadores],
            "puntos_liga": self.puntos_liga,
            "partidos_jugados": self.partidos_jugados,
            "goles_a_favor": self.goles_a_favor,
            "goles_en_contra": self.goles_en_contra,
        }
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.liga}) - Prestigio: {self.prestigio} - Plantilla: {len(self.jugadores)} jugadores"


class Partido:
    """Clase que representa un partido"""
    
    def __init__(self, local: Club, visitante: Club):
        self.local = local
        self.visitante = visitante
        self.goles_local = 0
        self.goles_visitante = 0
        self.jugado = False
        
    def simular(self) -> tuple:
        """Simula el resultado del partido"""
        # Factores que influyen en el resultado
        factor_local = 1.2  # Ventaja de jugar en casa
        habilidad_local = self.local.habilidad_promedio() * factor_local
        habilidad_visitante = self.visitante.habilidad_promedio()
        
        # Variación aleatoria
        variacion = random.uniform(0.8, 1.2)
        
        # Calcular goles esperados
        goles_local_esperados = (habilidad_local / 50) * variacion
        goles_visitante_esperados = (habilidad_visitante / 50) * variacion
        
        # Determinar goles reales con algo de aleatoriedad
        self.goles_local = max(0, int(random.gauss(goles_local_esperados, 1.5)))
        self.goles_visitante = max(0, int(random.gauss(goles_visitante_esperados, 1.5)))
        
        # Limitar goles a un máximo razonable
        self.goles_local = min(self.goles_local, 8)
        self.goles_visitante = min(self.goles_visitante, 8)
        
        self.jugado = True
        
        # Actualizar estadísticas de los clubes
        self.actualizar_estadisticas()
        
        # Asignar goles a jugadores aleatorios (simplificado)
        self.asignar_goles_jugadores()
        
        return self.goles_local, self.goles_visitante
    
    def actualizar_estadisticas(self):
        """Actualiza las estadísticas de liga de ambos clubes"""
        # Local
        self.local.partidos_jugados += 1
        self.local.goles_a_favor += self.goles_local
        self.local.goles_en_contra += self.goles_visitante
        
        # Visitante
        self.visitante.partidos_jugados += 1
        self.visitante.goles_a_favor += self.goles_visitante
        self.visitante.goles_en_contra += self.goles_local
        
        # Puntos
        if self.goles_local > self.goles_visitante:
            self.local.puntos_liga += 3
            self.local.victorias += 1
            self.visitante.derrotas += 1
        elif self.goles_local < self.goles_visitante:
            self.visitante.puntos_liga += 3
            self.visitante.victorias += 1
            self.local.derrotas += 1
        else:
            self.local.puntos_liga += 1
            self.visitante.puntos_liga += 1
            self.local.empates += 1
            self.visitante.empates += 1
    
    def asignar_goles_jugadores(self):
        """Asigna goles a jugadores del equipo ganador"""
        # Asignar goles locales
        for _ in range(self.goles_local):
            if self.local.jugadores:
                jugador = random.choice([j for j in self.local.jugadores if j.posicion in ["DEL", "EXT", "MED"]])
                if jugador:
                    jugador.goles_temporada += 1
                    jugador.partidos_jugados += 1
                    
        # Asignar goles visitantes
        for _ in range(self.goles_visitante):
            if self.visitante.jugadores:
                jugador = random.choice([j for j in self.visitante.jugadores if j.posicion in ["DEL", "EXT", "MED"]])
                if jugador:
                    jugador.goles_temporada += 1
                    jugador.partidos_jugados += 1
    
    def __str__(self) -> str:
        if self.jugado:
            return f"{self.local.nombre} {self.goles_local} - {self.goles_visitante} {self.visitante.nombre}"
        return f"{self.local.nombre} vs {self.visitante.nombre}"


class JuegoCarrera:
    """Clase principal del juego de modo carrera"""
    
    def __init__(self):
        self.clubes: Dict[str, Club] = {}
        self.jugadores_libres: List[Jugador] = []
        self.temporada_actual = 2024
        self.jugador_usuario = None
        self.club_usuario: Club = None
        self.historial_partidos = []
        self.mercado_fichajes = []
        
    def inicializar_juego(self):
        """Inicializa el juego con todos los clubes y jugadores"""
        print("\n" + "="*60)
        print("🏆 INICIALIZANDO JUEGO DE MODO CARRERA 🏆")
        print("="*60)
        
        # Crear clubes
        for datos_club in CLUBES:
            club = Club(datos_club)
            self.clubes[club.nombre] = club
            
        # Crear jugadores y asignarlos a clubes
        jugadores_no_asignados = []
        
        for datos_jugador in JUGADORES:
            jugador = Jugador(datos_jugador)
            asignado = False
            
            # Verificar si tiene asignación inicial
            for club_nombre, lista_jugadores in DISTRIBUCION_INICIAL.items():
                if jugador.nombre in lista_jugadores and club_nombre in self.clubes:
                    self.clubes[club_nombre].agregar_jugador(jugador)
                    asignado = True
                    break
            
            if not asignado:
                jugadores_no_asignados.append(jugador)
        
        # Distribuir jugadores no asignados aleatoriamente entre clubes
        for jugador in jugadores_no_asignados:
            club_aleatorio = random.choice(list(self.clubes.values()))
            club_aleatorio.agregar_jugador(jugador)
        
        print(f"✓ Se crearon {len(self.clubes)} clubes")
        print(f"✓ Se distribuyeron {len(JUGADORES)} jugadores")
        
    def mostrar_menu_principal(self):
        """Muestra el menú principal del juego"""
        print("\n" + "="*60)
        print(f"🎮 MODO CARRERA - Temporada {self.temporada_actual}")
        print("="*60)
        print("\n1. 📊 Ver clasificación de ligas")
        print("2. 👤 Gestionar mi club")
        print("3. ⚽ Jugar jornada")
        print("4. 💰 Mercado de fichajes")
        print("5. 📈 Ver estadísticas personales")
        print("6. 💾 Guardar partida")
        print("7. 🚪 Salir del juego")
        print("="*60)
        
    def seleccionar_club_usuario(self):
        """Permite al usuario seleccionar su club"""
        print("\n" + "="*60)
        print("🏟️  SELECCIONA TU CLUB")
        print("="*60)
        
        # Mostrar clubes por liga
        ligas = {}
        for club in self.clubes.values():
            if club.liga not in ligas:
                ligas[club.liga] = []
            ligas[club.liga].append(club)
        
        numero = 1
        clubes_por_numero = {}
        
        for liga, clubes in ligas.items():
            print(f"\n{liga}:")
            for club in clubes:
                print(f"  {numero}. {club.nombre} (Prestigio: {club.prestigio})")
                clubes_por_numero[numero] = club
                numero += 1
        
        while True:
            try:
                opcion = int(input(f"\nElige tu club (1-{numero-1}): "))
                if opcion in clubes_por_numero:
                    self.club_usuario = clubes_por_numero[opcion]
                    print(f"\n✅ ¡Has seleccionado {self.club_usuario.nombre}!")
                    return
                else:
                    print("❌ Opción inválida")
            except ValueError:
                print("❌ Por favor, introduce un número")
    
    def ver_clasificacion(self):
        """Muestra la clasificación de todas las ligas"""
        print("\n" + "="*60)
        print("📊 CLASIFICACIÓN DE LIGAS")
        print("="*60)
        
        ligas = {}
        for club in self.clubes.values():
            if club.liga not in ligas:
                ligas[club.liga] = []
            ligas[club.liga].append(club)
        
        for liga, clubes in ligas.items():
            print(f"\n{'='*60}")
            print(f"🏆 {liga}")
            print(f"{'='*60}")
            print(f"{'Pos':<4} {'Club':<25} {'PJ':<4} {'G':<4} {'E':<4} {'P':<4} {'GF':<4} {'GC':<4} {'Pts':<4}")
            print("-"*60)
            
            # Ordenar por puntos
            clubes_ordenados = sorted(clubes, key=lambda c: (c.puntos_liga, c.goles_a_favor - c.goles_en_contra), reverse=True)
            
            for pos, club in enumerate(clubes_ordenados, 1):
                diff_goles = club.goles_a_favor - club.goles_en_contra
                print(f"{pos:<4} {club.nombre:<25} {club.partidos_jugados:<4} {club.victorias:<4} {club.empates:<4} {club.derrotas:<4} {club.goles_a_favor:<4} {club.goles_en_contra:<4} {club.puntos_liga:<4}")
    
    def gestionar_club(self):
        """Muestra opciones de gestión del club del usuario"""
        if not self.club_usuario:
            print("❌ Primero debes seleccionar un club")
            return
            
        while True:
            print("\n" + "="*60)
            print(f"🏟️  GESTIÓN DE {self.club_usuario.nombre.upper()}")
            print("="*60)
            print(f"\n💰 Presupuesto: €{self.club_usuario.presupuesto/1000000:.1f}M")
            print(f"⭐ Habilidad promedio: {self.club_usuario.habilidad_promedio():.1f}")
            print(f"👥 Jugadores en plantilla: {len(self.club_usuario.jugadores)}")
            
            print("\n1. 👥 Ver plantilla completa")
            print("2. 🔍 Buscar jugador por nombre")
            print("3. 💸 Ver jugadores más valiosos")
            print("4. 📊 Estadísticas de goleadores")
            print("5. ⬅️ Volver al menú principal")
            
            opcion = input("\nElige una opción: ")
            
            if opcion == "1":
                self.ver_plantilla()
            elif opcion == "2":
                self.buscar_jugador()
            elif opcion == "3":
                self.ver_jugadores_valiosos()
            elif opcion == "4":
                self.ver_goleadores()
            elif opcion == "5":
                break
            else:
                print("❌ Opción inválida")
    
    def ver_plantilla(self):
        """Muestra la plantilla completa del club"""
        print("\n" + "="*60)
        print(f"👥 PLANTILLA DE {self.club_usuario.nombre}")
        print("="*60)
        
        # Agrupar por posición
        porteros = [j for j in self.club_usuario.jugadores if j.posicion == "POR"]
        defensas = [j for j in self.club_usuario.jugadores if j.posicion == "DEF"]
        laterales = [j for j in self.club_usuario.jugadores if j.posicion == "LAT"]
        mediocentros = [j for j in self.club_usuario.jugadores if j.posicion == "MED"]
        extremos = [j for j in self.club_usuario.jugadores if j.posicion == "EXT"]
        delanteros = [j for j in self.club_usuario.jugadores if j.posicion == "DEL"]
        
        posiciones = [
            ("PORTEROS", porteros),
            ("DEFENSAS CENTRALES", defensas),
            ("LATERALES", laterales),
            ("MEDIOCENTROS", mediocentros),
            ("EXTREMOS", extremos),
            ("DELANTEROS", delanteros)
        ]
        
        for titulo, jugadores in posiciones:
            if jugadores:
                print(f"\n{titulo}:")
                print("-"*60)
                for jugador in sorted(jugadores, key=lambda j: j.habilidad, reverse=True):
                    print(f"  {jugador.nombre:<25} {jugador.edad} años | {jugador.habilidad} OVR | €{jugador.valor/1000000:.1f}M")
    
    def buscar_jugador(self):
        """Busca un jugador por nombre"""
        nombre = input("\nIntroduce el nombre del jugador: ").strip()
        
        encontrados = []
        for club in self.clubes.values():
            for jugador in club.jugadores:
                if nombre.lower() in jugador.nombre.lower():
                    encontrados.append((jugador, club))
        
        if encontrados:
            print(f"\n✅ Se encontraron {len(encontrados)} jugador(es):")
            for jugador, club in encontrados:
                print(f"  • {jugador.nombre} - {club.nombre} - {jugador.posicion} - {jugador.habilidad} OVR")
        else:
            print("❌ No se encontraron jugadores con ese nombre")
    
    def ver_jugadores_valiosos(self):
        """Muestra los jugadores más valiosos del club"""
        print("\n" + "="*60)
        print(f"💎 JUGADORES MÁS VALIOSOS DE {self.club_usuario.nombre}")
        print("="*60)
        
        jugadores_ordenados = sorted(self.club_usuario.jugadores, key=lambda j: j.valor, reverse=True)
        
        for i, jugador in enumerate(jugadores_ordenados[:10], 1):
            print(f"{i}. {jugador.nombre:<25} €{jugador.valor/1000000:.1f}M - {jugador.habilidad} OVR")
    
    def ver_goleadores(self):
        """Muestra los máximos goleadores del club"""
        print("\n" + "="*60)
        print(f"⚽ MÁXIMOS GOLEADORES DE {self.club_usuario.nombre}")
        print("="*60)
        
        jugadores_ordenados = sorted(self.club_usuario.jugadores, key=lambda j: j.goles_temporada, reverse=True)
        
        print(f"{'Pos':<4} {'Nombre':<25} {'Goles':<6} {'Asistencias':<12} {'Partidos':<8}")
        print("-"*60)
        
        for i, jugador in enumerate(jugadores_ordenados[:10], 1):
            print(f"{i:<4} {jugador.nombre:<25} {jugador.goles_temporada:<6} {jugador.asistencias_temporada:<12} {jugador.partidos_jugados:<8}")
    
    def jugar_jornada(self):
        """Simula una jornada de liga"""
        print("\n" + "="*60)
        print("⚽ SIMULANDO JORNADA DE LIGA")
        print("="*60)
        
        # Crear emparejamientos
        clubes_lista = list(self.clubes.values())
        random.shuffle(clubes_lista)
        
        partidos_jornada = []
        
        # Emparejar clubes
        for i in range(0, len(clubes_lista) - 1, 2):
            if i + 1 < len(clubes_lista):
                local = clubes_lista[i]
                visitante = clubes_lista[i + 1]
                
                # Asegurar que el club del usuario juegue en casa la mitad de las veces
                if local == self.club_usuario and random.random() < 0.5:
                    local, visitante = visitante, local
                elif visitante == self.club_usuario and random.random() < 0.5:
                    local, visitante = visitante, local
                
                partido = Partido(local, visitante)
                partidos_jornada.append(partido)
        
        # Si hay un número impar de clubes, uno descansa
        if len(clubes_lista) % 2 == 1:
            print("\n⚠️  Un club descansa esta jornada")
        
        # Simular partidos
        print("\nResultados de la jornada:")
        print("-"*60)
        
        for partido in partidos_jornada:
            goles_local, goles_visitante = partido.simular()
            print(f"{partido.local.nombre:<25} {goles_local} - {goles_visitante} {partido.visitante.nombre}")
            
            # Si juega el club del usuario, mostrar detalles
            if self.club_usuario in [partido.local, partido.visitante]:
                print(f"   🎯 Tu club {'gana' if (partido.local == self.club_usuario and goles_local > goles_visitante) or (partido.visitante == self.club_usuario and goles_visitante > goles_local) else 'empata' if goles_local == goles_visitante else 'pierde'}")
        
        self.historial_partidos.extend(partidos_jornada)
        print("\n✅ Jornada completada")
    
    def mercado_fichajes(self):
        """Muestra el mercado de fichajes"""
        print("\n" + "="*60)
        print("💰 MERCADO DE FICHAJES")
        print("="*60)
        
        # Recopilar todos los jugadores disponibles para venta
        jugadores_disponibles = []
        
        for club in self.clubes.values():
            for jugador in club.jugadores:
                # Jugadores felices son menos propensos a ser vendidos
                if jugador.felicidad < 60 or random.random() < 0.1:
                    jugadores_disponibles.append((jugador, club))
        
        if not jugadores_disponibles:
            print("\nNo hay jugadores disponibles en el mercado actualmente")
            return
        
        # Ordenar por valor
        jugadores_disponibles.sort(key=lambda x: x[0].valor, reverse=True)
        
        print(f"\n{'Nombre':<25} {'Edad':<5} {'Pos':<5} {'Habilidad':<10} {'Valor':<12} {'Club Actual':<20}")
        print("-"*80)
        
        for i, (jugador, club) in enumerate(jugadores_disponibles[:20], 1):
            print(f"{i}. {jugador.nombre:<25} {jugador.edad:<5} {jugador.posicion:<5} {jugador.habilidad:<10} €{jugador.valor/1000000:<8.1f}M {club.nombre:<20}")
        
        # Opción de fichar
        if self.club_usuario:
            print(f"\n💰 Tu presupuesto: €{self.club_usuario.presupuesto/1000000:.1f}M")
            
            try:
                opcion = int(input("\nNúmero del jugador que quieres fichar (0 para cancelar): "))
                
                if opcion > 0 and opcion <= len(jugadores_disponibles):
                    jugador_a_fichar, club_actual = jugadores_disponibles[opcion - 1]
                    
                    if self.club_usuario.presupuesto >= jugador_a_fichar.valor:
                        confirmar = input(f"¿Confirmar fichaje de {jugador_a_fichar.nombre} por €{jugador_a_fichar.valor/1000000:.1f}M? (s/n): ")
                        
                        if confirmar.lower() == 's':
                            # Realizar fichaje
                            self.club_usuario.presupuesto -= jugador_a_fichar.valor
                            club_actual.remover_jugador(jugador_a_fichar)
                            self.club_usuario.agregar_jugador(jugador_a_fichar)
                            jugador_a_fichar.felicidad = 85
                            
                            print(f"\n✅ ¡Fichaje completado! {jugador_a_fichar.nombre} ahora juega en {self.club_usuario.nombre}")
                        else:
                            print("❌ Fichaje cancelado")
                    else:
                        print("❌ No tienes suficiente presupuesto")
                elif opcion != 0:
                    print("❌ Opción inválida")
                    
            except ValueError:
                print("❌ Por favor, introduce un número")
    
    def avanzar_temporada(self):
        """Avanza a la siguiente temporada"""
        print("\n" + "="*60)
        print(f"🔄 AVANZANDO A TEMPORADA {self.temporada_actual + 1}")
        print("="*60)
        
        # Mostrar campeones de cada liga
        ligas = {}
        for club in self.clubes.values():
            if club.liga not in ligas:
                ligas[club.liga] = []
            ligas[club.liga].append(club)
        
        print("\n🏆 CAMPEONES DE LA TEMPORADA:")
        for liga, clubes in ligas.items():
            campeon = max(clubes, key=lambda c: c.puntos_liga)
            print(f"  {liga}: {campeon.nombre} ({campeon.puntos_liga} puntos)")
        
        # Envejecer jugadores
        for club in self.clubes.values():
            for jugador in club.jugadores:
                jugador.envejecer()
        
        # Resetear estadísticas de temporada
        for club in self.clubes.values():
            club.resetear_estadisticas_temporada()
        
        # Generar nuevos jugadores jóvenes
        self.generar_jovenes_promesas()
        
        self.temporada_actual += 1
        print(f"\n✅ Temporada {self.temporada_actual} iniciada")
    
    def generar_jovenes_promesas(self):
        """Genera algunos jugadores jóvenes promesa"""
        nombres_jovenes = [
            {"nombre": "Endrick Felipe", "edad": 17, "nacionalidad": "Brasil", "posicion": "DEL", "valor": 30000000, "habilidad": 75},
            {"nombre": "Warren Zaire-Emery", "edad": 17, "nacionalidad": "Francia", "posicion": "MED", "valor": 25000000, "habilidad": 74},
            {"nombre": "Evan Ferguson", "edad": 19, "nacionalidad": "Irlanda", "posicion": "DEL", "valor": 35000000, "habilidad": 76},
            {"nombre": "Arda Guler", "edad": 18, "nacionalidad": "Turquía", "posicion": "MED", "valor": 28000000, "habilidad": 75},
        ]
        
        for datos in nombres_jovenes:
            if random.random() < 0.5:  # 50% de probabilidad de aparecer
                jugador = Jugador(datos)
                club_aleatorio = random.choice(list(self.clubes.values()))
                club_aleatorio.agregar_jugador(jugador)
        
        print("✨ Se han generado nuevas promesas del fútbol mundial")
    
    def guardar_partida(self):
        """Guarda el estado actual del juego"""
        datos_guardado = {
            "temporada": self.temporada_actual,
            "club_usuario": self.club_usuario.nombre if self.club_usuario else None,
            "clubes": {nombre: club.to_dict() for nombre, club in self.clubes.items()},
            "historial_partidos": len(self.historial_partidos)
        }
        
        with open("guardado_carrera.json", "w") as f:
            json.dump(datos_guardado, f, indent=2, ensure_ascii=False)
        
        print("✅ Partida guardada correctamente en 'guardado_carrera.json'")
    
    def cargar_partida(self):
        """Carga una partida guardada"""
        if not os.path.exists("guardado_carrera.json"):
            print("❌ No hay partidas guardadas")
            return False
        
        try:
            with open("guardado_carrera.json", "r") as f:
                datos = json.load(f)
            
            self.temporada_actual = datos["temporada"]
            
            # Reconstruir clubes
            self.clubes = {}
            for nombre, datos_club in datos["clubes"].items():
                club = Club({
                    "nombre": datos_club["nombre"],
                    "liga": datos_club["liga"],
                    "pais": datos_club["pais"],
                    "presupuesto": datos_club["presupuesto"],
                    "prestigio": datos_club["prestigio"]
                })
                club.puntos_liga = datos_club["puntos_liga"]
                club.partidos_jugados = datos_club["partidos_jugados"]
                club.goles_a_favor = datos_club["goles_a_favor"]
                club.goles_en_contra = datos_club["goles_en_contra"]
                
                # Reconstruir jugadores
                for datos_jugador in datos_club["jugadores"]:
                    jugador = Jugador(datos_jugador)
                    club.agregar_jugador(jugador)
                
                self.clubes[nombre] = club
            
            # Restaurar club del usuario
            if datos["club_usuario"] and datos["club_usuario"] in self.clubes:
                self.club_usuario = self.clubes[datos["club_usuario"]]
            
            print("✅ Partida cargada correctamente")
            return True
            
        except Exception as e:
            print(f"❌ Error al cargar la partida: {e}")
            return False
    
    def ejecutar(self):
        """Ejecuta el bucle principal del juego"""
        print("\n" + "="*60)
        print("⚽ BIENVENIDO AL MODO CARRERA DE FÚTBOL ⚽")
        print("="*60)
        
        # Preguntar si quiere cargar partida
        if os.path.exists("guardado_carrera.json"):
            cargar = input("\n¿Quieres cargar la última partida guardada? (s/n): ")
            if cargar.lower() == 's' and self.cargar_partida():
                print(f"\nContinuando con {self.club_usuario.nombre if self.club_usuario else 'sin club'}")
            else:
                self.inicializar_juego()
                self.seleccionar_club_usuario()
        else:
            self.inicializar_juego()
            self.seleccionar_club_usuario()
        
        # Bucle principal del juego
        while True:
            self.mostrar_menu_principal()
            
            opcion = input("\nElige una opción: ")
            
            if opcion == "1":
                self.ver_clasificacion()
            elif opcion == "2":
                self.gestionar_club()
            elif opcion == "3":
                self.jugar_jornada()
                
                # Verificar si se debe avanzar de temporada
                if self.club_usuario and self.club_usuario.partidos_jugados >= 38:
                    print("\n🎉 ¡Temporada completada!")
                    self.avanzar_temporada()
            elif opcion == "4":
                self.mercado_fichajes()
            elif opcion == "5":
                if self.club_usuario:
                    self.ver_goleadores()
                else:
                    print("❌ Primero selecciona un club")
            elif opcion == "6":
                self.guardar_partida()
            elif opcion == "7":
                print("\n👋 ¡Gracias por jugar! Hasta pronto.")
                break
            else:
                print("❌ Opción inválida")


if __name__ == "__main__":
    juego = JuegoCarrera()
    juego.ejecutar()
