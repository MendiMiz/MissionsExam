from model.target import Target


def convert_targets_to_models(json_data):
    return [Target(a["Target City"], a["Priority"]) for a in json_data]

