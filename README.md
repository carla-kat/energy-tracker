# 📊 Energy Tracker

Energy Tracker es una aplicación de terminal hecha en Python que permite registrar, visualizar y analizar hábitos diarios como energía, ánimo y sueño.

El proyecto empezó como un ejercicio básico y ha evolucionado a una herramienta simple de análisis personal de datos.

---

## 🚀 Funcionalidades

- ➕ Añadir registro diario (energía, ánimo, sueño y notas)
- 📜 Ver historial completo de registros
- 📈 Calcular medias de los últimos días
- 📊 Resumen semanal con comparación de tendencias
- 🏆 Mostrar automáticamente el último registro en el menú
- 🔄 Sobrescritura automática si ya existe un registro del mismo día

---

## 🧠 Qué hace esta app

La aplicación permite llevar un control básico de hábitos diarios y obtener una visión general de cómo cambian con el tiempo.

Ejemplo de datos registrados:

- Energía (0–10)
- Ánimo (0–10)
- Sueño (0–10)
- Notas personales

---

## 🛠️ Tecnologías utilizadas

- Python 3
- JSON (almacenamiento de datos)
- Módulos estándar (`json`, `datetime`, `os`)

---

## 📌 Cómo funciona

- El usuario introduce sus datos diarios.
- Los datos se guardan en un archivo JSON local.
- La app permite visualizar:
   - Historial completo
   -  Promedios de los últimos días
   - Resumen semanal con evolución

---

## 📊 Ejemplo de uso

```text
=================================
        📊 ENERGY TRACKER        
=================================

📌 Último registro: 2026-06-19
⚡ Energía: 7 | 😊 Ánimo: 6 | 😴 Sueño: 8
---------------------------------

1. ➕ Añadir entrada diaria
2. 📜 Ver historial
3. 📈 Resumen semanal
0. 🚪 Salir
```