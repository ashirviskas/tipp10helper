from db_generator import KeyboardLayoutsGenerator


def main():
    klg = KeyboardLayoutsGenerator(primary_start=13000)
    klg.generate_full_layout()


if __name__ == '__main__':
    main()
