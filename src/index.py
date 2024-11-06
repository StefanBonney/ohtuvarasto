"""main"""

from varasto import Varasto

def print_initial_state(mehua, olutta):
    """initial"""
    print(
        "Luonnin jälkeen:\n"
        f"Mehuvarasto: {mehua}\n"
        f"Olutvarasto: {olutta}\n"
    )

def print_olut_getter_values(olutta):
    """getter"""
    print(
        "Olut getterit:\n"
        f"saldo = {olutta.saldo}\n"
        f"tilavuus = {olutta.tilavuus}\n"
        f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}\n"
    )

def perform_mehu_operations(mehua):
    """operations"""
    print(
        "Mehu setterit:\n"
        "Lisätään 50.7\n"
        f"Mehuvarasto: {mehua}\n"
    )
    mehua.lisaa_varastoon(50.7)
    print(
        "Otetaan 3.14\n"
        f"Mehuvarasto: {mehua}\n"
    )
    mehua.ota_varastosta(3.14)

def handle_errors():
    """errors"""
    print(
        "Virhetilanteita:\n"
        "Varasto(-100.0);\n"
        f"{Varasto(-100.0)}\n"
        "Varasto(100.0, -50.7)\n"
        f"{Varasto(100.0, -50.7)}\n"
    )

def perform_olut_operations(olutta):
    """operations"""
    print(f"Olutvarasto: {olutta}\n")
    print("olutta.lisaa_varastoon(1000.0)\n")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}\n")

def perform_mehu_negative_operations(mehua):
    """negative"""
    print(
        f"Mehuvarasto: {mehua}\n"
        "mehua.lisaa_varastoon(-666.0)\n"
    )
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}\n")

def perform_getter_operations(olutta, mehua):
    """getter"""
    print(f"Olutvarasto: {olutta}\n")
    print("olutta.ota_varastosta(1000.0)\n")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}\n")
    print(f"Olutvarasto: {olutta}\n")

    print(f"Mehuvarasto: {mehua}\n")
    print("mehua.otaVarastosta(-32.9)\n")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}\n")
    print(f"Mehuvarasto: {mehua}\n")

def main():
    """Main Function"""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print_initial_state(mehua, olutta)
    print_olut_getter_values(olutta)
    perform_mehu_operations(mehua)
    handle_errors()
    perform_olut_operations(olutta)
    perform_mehu_negative_operations(mehua)
    perform_getter_operations(olutta, mehua)

if __name__ == "__main__":
    main()
