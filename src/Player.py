import json
from pathlib import Path

class Player:
    def __init__(self, name, data=None):
        self.name = name
        if data is not None:
            self.data = data
        else:
            self.data = {
                "name" : name,
                "modes" : [
                    {
                        "name" : "Chord Identifier",
                        "types" : ["major_triad","minor_triad","augmented_triad","diminished_triad"],
                        "inversions" : None
                    },
                ]
            }
            BASE_DIR = Path(__file__).resolve().parent
            data_file = BASE_DIR.parent / "profiles" / f"{self.name}.json"
            json_string = json.dumps(self.data, indent=4)
            with open(data_file, "w") as f:
                f.write(json_string)

    def __del__(self):
        # Destructor, we will have this save state when executed
        pass
