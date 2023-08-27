
def transforming_contact_data(file: str):
    """extrae información de cada contacto del archivo y la transforma"""

    result = []
    personal = {}
    with file.open(encoding="utf-8") as f:
        total_lines = len(f.readlines())
        line_counter = 0

        # volver al inicio de cada archivo
        f.seek(0)
        for line in f:
            line_counter += 1
            line_converted_to_array = line.split(": ")
            empty_line = len(line_converted_to_array) == 1
            last_line = total_lines == line_counter

            if empty_line:
                result.append(personal)
                personal = {}
            elif last_line:
                key = line_converted_to_array[0].strip()
                val = line_converted_to_array[1].strip()
                personal[key] = val
                result.append(personal)
            else:
                key = line_converted_to_array[0].strip()
                val = line_converted_to_array[1].strip()
                personal[key] = val

    return result
