from tracker import add_entry, load_data, get_last_days, get_last_entry
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear()

    last = get_last_entry()

    print("=================================")
    print("        📊 ENERGY TRACKER        ")
    print("=================================\n")

    if last:
        print(f"📌 Último registro: {last['date']}")
        print(f"⚡ Energía: {last['energy']} | 😊 Ánimo: {last['mood']} | 😴 Sueño: {last['sleep']}")
        print("-" * 40)

    print("1. ➕ Añadir entrada diaria")
    print("2. 📜 Ver historial")
    print("3. 📈 Resumen semanal")
    print("4. 📊 Estadísticas")
    print("5. 📈 Tendencias")
    print("0. 🚪 Salir\n")

def show_history():
    data = load_data()

    print("\n📜 HISTORIAL\n")

    for d in data:
     print(f"📅 {d['date']}")
     print(f"   ⚡ Energía: {d['energy']}")
     print(f"   😊 Ánimo: {d['mood']}")
     print(f"   😴 Sueño: {d['sleep']}")
     print(f"   📝 Notas: {d['notes']}")
     print("-" * 30)    
       

def show_average():
    data = get_last_days(7)

    if not data:
        print("No hay datos")
        return

    energy = sum(d["energy"] for d in data) / len(data)
    mood = sum(d["mood"] for d in data) / len(data)
    sleep = sum(d["sleep"] for d in data) / len(data)

    print(f"Media energía: {energy:.1f}")
    print(f"Media ánimo: {mood:.1f}")
    print(f"Media sueño: {sleep:.1f}")


def show_week_summary():
    data = get_last_days(14)

    if len(data) < 7:
        print("No hay suficientes datos (mínimo 7 días)")
        return

    current = data[-7:]
    previous = data[-14:-7]

    def avg(field, dataset):
        return sum(d[field] for d in dataset) / len(dataset)

    print("\n📈 RESUMEN SEMANAL\n")

    for field, emoji in [("energy", "⚡"), ("mood", "😊"), ("sleep", "😴")]:
        curr = avg(field, current)
        prev = avg(field, previous)

        diff = curr - prev

        trend = "→ igual"
        if diff > 0.2:
            trend = "📈 mejorando"
        elif diff < -0.2:
            trend = "📉 bajando"

        print(f"{emoji} {field}: {curr:.1f} ({trend})")


def ask_score(text):
    while True:
        try:
            value = int(input(text))

            if 0 <= value <= 10:
                return value

            print("Introduce un número entre 0 y 10.")

        except ValueError:
            print("Eso no es un número.")

def get_score(text):
    while True:
        try:
            value = int(input(text))

            if 0 <= value <= 10:
                return value

            print("❌ Debe estar entre 0 y 10")

        except ValueError:
            print("❌ Introduce un número válido")

def show_stats():
    data = load_data()

    if not data:
        print("No hay datos")
        return
    
    best_energy = max(data, key=lambda d: d["energy"])
    worst_energy = min(data, key=lambda d: d["energy"])

    best_mood = max(data, key=lambda d: d["mood"])
    worst_mood = min(data, key=lambda d: d["mood"])

    best_sleep = max(data, key=lambda d: d["sleep"])
    worst_sleep = min(data, key=lambda d: d["sleep"])

    print("\n📊 ESTADÍSTICAS\n")

    print(f"⚡ Mejor día de energía: {best_energy['date']} ({best_energy['energy']})")
    print(f"⚡ Peor día de energía: {worst_energy['date']} ({worst_energy['energy']})")

    print(f"😊 Mejor día de ánimo: {best_mood['date']} ({best_mood['mood']})")
    print(f"😊 Peor día de ánimo: {worst_mood['date']} ({worst_mood['mood']})")

    print(f"😴 Mejor día de sueño: {best_sleep['date']} ({best_sleep['sleep']})")
    print(f"😴 Peor día de sueño: {worst_sleep['date']} ({worst_sleep['sleep']})")

def get_average(data, field):
    return sum(d[field] for d in data) / len(data)

def show_trends():
    data = load_data()

    if len(data) < 14:
        print("Necesitas al menos 14 registros para analizar tendencias")
        return
    
    previous_week = data[-14:-7]
    current_week = data[-7:]

    energy_before = get_average(previous_week, "energy")
    energy_now = get_average(current_week, "energy")
    print(get_trend(energy_before, energy_now))

def get_trend(old, new):
    if new > old:
        return "📈 Mejorando"
    
    elif new < old:
        return "📉 Empeorando"
    
    else:
        return "➡️ Estable"

while True:
    menu()
    choice = input("> ")

    if choice == "1":
        e = get_score("Energía (0-10): ")
        m = get_score("Ánimo (0-10): ")
        s = get_score("Sueño (0-10): ")
        n = input("Notas: ")

        add_entry(e, m, s, n)

        input("\n✔ Guardado. Pulsa Enter para volver al menú...")

    elif choice == "2":
        clear()
        show_history()
        input("\nPulsa Enter para continuar...")

    elif choice == "3":
        clear()
        show_week_summary()
        input("\nPulsa Enter para continuar...")

    elif choice == "4":
        clear()
        show_stats()
        input("\nPulsa Enter para continuar...")

    elif choice == "5":
        clear()
        show_trends()
        input("\nPulsa Enter para continuar...")
    
    elif choice == "0":
        break