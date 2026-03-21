import json

try:
    with open('apollo_galaxy.json', 'r') as f:
        data = json.load(f)

    spikes_column = data['galaxy']['spikes']
    names_found = 0
    examples = []

    # Iterate through the files to find one that has satellites/spikes
    for i, file_spikes in enumerate(spikes_column):
        if file_spikes: # If this file has spikes
            # Check the first spike
            first_spike = file_spikes[0]
            # Schema says index 0 is "name"
            if isinstance(first_spike[0], str):
                names_found += 1
                if len(examples) < 3:
                    file_name = data['galaxy']['names'][i]
                    examples.append(f"File '{file_name}' -> Function '{first_spike[0]}'")

    print(f"--- Inspection Report ---")
    if names_found > 0:
        print(f"✅ YES. Function names are saved.")
        print(f"Found {names_found} files containing named satellites.")
        print(f"Examples:")
        for ex in examples:
            print(f"  - {ex}")
    else:
        print(f"❌ NO. Function names appear to be missing or not strings.")

except Exception as e:
    print(f"Error inspecting file: {e}")