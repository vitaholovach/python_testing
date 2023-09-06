import argparse

from main import Human

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Human instance to JSON or XML")
    parser.add_argument("format", choices=["json", "xml"], help="Choose the output format (json/xml)")

    args = parser.parse_args()

    human = Human("Vita", 28, "female", 1994)

    if args.format == "json":
        result = human.convert_to_json()
        with open("human.json", "w") as json_file:
            json_file.write(result)
        print("JSON file 'human.json' created.")
    elif args.format == "xml":
        result = human.convert_to_xml()
        with open("human.xml", "w") as xml_file:
            xml_file.write(result)
        print("XML file 'human.xml' created.")
