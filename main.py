from core.db_generator import KeyboardLayoutsGenerator


def main():
    klg = KeyboardLayoutsGenerator(primary_start=13000)
    klg.do_solution()


if __name__ == '__main__':
    main()
