import csv
import json
import sys


if __name__ == "__main__":
    data = []
    try:
        with open("./Assets/iris.csv") as f:
            csv_data = csv.DictReader(f)
            for rec in csv_data:
                data.append(rec)

    except IOError:
        print("Failed to load file.")

    if not data:
        raise ValueError("No Data Found!")

    print(f"Type of data: {type(data)}")
    species = set()
    counts = {}
    for s in data:
        species.add(s["species"])
        if s["species"] in counts:
            counts[s["species"]] += 1
        else:
            counts[s["species"]] = 1

    result = {
        "species": list(species),
        "counts": counts
    }

    try:
        with open("Assets./iris.json", mode="w") as f:
            json.dump(result, f, indent=4)
    except IOError:
        print("Can not write JSON file.")
    except:
        print(sys.exc_info())
